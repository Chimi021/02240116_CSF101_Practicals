class Node:
    def __init__(self, data):
        self.data = data  # Stores the data/value of the node
        self.next = None  # Pointer to the next node (initially None)

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head pointer to None (empty list)
    
    def append(self, data):
        """Adds a new node with given data to the end of the list"""
        new_node = Node(data)  # Create new node with data
        if not self.head:  # If list is empty
            self.head = new_node  # Make new node the head
            return
        current = self.head  # Start at head
        while current.next:  # Traverse until last node
            current = current.next
        current.next = new_node  # Link last node to new node
    
    def display(self):
        """Prints the linked list in human-readable format"""
        elements = []  # Store node values
        current = self.head  # Start at head
        while current:  # While not at end of list
            elements.append(str(current.data))  # Add data to elements
            current = current.next  # Move to next node
        print(" -> ".join(elements))  # Print with arrows between values
    
    def insert(self, data, position):
        """Inserts a new node at specified position (0-based index)"""
        new_node = Node(data)  # Create new node
        if position == 0:  # Insert at head
            new_node.next = self.head  # New node points to current head
            self.head = new_node  # Update head to new node
            return
        current = self.head  # Start at head
        for _ in range(position - 1):  # Move to node before insertion point
            if current is None:  # If position exceeds list length
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next  # New node points to next node
        current.next = new_node  # Previous node points to new node
    
    def delete(self, data):
        """Removes first node with matching data value"""
        if not self.head:  # Empty list case
            return
        if self.head.data == data:  # If head needs deletion
            self.head = self.head.next  # Move head to next node
            return
        current = self.head  # Start at head
        while current.next:  # While not at last node
            if current.next.data == data:  # If next node matches
                current.next = current.next.next  # Skip the matching node
                return
            current = current.next  # Move to next node
    
    def search(self, data):
        """Returns position (index) of first node with matching data, or -1 if not found"""
        current = self.head  # Start at head
        position = 0  # Initialize counter
        while current:  # While not at end
            if current.data == data:  # If match found
                return position  # Return current position
            current = current.next  # Move to next node
            position += 1  # Increment counter
        return -1  # Return -1 if not found
    
    def reverse(self):
        """Reverses the linked list in place"""
        prev = None  # Previous node starts as None
        current = self.head  # Start at head
        while current:  # While not at end
            next_node = current.next  # Store next node temporarily
            current.next = prev  # Reverse the link direction
            prev = current  # Move prev forward
            current = next_node  # Move current forward
        self.head = prev  # Update head to last node (now first)

# Create and test linked list
ll = LinkedList()
ll.append(1)  # List: 1
ll.append(2)  # List: 1 -> 2
ll.append(3)  # List: 1 -> 2 -> 3
ll.display()  # Output: 1 -> 2 -> 3

ll.insert(4, 1)  # Insert 4 at position 1
ll.display()  # Output: 1 -> 4 -> 2 -> 3

ll.delete(2)  # Delete node with value 2
ll.display()  # Output: 1 -> 4 -> 3

print(ll.search(4))  # Output: 1 (position of 4)
print(ll.search(5))  # Output: -1 (not found)

ll.reverse()  # Reverse the list
ll.display()  # Output: 3 -> 4 -> 1


#REVERSE LINKED LIST
class ListNode:
    """LeetCode's standard ListNode definition"""
    def __init__(self, val=0, next=None):
        self.val = val  # Value of the node
        self.next = next  # Pointer to next node

def reverseList(head):
    """Reverses a linked list iteratively"""
    prev = None  # Previous node starts as None
    current = head  # Start at head
    
    while current:  # While current node exists
        next_temp = current.next  # Store next node temporarily
        current.next = prev  # Reverse the link direction
        prev = current  # Move prev forward
        current = next_temp  # Move current forward
    
    return prev  # Return new head (prev is now at original end)

# Test reverseList
# Create list: 1 -> 2 -> 3 -> 4 -> 5
# ####head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# This is exactly equivalent to the nested version above
node5 = ListNode(5)        # Last node with value 5, next=None by default
node4 = ListNode(4, node5) # Node4 points to node5
node3 = ListNode(3, node4) # Node3 points to node4
node2 = ListNode(2, node3) # Node2 points to node3
head = ListNode(1, node2)  # Head node points to node2
reversed_head = reverseList(head)
# While loop to print reversed list (5 -> 4 -> 3 -> 2 -> 1)
current = reversed_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

#MERGE 2 SORTED LIST
def mergeTwoLists(list1, list2):
    """Merges two sorted linked lists into one sorted list"""
    dummy = ListNode(0)  # Dummy node to simplify edge cases
    current = dummy  # Pointer to build the new list
    
    while list1 and list2:  # While both lists have nodes
        if list1.val <= list2.val:  # Choose smaller value
            current.next = list1  # Link to list1's node
            list1 = list1.next  # Move list1 forward
        else:
            current.next = list2  # Link to list2's node
            list2 = list2.next  # Move list2 forward
        current = current.next  # Move current forward
    
    # Attach remaining elements from either list
    if list1:
        current.next = list1
    if list2:
        current.next = list2
    
    return dummy.next  # Skip dummy node to return actual head

# Test mergeTwoLists
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
merged = mergeTwoLists(list1, list2)
# Print merged list: 1 -> 1 -> 2 -> 3 -> 4 -> 4
current = merged
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

#REMOVE Nth NODE FROM END LIST
def removeNthFromEnd(head, n):
    """Removes the nth node from the end of the list"""
    dummy = ListNode(0, head)  # Dummy node to handle edge cases
    fast = slow = dummy  # Initialize two pointers
    
    # Move fast pointer n nodes ahead
    for _ in range(n):
        fast = fast.next
    
    # Move both until fast reaches last node
    while fast.next:
        fast = fast.next
        slow = slow.next
    
    # Remove the nth node from end
    slow.next = slow.next.next
    
    return dummy.next  # Return head (skip dummy)

# Test removeNthFromEnd
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
new_head = removeNthFromEnd(head, 2)
# Print modified list: 1 -> 2 -> 3 -> 5 (4 was removed)
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")