def count_comparisons_linear_search(arr, target):
    """
    arr:    a list of numbers
    target: the value being searched for

    Returns:
        (found, comparisons): found is True if target is in arr, False
        otherwise. comparisons is the number of element-to-target
        comparisons actually performed (stop as soon as a match is
        found -- don't keep scanning).
    """
    # TODO: Implement a left-to-right linear scan, counting comparisons.
    found = False
    comparisons = 0
    for i in range(0, len(arr)):
        comparisons += 1
        if target==arr[i]:
            found = True
            return (found, comparisons)
    return (found, comparisons)


def count_comparisons_binary_search(sorted_arr, target):
    """
    sorted_arr: a list of numbers, already sorted ascending
    target:     the value being searched for

    Returns:
        (found, comparisons): same shape as count_comparisons_linear_search,
        but using binary search -- each comparison must actually halve
        the remaining search space.
    """
    # TODO: Implement binary search from Theory, counting one
    # comparison per midpoint check.
    # Base Case: If the search space is empty, the target isn't here
    if not sorted_arr:
        return (False, 0)
        
    mid = len(sorted_arr) // 2
    comparisons = 1  # We are about to make exactly one midpoint check
    
    # 1. Target found
    if sorted_arr[mid] == target:
        return (True, comparisons)
        
    # 2. Target is in the right half
    elif target > sorted_arr[mid]:
        # Slice from mid + 1 to the end
        found, sub_comparisons = count_comparisons_binary_search(sorted_arr[mid + 1:], target)
        return (found, comparisons + sub_comparisons)
        
    # 3. Target is in the left half
    else:
        # Slice from the start up to mid
        found, sub_comparisons = count_comparisons_binary_search(sorted_arr[:mid], target)
        return (found, comparisons + sub_comparisons)
