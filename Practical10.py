# Practical 10: Recursions and Backtracking Algorithms (Simplified Version)

# ==================== PART 1: Factorial ====================

def factorial(n):
    if n == 1:  # Base case: factorial of 1 is 1
        return 1
    else:
        return n * factorial(n-1)  # Recursive case: n! = n * (n-1)!
# Test
print("Factorial of 5:", factorial(5))  # 120

# ==================== PART 2: Fibonacci ====================

# 1. Recursive Fibonacci
def fib_recursive(n):
    if n <= 1:  # Base cases: F(0)=0, F(1)=1
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)  # Recursive relation: F(n) = F(n-1) + F(n-2)

# 2. Iterative Fibonacci
def fib_iterative(n):
    if n <= 1:  # Handle base cases
        return n
    a, b = 0, 1  # Initialize first two Fibonacci numbers
    for _ in range(2, n+1):  # Iterate from 2 to n
        a, b = b, a + b  # Update values: a becomes b, b becomes a+b
    return b  # After loop, b contains F(n)

# 3. Memoized Fibonacci
fib_memo = {0:0, 1:1}  # Pre-filled base cases
fib_memo = {0:0, 1:1}  # Dictionary to store computed results
def fib_memoized(n):
    if n not in fib_memo:  # If not already computed
        fib_memo[n] = fib_memoized(n-1) + fib_memoized(n-2)  # Compute and store
    return fib_memo[n]  # Return cached result

# Test Fibonacci
print("\nFibonacci numbers (n=0 to 9):")
for i in range(10):
    print(f"Recursive:{fib_recursive(i)}", 
          f"Iterative:{fib_iterative(i)}", 
          f"Memoized:{fib_memoized(i)}")

# ==================== PART 3: Climbing Stairs ====================

def climb_stairs(n):
    if n <= 2:  # Base cases: 1 way for 1 step, 2 ways for 2 steps
        return n
    dp = [0]*(n+1)  # DP array to store number of ways for each step count
    dp[1], dp[2] = 1, 2  # Initialize base cases
    for i in range(3, n+1):  # Build up solution from 3 to n
        dp[i] = dp[i-1] + dp[i-2]  # Ways to reach i = ways to i-1 + ways to i-2
    return dp[n]  # Final answer

# Test
print("\nClimbing stairs ways:")
for i in range(1, 10):
    print(f"{i} stairs: {climb_stairs(i)} ways")

# ==================== PART 4: Tower of Hanoi ====================

def hanoi(n, source, target, auxiliary):
    if n == 1:  # Base case: move single disk directly to target
        print(f"Move disk 1 from {source} to {target}")
        return
    # Move n-1 disks from source to auxiliary (using target as temp)
    hanoi(n-1, source, auxiliary, target)
    # Move remaining largest disk to target
    print(f"Move disk {n} from {source} to {target}")
    # Move n-1 disks from auxiliary to target (using source as temp)
    hanoi(n-1, auxiliary, target, source)

# Test
print("\nTower of Hanoi (3 disks):")
hanoi(3, 'A', 'C', 'B')

# ==================== PART 5: Combination Sum ====================

def combination_sum(candidates, target):
    result = []  # Will store all valid combinations
    
    def backtrack(start, current_sum, path):
        if current_sum == target:  # Found valid combination
            result.append(path.copy())  # Add copy to result
            return
        if current_sum > target:  # Prune invalid paths
            return
        for i in range(start, len(candidates)):  # Try each candidate
            path.append(candidates[i])  # Choose current candidate
            # Explore further with current candidate (allow reuse)
            backtrack(i, current_sum + candidates[i], path)
            path.pop()  # Backtrack: remove last choice
    
    candidates.sort()  # Sort to enable pruning of larger numbers
    backtrack(0, 0, [])  # Start with empty path
    return result

# Test
print("\nCombination sum for target 7:")
print(combination_sum([2,3,6,7], 7))

# ==================== PART 6: Word Search ====================

def word_search(board, word):
    rows, cols = len(board), len(board[0])  # Get board dimensions
    
    def dfs(r, c, index):
        # Base case: all characters matched
        if index == len(word):
            return True
        # Check boundaries and character match
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
            return False
        # Mark current cell as visited (temporarily)
        temp = board[r][c]
        board[r][c] = '#'
        # Explore all 4 directions (down, up, right, left)
        found = (dfs(r+1, c, index+1) or dfs(r-1, c, index+1) or
                 dfs(r, c+1, index+1) or dfs(r, c-1, index+1))
        # Backtrack: restore original value
        board[r][c] = temp
        return found
    
    # Try starting DFS from every cell
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):  # Start with first character
                return True
    return False  # Word not found

# Test
board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
print("\nWord search for 'ABCCED':", word_search(board, "ABCCED"))

# ==================== PART 7: Permutations ====================

def permutations(nums):
    result = []  # Will store all permutations
    
    def backtrack(first):
        if first == len(nums):  # Complete permutation generated
            result.append(nums.copy())  # Add copy to result
            return
        for i in range(first, len(nums)):  # Try each remaining number
            # Swap current element with first position
            nums[first], nums[i] = nums[i], nums[first]
            # Generate all permutations for next position
            backtrack(first + 1)
            # Backtrack: undo the swap
            nums[first], nums[i] = nums[i], nums[first]
    
    backtrack(0)  # Start with first position
    return result

# Test
print("\nPermutations of [1,2,3]:")
print(permutations([1,2,3]))