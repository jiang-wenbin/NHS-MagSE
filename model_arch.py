# 1.865M
CRN_12_128 = {
    # (in_channels, out_channels, kernel_size, stride, padding)
    "encoder":
        ((  1,  32, (5, 2), (2, 1)),
         ( 32,  64, (5, 2), (2, 1)),
         ( 64,  96, (5, 2), (2, 1)),
         ( 96, 128, (5, 2), (2, 1)),
         (128, 128, (5, 2), (2, 1)),
         (128, 128, (5, 2), (2, 1))),
    # (input_size, hidden_size, num_layers)
    "lstm": (128, 128, 2),
    # (in_channels, out_channels, kernel_size, stride, padding, output_padding, is_last)
    "decoder":
        ((256, 128, (5, 2), (2, 1)),
         (256, 128, (5, 2), (2, 1)),
         (256,  96, (5, 2), (2, 1)),
         (192,  64, (5, 2), (2, 1)),
         (128,  32, (5, 2), (2, 1)),
         ( 64,   1, (5, 2), (2, 1), (0, 0), (0, 0), True))
}

# 1.5M
CRN_12_120 = {
    # (in_channels, out_channels, kernel_size, stride, padding)
    "encoder":
        ((  1,  32, (5, 2), (2, 1)),
         ( 32,  64, (5, 2), (2, 1)),
         ( 64,  64, (5, 2), (2, 1)),
         ( 64, 120, (5, 2), (2, 1)),
         (120, 120, (5, 2), (2, 1)),
         (120, 120, (5, 2), (2, 1))),
    # (input_size, hidden_size, num_layers)
    "lstm": (120, 120, 2),
    # (in_channels, out_channels, kernel_size, stride, padding, output_padding, is_last)
    "decoder":
        ((240, 120, (5, 2), (2, 1)),
         (240, 120, (5, 2), (2, 1)),
         (240,  64, (5, 2), (2, 1)),
         (128,  64, (5, 2), (2, 1)),
         (128,  32, (5, 2), (2, 1)),
         ( 64,   1, (5, 2), (2, 1), (0, 0), (0, 0), True))
}

# 1.016M
CRN_12_96 = {
    # (in_channels, out_channels, kernel_size, stride, padding)
    "encoder":
        ((  1, 24, (5, 2), (2, 1)),
         ( 24, 48, (5, 2), (2, 1)),
         ( 48, 64, (5, 2), (2, 1)),
         ( 64, 96, (5, 2), (2, 1)),
         ( 96, 96, (5, 2), (2, 1)),
         ( 96, 96, (5, 2), (2, 1))),
    # (input_size, hidden_size, num_layers)
    "lstm": (96, 96, 2),
    # (in_channels, out_channels, kernel_size, stride, padding, output_padding, is_last)
    "decoder":
        ((192, 96, (5, 2), (2, 1)),
         (192, 96, (5, 2), (2, 1)),
         (192, 64, (5, 2), (2, 1)),
         (128, 48, (5, 2), (2, 1)),
         ( 96, 24, (5, 2), (2, 1)),
         ( 48,  1, (5, 2), (2, 1), (0, 0), (0, 0), True))
}

# 513.937K
CRN_12_64 = {
    # (in_channels, out_channels, kernel_size, stride, padding)
    "encoder":
        ((  1, 16, (5, 2), (2, 1)),
         ( 16, 32, (5, 2), (2, 1)),
         ( 32, 64, (5, 2), (2, 1)),
         ( 64, 64, (5, 2), (2, 1)),
         ( 64, 64, (5, 2), (2, 1)),
         ( 64, 64, (5, 2), (2, 1))),
    # (input_size, hidden_size, num_layers)
    "lstm": (64, 64, 2),
    # (in_channels, out_channels, kernel_size, stride, padding, output_padding, is_last)
    "decoder":
        ((128, 64, (5, 2), (2, 1)),
         (128, 64, (5, 2), (2, 1)),
         (128, 64, (5, 2), (2, 1)),
         (128, 32, (5, 2), (2, 1)),
         ( 64, 16, (5, 2), (2, 1)),
         ( 32,  1, (5, 2), (2, 1), (0, 0), (0, 0), True))
}

# 3.7M
CRN_12_256 = {
    # (in_channels, out_channels, kernel_size, stride, padding)
    "encoder":
        ((  1,  60, (5, 2), (2, 1)),
         ( 60, 128, (5, 2), (2, 1)),
         (128, 128, (5, 2), (2, 1)),
         (128, 128, (5, 2), (2, 1)),
         (128, 128, (5, 2), (2, 1)),
         (128, 256, (5, 2), (2, 1))),
    # (input_size, hidden_size, num_layers)
    "lstm": (256, 256, 2),
    # (in_channels, out_channels, kernel_size, stride, padding, output_padding, is_last)
    "decoder":
        ((512, 128, (5, 2), (2, 1)),
         (256, 128, (5, 2), (2, 1)),
         (256, 128, (5, 2), (2, 1)),
         (256, 128, (5, 2), (2, 1)),
         (256,  60, (5, 2), (2, 1)),
         (120,   1, (5, 2), (2, 1), (0, 0), (0, 0), True))
}

# 3.0M
CRN_12_192 = {
    # (in_channels, out_channels, kernel_size, stride, padding)
    "encoder":
        ((  1,  60, (5, 2), (2, 1)),
         ( 60, 128, (5, 2), (2, 1)),
         (128, 128, (5, 2), (2, 1)),
         (128, 128, (5, 2), (2, 1)),
         (128, 128, (5, 2), (2, 1)),
         (128, 190, (5, 2), (2, 1))),
    # (input_size, hidden_size, num_layers)
    "lstm": (190, 190, 2),
    # (in_channels, out_channels, kernel_size, stride, padding, output_padding, is_last)
    "decoder":
        ((380, 128, (5, 2), (2, 1)),
         (256, 128, (5, 2), (2, 1)),
         (256, 128, (5, 2), (2, 1)),
         (256, 128, (5, 2), (2, 1)),
         (256,  60, (5, 2), (2, 1)),
         (120,   1, (5, 2), (2, 1), (0, 0), (0, 0), True))
}

# 2.0M
CRN_12_148 = {
    # (in_channels, out_channels, kernel_size, stride, padding)
    "encoder":
        ((  1,  32, (5, 2), (2, 1)),
         ( 32,  64, (5, 2), (2, 1)),
         ( 64,  96, (5, 2), (2, 1)),
         ( 96, 128, (5, 2), (2, 1)),
         (128, 128, (5, 2), (2, 1)),
         (128, 145, (5, 2), (2, 1))),
    # (input_size, hidden_size, num_layers)
    "lstm": (145, 145, 2),
    # (in_channels, out_channels, kernel_size, stride, padding, output_padding, is_last)
    "decoder":
        ((290, 128, (5, 2), (2, 1)),
         (256, 128, (5, 2), (2, 1)),
         (256,  96, (5, 2), (2, 1)),
         (192,  64, (5, 2), (2, 1)),
         (128,  32, (5, 2), (2, 1)),
         ( 64,   1, (5, 2), (2, 1), (0, 0), (0, 0), True))
}