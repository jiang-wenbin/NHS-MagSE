import torch
from torch import nn
import torch.nn.functional as F


def _padded_cat(x, y, dim=1):
    x_pad = F.pad(x, (0, y.shape[3] - x.shape[3], 
                      0, y.shape[2] - x.shape[2]))
    z = torch.cat((x_pad, y), dim=dim)
    return z


class _ConvBlock(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size=(3, 2), stride=(2, 1), 
                 padding=(0, 1), causal=True):
        super().__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding)
        self.norm = nn.BatchNorm2d(num_features=out_channels)
        self.activation = nn.PReLU()
        self.causal = causal
        nn.init.xavier_uniform_(self.conv.weight)
        nn.init.zeros_(self.conv.bias)

    def forward(self, x):
        """
        2D Causal convolution.
        Args:
            x: [B, C, F, T]
        Returns:
            [B, C, F, T]
        """
        x = self.conv(x)
        if self.causal is True:
            x = x[:, :, :, :-1]
        x = self.norm(x)
        x = self.activation(x)
        return x


class _TransConvBlock(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size=(3, 2), stride=(2, 1),
                 padding=(0, 0), output_padding=(0, 0), is_last=False, causal=True):
        super().__init__()
        self.conv = nn.ConvTranspose2d(in_channels, out_channels, kernel_size, stride, 
                                       padding, output_padding)
        self.is_last = is_last
        self.causal = causal
        self.norm = nn.BatchNorm2d(num_features=out_channels)
        self.activation = nn.PReLU()
        nn.init.xavier_uniform_(self.conv.weight)
        nn.init.zeros_(self.conv.bias)

    def forward(self, x):
        """
        2D Causal convolution.
        Args:
            x: [B, C, F, T]
        Returns:
            [B, C, F, T]
        """
        x = self.conv(x)
        if self.causal is True:
            x = x[:, :, :, :-1]
        if self.is_last is False:
            x = self.norm(x)
            x = self.activation(x)
        return x


class CRN(nn.Module):    
    def __init__(self, param, debug=False):
        super(CRN, self).__init__()
        self.debug = debug
        self.encoder = nn.ModuleList([_ConvBlock(*item) for item in param["encoder"]])
        self.lstm_layer = nn.LSTM(*param["lstm"])
        self.decoder = nn.ModuleList([_TransConvBlock(*item) for item in param["decoder"]])

    def forward(self, x):
        self.lstm_layer.flatten_parameters()
        e = x
        e_list = []
        for i, layer in enumerate(self.encoder):
            e = layer(e)
            e_list.append(e)
            if self.debug:
                print(f"encoder_{i}: {e.shape}")   

        batch_size, n_channels, n_freq, n_frames = e.shape

        lstm_in = e.reshape(batch_size, n_channels*n_freq, n_frames).permute(0, 2, 1)
        lstm_out, _ = self.lstm_layer(lstm_in)
        lstm_out = lstm_out.permute(0, 2, 1).reshape(batch_size, n_channels, n_freq, n_frames)
        
        idx = len(e_list)
        d = lstm_out
        for i, layer in enumerate(self.decoder):
            idx = idx - 1            
            d = layer(_padded_cat(d, e_list[idx]))
            if self.debug:
                print(f"decoder_{i}: {d.shape}")
        
        return d


# The DCCRN uses the open-source implementation in asteroid
from asteroid.masknn.recurrent import DCCRMaskNet
class DCCRN(torch.nn.Module):
    def __init__(self, n_freqs, arch="DCCRN-CL", mask=True):
        super().__init__()
        mask_bound = "tanh" if mask is True else None
        self.model = DCCRMaskNet.default_architecture(
            architecture = arch, n_freqs = n_freqs, mask_bound=mask_bound)
        
    def forward(self, noisy):
        noisy = noisy.squeeze(1)
        noisy = noisy[..., :-1, :] # Remove Nyquist frequency bin
        est = self.model(noisy)
        est = torch.nn.functional.pad(est, [0, 0, 0, 1]) # Pad Nyquist frequency bin
        return est