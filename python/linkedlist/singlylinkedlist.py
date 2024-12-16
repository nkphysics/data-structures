class SinglyLinkedList:
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
        # O(1) constant time
        new_node = self.Node(data, self._head)
        self._head = new_node
        self._size += 1

    def append(self, data):
        # O(n) linear time
        item = self._head
        if item is None:
            self._head = Node(data)
        else:
            while item.next is not None:
                item = item.next
            item.next = self.Node(data)
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
            while item.next.next is not None:
                item = item.next
            del item.next
            item.next = None
            self._size -= 1

    def get_index(self, data):
        # O(n) linear time
        if self._head is None:
            raise IndexError("Linked list is empty")
        else:
            item = self._head
            index = 0
            while item.data != data:
                if item.next is None:
                    raise ValueError(f"Item: {data} not found in linked list")
                else:
                    item = item.next
                    index += 1
            return index
    
    def get_data(self, index: int):
        # O(n) linear time
        item = self._head
        for i in range(self._size):
            if i == index:
                return item.data
            else:
                if item.next is None:
                    raise IndexError("Index out of bounds")
                else:
                    item = item.next

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

    def insert(self, data, index):
        # O(n) linear
        item = self._head
        if item is None:
            raise IndexError("Linked List is empty, prepend to add data")
        for i in range(index - 1):
            if item.next is None:
                raise IndexError("Index out of bounds")
            else:
                item = item.next
        new = self.Node(data, item.next)
        item.next = new

            
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
    ll = SinglyLinkedList()
    # ll.insert("gooseberry", 2)
    ll.prepend("apple")
    ll.append("orange")
    ll.prepend("strawberry")
    ll.prepend("bannana")
    ll.prepend("pear")
    ll.prepend("raspberry")
    print("apple" in ll)
    print("grapes" in ll)
    ll.display()
    print(ll.get_index('strawberry'))
    # print(ll.get_index('grapes'))
    print(ll.get_data(5))
    ll.delete_front()
    ll.display()
    ll.delete_end()
    ll.display()
    ll.delete("strawberry")
    ll.display()
    ll.insert("blueberry", 1)
    ll.display()
    # ll.insert("blackberry", 10)

