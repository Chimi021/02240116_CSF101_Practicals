def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        # n-i-1 because after each pass, largest element bubbles to the end
        # -1 because we compare j and j+1 (avoid index out of range)
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # Early exit if already sorted
            break
    return arr

def merge_sort(arr):
    if len(arr) <= 1:  # Base case: single element is already sorted
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # Recursively sort left half
    right = merge_sort(arr[mid:]) # Recursively sort right half
    
    return merge(left, right)  # Merge the two sorted halves

def merge(left, right):
    result = []
    i = j = 0
    
    # Compare elements from both halves and add smaller one to result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add any remaining elements (one half may be longer)
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_idx = partition(arr, low, high)  # Partition the array
        quick_sort(arr, low, pivot_idx - 1)    # Sort left of pivot
        quick_sort(arr, pivot_idx + 1, high)   # Sort right of pivot
    
    return arr

def partition(arr, low, high):
    pivot = arr[high]  # Choosing last element as pivot
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap if element <= pivot
    
    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return pivot index

# Testing
test_arr = [64, 34, 25, 12, 22, 11, 90]
print("Original:", test_arr)
print("Bubble:", bubble_sort(test_arr.copy()))
print("Merge:", merge_sort(test_arr.copy()))
print("Quick:", quick_sort(test_arr.copy()))