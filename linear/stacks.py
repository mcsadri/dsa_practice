class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        pass

    def pop(self):
        pass


if __name__ == "__main__":
    stack_1 = Stack(Node(1))
    stack_1.top.next = Node(2)
stack_1.top.next.next = Node(3)