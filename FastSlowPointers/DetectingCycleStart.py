# Start of LinkedList Cycle (medium)
# https://www.educative.io/courses/grokking-the-coding-interview/N7pvEn86YrN
#
# Given the head of a Singly LinkedList that contains a cycle, write a
# function to find the starting node of the cycle.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_cycle_length(slow):
    count = 1
    curr = slow

    while curr.next != slow:
        curr = curr.next
        count += 1

    return count


def find_node_in_cycle(head):
    slow = head
    fast = head

    found_node = None

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return slow

# !Extra loops solution
def find_cycle_start_worse(head):
    cycle_length = find_cycle_length(find_node_in_cycle(head))

    start1 = head
    start2 = head

    for i in range(cycle_length):
        start2 = start2.next

    while start1 != start2:
        start1 = start1.next
        start2 = start2.next

    return start1

# * No extra loops solution
def find_cycle_start(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            start = head
            start2 = slow

            while start != start2:
                start = start.next
                start2 = start2.next

            return start


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
