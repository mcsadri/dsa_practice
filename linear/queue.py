class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
        pass

    def dequeue(self):
        pass


if __name__ == "__main__":
    queue_1 = Queue()
    queue_1.front = Node(1)
    queue_1.front.next = Node(2)
    queue_1.front.next.next = Node(3)
    queue_1.back = queue_1.front.next.next
