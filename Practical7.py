# ===== 1. Contains Duplicate =====
def contains_duplicate(nums):
    """
    Checks if any value appears at least twice in the array.
    
    Args:
        nums: List of integers to check
        
    Returns:
        bool: True if duplicates exist, False otherwise
        
    Built-in functions used:
        set(): Converts list to set (removes duplicates)
        len(): Returns length of sequence
    """
    # Compare length of original list vs set (sets remove duplicates)
    return len(nums) != len(set(nums))  

# Test cases
print("Contains Duplicate:")
print(contains_duplicate([1,2,3,1]))  # True
print(contains_duplicate([1,2,3,4]))  # False
print()


# ===== 2. Valid Anagram =====
def is_anagram(s, t):
    """
    Checks if two strings are anagrams (contain same characters in same counts).
    
    Args:
        s: First string
        t: Second string
        
    Returns:
        bool: True if anagrams, False otherwise
        
    Built-in functions used:
        ord(): Gets ASCII value of character
        all(): Returns True if all elements in iterable are True
    """
    if len(s) != len(t):
        return False
    
    # Initialize count array for 26 letters (a-z)
    count = [0] * 26  
    
    for i in range(len(s)):
        # Increment count for s's character, decrement for t's
        # ord('a') is 97, so ord(char)-97 gives 0-25 index
        count[ord(s[i]) - ord('a')] += 1  
        count[ord(t[i]) - ord('a')] -= 1
    
    # Check all counts are zero (using generator expression)
    return all(c == 0 for c in count)  

print("Valid Anagram:")
print(is_anagram("anagram", "nagaram"))  # True
print(is_anagram("rat", "car"))         # False
print()


# ===== 3. Two Sum =====
def two_sum(nums, target):
    """
    Finds indices of two numbers that add up to target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List[int]: Indices of the two numbers
        
    Built-in functions used:
        enumerate(): Returns index and value from iterable
    """
    num_map = {}  # Stores {number: index} pairs
    
    for i, num in enumerate(nums):  # Get both index and value
        complement = target - num
        if complement in num_map:  # O(1) lookup
            return [num_map[complement], i]
        num_map[num] = i  # Store current number's index
    
    return []  # Problem states solution exists

print("Two Sum:")
print(two_sum([2,7,11,15], 9))  # [0,1]
print(two_sum([3,2,4], 6))     # [1,2]
print()


# ===== 4. Valid Palindrome =====
def is_palindrome(s):
    """
    Checks if string is palindrome after removing non-alphanumeric chars.
    
    Args:
        s: Input string
        
    Returns:
        bool: True if palindrome, False otherwise
        
    Built-in functions used:
        isalnum(): Checks if character is alphanumeric
        lower(): Converts character to lowercase
    """
    left, right = 0, len(s) - 1  # Initialize two pointers
    
    while left < right:
        # Skip non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        # Move pointers inward
        left += 1
        right -= 1
    
    return True

print("Valid Palindrome:")
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))                     # False
print()


# ===== 5. Three Sum =====
def three_sum(nums):
    """
    Finds all unique triplets that sum to zero.
    
    Args:
        nums: List of integers
        
    Returns:
        List[List[int]]: List of valid triplets
        
    Built-in functions used:
        sort(): Sorts list in-place
        append(): Adds item to list
    """
    nums.sort()  # Sort to enable two-pointer approach
    result = []
    
    for i in range(len(nums)-2):
        # Skip duplicate values for first number
        if i > 0 and nums[i] == nums[i-1]:
            continue
            
        left, right = i+1, len(nums)-1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total < 0:
                left += 1  # Need larger sum
            elif total > 0:
                right -= 1  # Need smaller sum
            else:
                # Found valid triplet
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
    
    return result

print("Three Sum:")
print(three_sum([-1,0,1,2,-1,-4]))  # [[-1,-1,2],[-1,0,1]]
print(three_sum([0,1,1]))           # []
print()


# ===== 6. Best Time to Buy and Sell Stock =====
def max_profit(prices):
    """
    Calculates maximum profit from single buy/sell transaction.
    
    Args:
        prices: List of stock prices
        
    Returns:
        int: Maximum profit possible
        
    Built-in functions used:
        min(): Finds minimum value
        max(): Finds maximum value
    """
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices[1:]:
        # Track the minimum price seen so far
        min_price = min(min_price, price)
        # Calculate potential profit and update max
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

print("Max Profit:")
print(max_profit([7,1,5,3,6,4]))  # 5
print(max_profit([7,6,4,3,1]))    # 0
print()


# ===== 7. Longest Substring Without Repeating Characters =====
def length_of_longest_substring(s):
    """
    Finds length of longest substring without repeating characters.
    
    Args:
        s: Input string
        
    Returns:
        int: Length of longest substring
        
    Built-in functions used:
        set(): Collection of unique elements
        add(): Adds element to set
        remove(): Removes element from set
    """
    char_set = set()  # Track characters in current window
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # If duplicate found, move left pointer
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])# Add current character to set
        # Update max length if needed
        max_length = max(max_length, right - left + 1)
    
    return max_length

print("Longest Substring:")
print(length_of_longest_substring("abcabcbb"))  # 3
print(length_of_longest_substring("bbbbb"))     # 1