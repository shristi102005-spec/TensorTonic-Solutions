from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    mean = np.mean(x)
    median = np.median(x)

    freq = Counter(x)
    max_freq = max(freq.values())

    mode = min(
        value for value, count in freq.items()
        if count == max_freq
    )

    return {
        "mean": float(mean),
        "median": float(median),
        "mode": float(mode)
    }