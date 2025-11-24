import math


def mean(data):
    if not data:
        return None
    return sum(data) / len(data)


def median(data):
    if not data:
        return None
    sorted_data = sorted(data)
    n = len(data)
    if n % 2 == 0:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        return sorted_data[n // 2]


def mode(data):
    if not data:
        return None
    counts = {}
    for x in data:
        counts[x] = counts.get(x, 0) + 1

    max_count = max(counts.values())
    modes = [x for x, count in counts.items() if count == max_count]
    if len(modes) == 1:
        return modes[0]
    return modes


def variance(data, population=True):
    if not data or len(data) < 2:
        return None
    mu = mean(data)
    sum_sq_diff = sum((x - mu) ** 2 for x in data)
    if population:
        return sum_sq_diff / len(data)
    else:
        return sum_sq_diff / (len(data) - 1)


def std_dev(data, population=True):
    var = variance(data, population)
    if var is None:
        return None
    return math.sqrt(var)


def covariance(data_x, data_y, population=True):
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
    cov = covariance(data_x, data_y)
    std_x = std_dev(data_x)
    std_y = std_dev(data_y)

    if cov is None or std_x is None or std_y is None or std_x == 0 or std_y == 0:
        return None

    return cov / (std_x * std_y)


def linear_regression(data_x, data_y):
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


def z_score(data, value):
    mu = mean(data)
    sigma = std_dev(data)

    if mu is None or sigma is None or sigma == 0:
        return None
    return (value - mu) / sigma


def percentile(data, p):
    if not data or p < 0 or p > 100:
        return None

    sorted_data = sorted(data)
    n = len(data)
    k = (n - 1) * (p / 100)
    f = math.floor(k)
    c = math.ceil(k)

    if f == c:
        return sorted_data[int(k)]

    d0 = sorted_data[int(f)] * (c - k)
    d1 = sorted_data[int(c)] * (k - f)
    return d0 + d1


def iqr(data):
    q1 = percentile(data, 25)
    q3 = percentile(data, 75)

    if q1 is None or q3 is None:
        return None
    return q3 - q1


def skewness(data):
    if not data or len(data) < 3:
        return None

    mu = mean(data)
    sigma = std_dev(data)

    if sigma == 0:
        return None

    n = len(data)
    sum_cubed_diff = sum((x - mu) ** 3 for x in data)

    return (n / ((n - 1) * (n - 2))) * (sum_cubed_diff / (sigma**3))


def kurtosis(data):
    if not data or len(data) < 4:
        return None

    mu = mean(data)
    sigma = std_dev(data)

    if sigma == 0:
        return None

    n = len(data)
    sum_fourth_diff = sum((x - mu) ** 4 for x in data)

    term1 = (n * (n + 1)) / ((n - 1) * (n - 2) * (n - 3))
    term2 = sum_fourth_diff / (sigma**4)
    term3 = (3 * (n - 1) ** 2) / ((n - 2) * (n - 3))

    return term1 * term2 - term3
