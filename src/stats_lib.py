import math

def mean(data):
    """Calculates the arithmetic mean."""
    if not data:
        return None
    return sum(data) / len(data)

def median(data):
    """Calculates the median."""
    if not data:
        return None
    sorted_data = sorted(data)
    n = len(data)
    if n % 2 == 0:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        return sorted_data[n // 2]

def mode(data):
    """Calculates the mode."""
    if not data:
        return None
    counts = {}
    for x in data:
        counts[x] = counts.get(x, 0) + 1
    
    max_count = max(counts.values())
    modes = [x for x, count in counts.items() if count == max_count]
    if len(modes) == 1:
        return modes[0]
    return modes # Return list if multiple modes

def variance(data, population=True):
    """Calculates the variance."""
    if not data or len(data) < 2:
        return None
    mu = mean(data)
    sum_sq_diff = sum((x - mu) ** 2 for x in data)
    if population:
        return sum_sq_diff / len(data)
    else:
        return sum_sq_diff / (len(data) - 1)

def std_dev(data, population=True):
    """Calculates the standard deviation."""
    var = variance(data, population)
    if var is None:
        return None
    return math.sqrt(var)

def covariance(data_x, data_y, population=True):
    """Calculates the covariance between two datasets."""
    if len(data_x) != len(data_y) or len(data_x) < 2:
        return None
    
    mu_x = mean(data_x)
    mu_y = mean(data_y)
    
    sum_diff_prod = sum((x - mu_x) * (y - mu_y) for x, y in zip(data_x, data_y))
    
    if population:
        return sum_diff_prod / len(data_x)
    else:
        return sum_diff_prod / (len(data_x) - 1)

def correlation(data_x, data_y):
    """Calculates the Pearson correlation coefficient."""
    cov = covariance(data_x, data_y)
    std_x = std_dev(data_x)
    std_y = std_dev(data_y)
    
    if cov is None or std_x is None or std_y is None or std_x == 0 or std_y == 0:
        return None
    
    return cov / (std_x * std_y)

def linear_regression(data_x, data_y):
    """Calculates the slope and intercept of the linear regression line."""
    if len(data_x) != len(data_y) or len(data_x) < 2:
        return None
    
    mu_x = mean(data_x)
    mu_y = mean(data_y)
    
    numerator = sum((x - mu_x) * (y - mu_y) for x, y in zip(data_x, data_y))
    denominator = sum((x - mu_x) ** 2 for x in data_x)
    
    if denominator == 0:
        return None
    
    slope = numerator / denominator
    intercept = mu_y - (slope * mu_x)
    
    return slope, intercept
