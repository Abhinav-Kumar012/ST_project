import math

def linear_search(arr, target):
    """Performs linear search."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    """Performs iterative binary search on a sorted array."""
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_recursive(arr, target, low, high):
    """Performs recursive binary search on a sorted array."""
    if low > high:
        return -1
        
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

def jump_search(arr, target):
    """Performs jump search on a sorted array."""
    n = len(arr)
    step = math.sqrt(n)
    
    prev = 0
    while arr[int(min(step, n)-1)] < target:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1
            
    while arr[int(prev)] < target:
        prev += 1
        if prev == min(step, n):
            return -1
            
    if arr[int(prev)] == target:
        return int(prev)
        
    return -1

def exponential_search(arr, target):
    """Performs exponential search on a sorted array."""
    n = len(arr)
    if n == 0:
        return -1
        
    if arr[0] == target:
        return 0
        
    i = 1
    while i < n and arr[i] <= target:
        i = i * 2
        
    return binary_search_recursive(arr, target, i // 2, min(i, n - 1))

def interpolation_search(arr, target):
    """Performs interpolation search on a sorted array with uniformly distributed values."""
    low = 0
    high = len(arr) - 1
    
    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
            
        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (target - arr[low])))
        
        if arr[pos] == target:
            return pos
            
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
            
    return -1
