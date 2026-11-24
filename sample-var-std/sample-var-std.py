import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    x = np.array(x)
    
    mean = np.mean(x)
    deviations = x - mean
    squared_deviations = deviations ** 2

    variance = np.sum(squared_deviations) / (len(x) - 1)

    standard_deviation = np.sqrt(variance)

    return {
        "variance": float(variance),
        "standard_deviation": float(standard_deviation)
    }

    
    