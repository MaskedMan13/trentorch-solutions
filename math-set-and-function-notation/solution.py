def is_subset(a, b):
    """
    a, b: Python sets

    Returns:
        True if every element of a is also in b (a is a subset of b,
        written a subseteq b), False otherwise.
    """
    # TODO: Implement using Python's own set operations.
    if a==a&b:
        return True
    else:
        return False


def argmax(values):
    """
    values: a non-empty list or tuple of numbers

    Returns:
        The INDEX of the largest value in values. If multiple values are
        tied for the maximum, return the first such index.
    """
    # TODO: Implement argmax from Theory: scan once, tracking the best
    # value and its index, updating only on a strictly larger value.
    max_index = 0
    max_value = values[max_index]
    for i in range(1, len(values)):
        if values[i]>max_value:
            max_value = values[i]
            max_index = i
    return max_index
