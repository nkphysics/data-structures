class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        # O(1) constant time
        return self._size

    def __contains__(self, data):
        # O(n) linear time
        state = False
        item = self._head
        while state is False and item.next is not None:
            if item.data == data:
                state = True
            else:
                item = item.next
        return state

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.previous = None

    def push(self, data):
        # O(1) constant time
        item = self._head
        if item is None:
            self._head = self.Node(data)
            self._tail = self._head
        else:
            new_node = self.Node(data)
            new_node.previous = self._tail
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def pop(self):
        # O(1) constant time
        current = self._head
        second = current.next
        self._head = second
        self._head.previous = None
        del current
        self._size -= 1

    def get_index(self, data, start="front"):
        # O(n) linear time
        if self._head is None:
            raise IndexError("Linked list is empty")
        else:
            if start == "front":
                item = self._head
                index = 0
                while item.data != data:
                    if item.next is None:
                        raise ValueError(f"Item: {data} not found")
                    else:
                        item = item.next
                        index += 1
            elif start == "end":
                item = self._tail
                index = self._size - 1
                while item.data != data:
                    if item.previous is None:
                        raise ValueError(f"Item: {data} not found")
                    else:
                        item = item.previous
                        index -= 1
            else:
                raise ValueError("Start point not recognized")
            return index

    def peek(self):
        # O(1) linear time
        item = self._head
        return item.data

    def display(self):
        # O(n) linear time
        position = 0
        item = self._head
        while item.next is not None:
            print(f"{position}: {item.data}")
            position += 1
            item = item.next
        print(f"{position}: {item.data}\n")


if __name__ == "__main__":
    ll = Queue()
    ll.push("apple")
    print(len(ll))
    ll.push("orange")
    ll.push("strawberry")
    ll.push("bannana")
    ll.push("pear")
    ll.push("raspberry")
    ll.display()
    ll.pop()
    ll.display()
    print(ll.peek())
    print(ll.get_index("pear"))
