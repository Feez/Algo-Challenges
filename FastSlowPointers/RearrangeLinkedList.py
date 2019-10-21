# MPalindrome LinkedList (medium)
# https://www.educative.io/courses/grokking-the-coding-interview/B1PzmqOKDLQ
#
# Given the head of a Singly LinkedList, write a method to check 
# if the LinkedList is a palindrome or not.
#
# Your algorithm should use constant space and the input LinkedList should be 
# in the original form once the algorithm is finished. 
# The algorithm should have O(N) time complexity where ‘N’ is the number of 
# nodes in the LinkedList.


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"Node({self.value})"

    def traverse(self, visited=None):
        if visited is None:
            visited = set()
        visited.add(self)

        add_str = ""
        if self.next:
            add_str = f"->{self.next.traverse(visited)}"

        return str(self) + add_str

    def get_middle(self):
        slow = self
        fast = self

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse(self):
        prev = None
        curr = self

        while curr:
            next = curr.next

            curr.next = prev
            prev = curr

            curr = next

        return prev

    def is_palindrome(self):
        middle = self.get_middle()

        second_half = middle.reverse()

        start1 = self
        start2 = second_half

        while start1 != middle:
            if start1.value != start2.value:
                second_half.reverse()
                return False

            start1 = start1.next
            start2 = start2.next

        second_half.reverse()

        return True


    def reorder(self):
        head = self
        middle = self.get_middle()
        second_half = middle.reverse()

        curr = head
        while curr != middle:
            curr_next = curr.next
            second_half_next = second_half.next

            curr.next = second_half
            second_half.next = curr_next

            curr = curr_next
            second_half = second_half_next

        middle.next = None


def build_node_list(count):
    head = Node(0)
    curr = head

    for i in range(1, count):
        curr.next = Node(i)
        curr = curr.next

    return head

def build_palindrome(count):
    head = Node(0)
    curr = head

    for i in range(1, count // 2):
        curr.next = Node(i)
        curr = curr.next

    for i in reversed(range(count // 2 - 1)):
        curr.next = Node(i)
        curr = curr.next

    return head


        
head = build_node_list(10)
print("Normal: ", head.traverse())
head.reorder()
print("Reorder: ", head.traverse())
