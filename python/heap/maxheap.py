class Maxheap:
    def __init__(self):
        self.elements = []

    def __len__(self) -> int:
        return len(self.elements)

    def _left_child_index(self, index):
        left = (index * 2) + 1
        return left if left < len(self.elements) else None

    def _right_child_index(self, index):
        right = (index * 2) + 2
        return right if right < len(self.elements) else None

    def _parent_index(self, index):
        return (index - 1) // 2 if index != 0 else None

    def _leaf_index(self):
        return len(self.elements) // 2

    def _priority_child_index(self, index):
        lchild = self._left_child_index(index)
        rchild = self._right_child_index(index)
        if lchild is not None and rchild is None:
            pass
        elif lchild is not None and rchild is not None:
            try:
                pchild = self.elements[lchild]
                if pchild[0] < self.elements[rchild][0]:
                    lchild = rchild
            except IndexError:
                pass
        return lchild

    def _bubble_up(self, index):
        # O(log(n)) time complexity
        item = self.elements[index]
        while index > 0:
            parent_index = self._parent_index(index)
            parent = self.elements[parent_index]
            if item[0] > parent[0]:
                self.elements[index] = parent
                index = parent_index
            else:
                break
        self.elements[index] = item

    def insert(self, item: tuple):
        # O(log(n)) time complexity (because of bubbling up)
        self.elements.append(item)
        self._bubble_up(len(self.elements) - 1)

    def _sift_down(self, index):
        # O(log(n)) time complexity
        item = self.elements[index]
        pindex = index
        while True:
            child_index = self._priority_child_index(pindex)
            if child_index is None:
                break
            if self.elements[pindex][0] < self.elements[child_index][0]:
                self.elements[pindex] = self.elements[child_index]
                pindex = child_index
            else:
                break
        self.elements[pindex] = item

    def pop_top(self):
        # O(log(n)) time complexity (because if sifting down)
        if len(self.elements) == 0:
            raise ValueError('Empty heap.')
        else:
            item = self.elements[0]
            self.elements[0] = self.elements.pop()
            self._sift_down(0)
        return item

    def peek(self):
        # O(1) constant time
        if len(self.elements) == 0:
            raise IndexError("Empty heap")
        return self.elements[0]

    def heapify(self, elements):
        # O(n) linear time complexity (at worst)
        self.elements = elements[:]
        last_leaf = self._leaf_index() - 1
        for index in range(last_leaf, -1, -1):
            self._sift_down(index)


if __name__ == "__main__":
    planets = ["mercury", "venus", "earth", "mars",
               "jupiter", "saturn", "uranus", "neptune"]
    heap = Maxheap()
    for i in enumerate(planets):
        heap.insert(i)
    print(heap.elements)
    heap.pop_top()
    print(heap.elements)
    heap.heapify(heap.elements)
    print(heap.elements)
    for i in heap.elements:
        heap.pop_top()
        heap.heapify(heap.elements)
        print(heap.elements)
