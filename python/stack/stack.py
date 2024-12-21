class Stack:
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
        while state is False and item is not None:
            if item.data == data:
                state = True
            else:
                item = item.next
        return state

    class Node:
        def __init__(self, data, nextnode=None):
            self.data = data
            self.next = nextnode

    def push(self, data):
        # O(1) constant time
        new_node = self.Node(data, self._head)
        self._head = new_node
        self._size += 1

    def pop(self):
        # O(1) constant time
        current = self._head
        if current is None:
            raise IndexError("Stack is empty, nothing to pop out.")
        else:
            second = current.next
            self._head = second
            del current
            self._size -= 1

    def peek(self):
        # O(1) linear time
        item = self._head
        if item is None:
            raise IndexError("Stack is empty")
        else:
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
    ll = Stack()
    ll.push("mercury")
    ll.push("venus")
    ll.push("earth")
    ll.push("mars")
    ll.display()
    ll.pop()
    ll.display()
    print("mars" in ll)
    print("mercury" in ll)
    print(len(ll))
    planet = ll.peek()
    print(planet)
