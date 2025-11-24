def set_union(set_a, set_b):
    if not isinstance(set_a, list) or not isinstance(set_b, list):
        return None

    result = []
    for x in set_a:
        if x not in result:
            result.append(x)

    for x in set_b:
        if x not in result:
            result.append(x)
    return result


def set_intersection(set_a, set_b):
    if not isinstance(set_a, list) or not isinstance(set_b, list):
        return None

    result = []
    for x in set_a:
        if x in set_b and x not in result:
            result.append(x)
    return result


def set_difference(set_a, set_b):
    if not isinstance(set_a, list) or not isinstance(set_b, list):
        return None

    result = []
    for x in set_a:
        if x not in set_b and x not in result:
            result.append(x)
    return result


def set_symmetric_difference(set_a, set_b):
    if not isinstance(set_a, list) or not isinstance(set_b, list):
        return None

    result = []

    for x in set_a:
        if x not in set_b and x not in result:
            result.append(x)

    for x in set_b:
        if x not in set_a and x not in result:
            result.append(x)
    return result


def is_subset(sub, super_set):
    if not isinstance(sub, list) or not isinstance(super_set, list):
        return False

    for x in sub:
        if x not in super_set:
            return False
    return True


def power_set(s):
    if not isinstance(s, list):
        return None

    n = len(s)
    power_set_size = 2**n
    result = []

    for i in range(power_set_size):
        subset = []
        for j in range(n):
            if (i & (1 << j)) > 0:
                subset.append(s[j])
        result.append(subset)
    return result


def cartesian_product(set_a, set_b):
    if not isinstance(set_a, list) or not isinstance(set_b, list):
        return None

    result = []
    for x in set_a:
        for y in set_b:
            result.append((x, y))
    return result


def jaccard_similarity(set_a, set_b):
    union = set_union(set_a, set_b)
    intersection = set_intersection(set_a, set_b)

    if not union:
        return 0.0 if not intersection else 1.0

    return len(intersection) / len(union)
