import numpy as np


def calculate_moving_average(data, window):
    if len(data) < window:
        return [None] * len(data)
    return [None] * (window - 1) + [
        np.mean(data[i - window + 1 : i + 1]) for i in range(window - 1, len(data))
    ]


def normalize_column(data):
    mean = np.mean(data)
    std = np.std(data)

    if std == 0:
        return [0] * len(data)  # Avoid division by zero

    return [(x - mean) / std for x in data]
