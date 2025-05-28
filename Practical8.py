# class Stack:
#     def __init__(self):
#         self.items = []

#     def is_empty(self):
#         return len(self.items) == 0

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             raise IndexError("Stack is empty")

#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             raise IndexError("Stack is empty")

#     def size(self):
#         return len(self.items)

# # Test the Stack
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.pop())  # Should print 3
# print(stack.peek())  # Should print 2
# print(stack.size())  # Should print 2

# Part 1: Implementing a Stack
class Stack:
    def __init__(self):
        # Initialize an empty list to store stack items
        self.items = []

    def is_empty(self):
        # Check if stack is empty by checking list length
        return len(self.items) == 0

    def push(self, item):
        # Add item to the end of the list (top of stack)
        # list.append() adds item to end of list in O(1) time
        self.items.append(item)

    def pop(self):
        # Remove and return the last item (top of stack)
        # list.pop() without index removes last item in O(1) time
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        # Return the last item without removing it
        # list[-1] accesses last element in O(1) time
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        # Return number of items in stack
        # len() returns list length in O(1) time
        return len(self.items)

# Test Stack implementation
def test_stack():
    s = Stack()
    print("Testing Stack:")
    print("Is empty?", s.is_empty())  # True
    s.push(1)
    s.push(2)
    s.push(3)
    print("Size:", s.size())  # 3
    print("Peek:", s.peek())  # 3
    print("Pop:", s.pop())  # 3
    print("Pop:", s.pop())  # 2
    print("Size:", s.size())  # 1
    print("Is empty?", s.is_empty())  # False
    print("Peek:", s.peek())  # 1
    print("Pop:", s.pop())  # 1
    print("Is empty?", s.is_empty())  # True
    try:
        s.pop()
    except IndexError as e:
        print("Error:", e)  # Should print "Stack is empty"

test_stack()


# Part 2: Implementing a Queue
class Queue:
    def __init__(self):
        # Initialize an empty list to store queue items
        self.items = []

    def is_empty(self):
        # Check if queue is empty by checking list length
        return len(self.items) == 0

    def enqueue(self, item):
        # Add item to the end of the queue
        # list.append() adds to end in O(1) time
        self.items.append(item)

    def dequeue(self):
        # Remove and return first item (front of queue)
        # list.pop(0) removes first item in O(n) time
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        # Return first item without removing it
        # list[0] accesses first element in O(1) time
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        # Return number of items in queue
        return len(self.items)

# Test Queue implementation
def test_queue():
    q = Queue()
    print("\nTesting Queue:")
    print("Is empty?", q.is_empty())  # True
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Size:", q.size())  # 3
    print("Front:", q.front())  # 1
    print("Dequeue:", q.dequeue())  # 1
    print("Dequeue:", q.dequeue())  # 2
    print("Size:", q.size())  # 1
    print("Is empty?", q.is_empty())  # False
    print("Front:", q.front())  # 3
    print("Dequeue:", q.dequeue())  # 3
    print("Is empty?", q.is_empty())  # True
    try:
        q.dequeue()
    except IndexError as e:
        print("Error:", e)  # Should print "Queue is empty"

test_queue()


# Part 3: Implementing Stack using Queues
from queue import Queue  # Import Python's built-in Queue class

class MyStack:
    def __init__(self):
        # Initialize two queues
        # Queue() creates a FIFO queue
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        # Add new element to q2
        # Queue.put() adds item to the end of queue
        self.q2.put(x)
        # Move all elements from q1 to q2
        while not self.q1.empty():
            # Queue.get() removes and returns front item
            self.q2.put(self.q1.get())
        # Swap q1 and q2 so q1 always has stack order
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        # Remove and return top element from q1
        return self.q1.get()

    def top(self) -> int:
        # Return top element without removing
        # Queue.queue[0] accesses front element (not standard queue operation)
        return self.q1.queue[0]

    def empty(self) -> bool:
        # Check if stack is empty
        # Queue.empty() returns True if queue is empty
        return self.q1.empty()

# Test MyStack implementation
def test_mystack():
    stack = MyStack()
    print("\nTesting MyStack:")
    print("Is empty?", stack.empty())  # True
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Top:", stack.top())  # 3
    print("Pop:", stack.pop())  # 3
    print("Pop:", stack.pop())  # 2
    print("Is empty?", stack.empty())  # False
    print("Top:", stack.top())  # 1
    print("Pop:", stack.pop())  # 1
    print("Is empty?", stack.empty())  # True

test_mystack()


# Part 4: Reverse a String using Stack
def reverse_string(s):
    stack = Stack()
    # Push all characters onto stack
    for char in s:
        stack.push(char)
    
    reversed_string = ""
    # Pop all characters to build reversed string
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

# Test reverse_string
print("\nTesting reverse_string:")
print(reverse_string("Hello"))  # "olleH"
print(reverse_string("12345"))  # "54321"
print(reverse_string(""))  # ""


# Part 2: Implementing a Queue (corrected)
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):  # This is the correct method name
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

# Part 5: Hot Potato Simulation using Queue (corrected)
def hot_potato(names, num):
    q = Queue()  # Changed variable name to 'q' to avoid confusion
    # Enqueue all names
    for name in names:
        q.enqueue(name)  # Using the Queue instance 'q', not the method name
    
    while q.size() > 1:
        # Pass the potato num times
        for _ in range(num):
            # Move person from front to back
            q.enqueue(q.dequeue())
        # Person at front is eliminated
        q.dequeue()
    
    # Last remaining person is winner
    return q.dequeue()

# Test hot_potato
print("\nTesting hot_potato:")
names = ["Pharsa", "Nana", "Johnson", "Angela", "Estes"]
print(hot_potato(names, 3))  # Output will vary based on num
print(hot_potato(names, 1))  # Different winner

# Part 6: Balanced Parentheses using Stack
def is_balanced(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty():
                return False  # Unmatched closing parenthesis
            stack.pop()
    # If stack is empty, all parentheses matched
    return stack.is_empty()

# Test is_balanced
print("\nTesting is_balanced:")
print(is_balanced("(())"))  # True
print(is_balanced("(()"))  # False
print(is_balanced(")("))  # False
print(is_balanced(""))  # True


# Part 7: Valid Parentheses (Leetcode problem)
def isValid(s: str) -> bool:
    stack = []
    # Mapping of closing to opening brackets
    bracket_map = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in bracket_map:  # Closing bracket
            # Check if stack is empty or top doesn't match
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()  # Remove matching opening bracket
        else:  # Opening bracket
            stack.append(char)  # Add to stack
    
    # If stack is empty, all brackets matched
    return len(stack) == 0

# Test isValid
print("\nTesting isValid:")
print(isValid("()[]{}"))  # True
print(isValid("([{}])"))  # True
print(isValid("(]"))  # False
print(isValid("([)]"))  # False
print(isValid("{"))  # False