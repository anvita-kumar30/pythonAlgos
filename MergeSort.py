def merge_sort(list):
    """
    Sorts a linked list in ascending order
    Returns a new sorted linked list

    Divide: Find the midpoint of the list adn divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Takes O(nlog(n)) time
    Takes O(n) space
    """
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right

    Takes O(log n) time
    """
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    """
    Merges two linked lists, sorting by data in nodes
    Returns a new merged list
    Takes O(n) space
    Runs in O(n) time
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l

def verify_sorted(list):
    n = len(list)
    

alist = [54, 62, 93, 17, 77, 31, 44, 55, 20]
l = merge_sort(alist)
print(l)

    # # Create a new linked list that contains nodes from merging left and right
    # merged = LinkedList()
    # # Add a fake head that is discarded later.
    # merged.add(0)
    # # Set current to the head of the linked list
    # current = merged.head
    #
    # # Obtain head nodes for left and right linked lists
    # left_head = left.head
    # right_head = right.head
    #
    # # Iterate over left and right as long until the tail node of both
    # # left and right
    # while left_head or right_head:
    #     # If the head node of left is None, we're at the tail
    #     # Add the tail node from right to the merged linked list
    #     if left_head is None:
    #         current.next_node = right_head
    #         # Call next on right to set loop condition to False
    #         right_head = right_head.next_node
    #     # If the head node of right is None, we're at the tail
    #     # Add the tail node from left to the merged linked list
    #     elif right_head is None:
    #         current.next_node = left_head
    #         # Call next on left to set loop condition to False
    #         left_head = left_head.next_node
    #     else:
    #         # Not at either tail node
    #         # Obtain node data to perform comparison operations
    #         left_data = left_head.data
    #         right_data = right_head.data
    #
    #         # If data on left is lesser than right set current to left node
    #         # Move left head to next node
    #         if left_data < right_data:
    #             current.next_node = left_head
    #             left_head = left_head.next_node
    #         # If data on left is greater than right set current to right node
    #         # Move right head to next node
    #         else:
    #             current.next_node = right_head
    #             right_head = right_head.next_node
    #
    #     # Move current to next node
    #     current = current.next_node
    #
    # # Discard fake head and set first merged node as head
    # head = merged.head.next_node
    # merged.head = head
    #
    # return merged