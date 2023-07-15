# class review: https://replit.com/@AdamOwada/Linked-List-Review#


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LL:
    def __init__(self, head=None):
        self.head = head

    def print_ll(self):
        # step 1: define a current pointer
        current = self.head  # initially points to head on entry into the method
        # step 2: use a while lool for traversal
        while current:  # while current is truthy
            # step 3: "do the thing"
            print(current.value)
            # step 4: move the pointer
            current = current.next  # reassign current to the next node in the linked list, eventually current.next = Falsey, which breaks the while loop


if __name__ == "__main__":
    ll_1 = LL(Node(1))
    ll_1.head.next = Node(2)
    ll_1.head.next.next = Node(3)

    print(ll_1.head.val)  # prints value of node 1
    print(ll_1.head.next)  # prints memory address of node 2
    print(ll_1.head.next.value)  # prints value of node 2
    print(ll_1.head.next.next)  # prints memory address of node 3
    print(ll_1.head.next.next.next)  # prints None -node 3's .next doesn’t have a value

    ll_1.print_ll()
