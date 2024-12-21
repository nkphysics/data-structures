class DoublyLinkedList:
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

    def prepend(self, data):
        # O(1) constant time
        item = self._head
        if item is None:
            self._head = self.Node(data)
            self._tail = self._head
        else:
            new_node = self.Node(data)
            new_node.next = self._head
            self._head.previous = new_node
            self._head = new_node
        self._size += 1

    def append(self, data):
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

    def delete_front(self):
        # O(1) constant time
        current = self._head
        second = current.next
        self._head = second
        self._head.previous = None
        del current
        self._size -= 1

    def delete_end(self):
        # O(1) constant time
        item = self._tail
        second_last = item.previous
        self._tail = second_last
        self._tail.next = None
        del item
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

    def get_data(self, index: int):
        # O(n) linear time
        max_index = self._size - 1
        midpoint = max_index / 2
        ldiff = max_index - index
        if ldiff >= midpoint:
            item = self._head
            for i in range(self._size):
                if i == index:
                    return item.data
                else:
                    if item.next is None:
                        raise IndexError("Index out of bounds")
                    else:
                        item = item.next
        else:
            item = self._tail
            for i in reversed(range(self._size)):
                if i == index:
                    return item.data
                else:
                    if item.previous is None:
                        raise IndexError("Index out of bounds")
                    else:
                        item = item.previous

    def delete(self, data):
        # O(n) linear time
        item = self._head
        if self._head is None:
            raise IndexError("Linked list is empty")
        else:
            last = 0
            while item.data != data:
                if item.next is None:
                    raise ValueError(f"Item: {data} not found in linked list")
                else:
                    last = item
                    item = item.next
            last.next = item.next
            del item
            self._size -= 1

    def insert(self, data, index: int):
        # O(n) linear
        max_index = self._size - 1
        if index > max_index:
            self.append(data)
        elif index == 0 or max_index < 0:
            self.prepend(data)
        else:
            midpoint = max_index * 0.5
            if index <= midpoint:
                item = self._head
                for _ in range(index - 1):
                    item = item.next
                new = self.Node(data)
                new.next = item.next
                new.previous = item
                item.next = new
                self._size += 1
            else:
                item = self._tail
                for _ in range(self._size - index):
                    item = item.previous
                new = self.Node(data)
                new.next = item.next
                new.previous = item
                item.next = new
                self._size += 1

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
    ll = DoublyLinkedList()
    ll.prepend("apple")
    ll.prepend("orange")
    ll.prepend("strawberry")
    ll.prepend("bannana")
    ll.prepend("pear")
    ll.prepend("raspberry")
    ll.display()
    ll.delete_front()
    ll.display()
    ll.append("raspberry")
    ll.append("blackberry")
    ll.append("blueberry")
    ll.display()
    ll.delete_end()
    ll.display()
    print(ll.get_index("strawberry"))
    print(ll.get_index("blackberry", "end"))
    print(ll.get_data(2))
    print(ll.get_data(6))
    ll.delete("strawberry")
    ll.display()
    ll.insert("lemon", 0)
    ll.insert("mango", 1)
    ll.insert("strawberry", 6)
    ll.insert("gooseberry", 100)
    ll.display()
    # # ll.insert("blackberry", 10)
