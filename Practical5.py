#Practical 5
# Linear Search Implementation
def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Target found
    return -1  # Target not found

# Binary Search Implementation (Iterative)
def binary_search(arr, target):
    """Searches sorted list using divide-and-conquer approach"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Find middle index
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    
    return -1  # Target not found

# Binary Search Implementation (Recursive)
def binary_search_recursive(arr, target, left, right):
    """Recursive version of binary search"""
    if left > right:
        return -1  # Base case: not found
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid  # Target found
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid+1, right)  # Search right
    else:
        return binary_search_recursive(arr, target, left, mid-1)  # Search left

# Performance Comparison Function
def compare_search_performance(arr, target):
    """Compares execution time of both search methods"""
    import time
    
    # Time linear search
    start = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start
    
    # Time binary search (requires sorted list)
    sorted_arr = sorted(arr)
    start = time.time()
    binary_result = binary_search(sorted_arr, target)
    binary_time = time.time() - start
    
    print(f"Linear Search: Result {linear_result}, Time {linear_time:.6f}s")
    print(f"Binary Search: Result {binary_result}, Time {binary_time:.6f}s")

# Main Demonstration Function
def main():
    """Demonstrates all search implementations"""
    import random
    test_data = [random.randint(1, 100) for _ in range(20)]
    target = random.choice(test_data)
    
    print(f"Sample Data: {test_data}")
    print(f"Sorted Data: {sorted(test_data)}")
    print(f"\nSearching for: {target}\n")
    
    # Run all search variants
    print(f"Linear Search: {linear_search(test_data, target)}")
    sorted_data = sorted(test_data)
    print(f"Binary Search (Iterative): {binary_search(sorted_data, target)}")
    print(f"Binary Search (Recursive): {binary_search_recursive(sorted_data, target, 0, len(sorted_data)-1)}")
    
    # Performance test
    print("\nPerformance Test (100,000 elements):")
    large_data = list(range(100000))
    compare_search_performance(large_data, 99999)

if __name__ == "__main__":
    main()



print ("..........................................................................................")
# Exercise 1: Modified linear search to find all occurrences
def linear_search_all(arr, target):
    """Returns all indices where target appears"""
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices if indices else -1

# Exercise 2: Binary search for insertion point
def find_insert_position(sorted_arr, target):
    """Finds where target should be inserted to maintain order"""
    left, right = 0, len(sorted_arr)
    while left < right:
        mid = (left + right) // 2
        if sorted_arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

# Exercise 3: Search with comparison counting
class SearchWithCounter:
    """Wrapper that counts comparisons during search"""
    def __init__(self):
        self.comparisons = 0
    
    def linear_search(self, arr, target):
        self.comparisons = 0
        for i in range(len(arr)):
            self.comparisons += 1
            if arr[i] == target:
                return i
        return -1
    
    def binary_search(self, arr, target):
        self.comparisons = 0
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left + right) // 2
            self.comparisons += 1
            if arr[mid] == target:
                return mid
            self.comparisons += 1
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1