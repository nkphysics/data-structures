class CircularLinkedList:
    def __init__(self, head=None):
        self._head = head
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
        def __init__(self, data, nextnode=None):
            self.data = data
            self.next = nextnode

    def prepend(self, data):
        # O(1) linear time
        new_node = self.Node(data, self._head)
        self._head = new_node
        self._size += 1

    def append(self, data):
        # O(n) linear time
        first = self._head
        item = self._head
        if item is None:
            self._head = self.Node(data)
            self._head.next = self._head
        else:
            for _ in range(self._size - 1):
                item = item.next
            item.next = self.Node(data, first)
        self._size += 1

    def delete_front(self):
        # O(1) constant time
        current = self._head
        second = current.next
        self._head = second
        del current
        self._size -= 1

    def delete_end(self):
        # O(n) linear time
        item = self._head
        if item is None:
            raise IndexError("Linked list is empty")
        else:
            previous = 0
            for _ in range(self._size - 1):
                previous = item
                item = item.next
            previous.next = item.next
            del item
            self._size -= 1

    def get_index(self, data):
        # O(n) linear time
        if self._head is None:
            raise IndexError("Linked list is empty")
        else:
            item = self._head
            for i in range(self._size):
                if item.data == data:
                    return i
                else:
                    item = item.next
            raise ValueError(f"Item: {data} not found in linked list")

    def get_data(self, index: int):
        # O(n) linear time
        if index > (self._size - 1):
            raise IndexError("Index larger than size of linked list")
        else:
            item = self._head
            for i in range(self._size):
                if i == index:
                    return item.data
                else:
                    item = item.next

    def delete(self, data):
        # O(n) linear time
        if self._head is None:
            raise IndexError("Linked list is empty")
        else:
            last = None
            item = self._head
            for _ in range(self._size - 1):
                if item.data == data:
                    last.next = item.next
                    del item
                    self._size -= 1
                    return
                else:
                    last = item
                    item = item.next
            raise ValueError(f"Item: {data} not found in linked list")

    def insert(self, data, index):
        # O(n) linear
        max_index = self._size - 1
        if index > max_index:
            self.append(data)
        elif index == 0 or max_index < 0:
            self.prepend(data)
        else:
            item = self._head
            if item is None:
                raise IndexError("Linked List is empty, prepend to add data")
            for _ in range(index - 1):
                item = item.next
            new = self.Node(data, item.next)
            item.next = new
            self._size += 1

    def display(self):
        # O(n) linear time
        position = 0
        item = self._head
        for _ in range(self._size - 1):
            print(f"{position}: {item.data}")
            position += 1
            item = item.next
        print(f"{position}: {item.data}\n")


if __name__ == "__main__":
    ll = CircularLinkedList()
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
    print(ll.get_index("blackberry"))
    print(ll.get_data(2))
    print(ll.get_data(6))
    ll.delete("strawberry")
    ll.display()
    ll.insert("lemon", 0)
    ll.insert("mango", 1)
    ll.insert("strawberry", 6)
    ll.insert("gooseberry", 100)
    ll.display()
