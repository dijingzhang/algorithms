class Heap:
    def __init__(self, heap = []):
        self.heap = heap

    def heapify(self):
        for i in range((len(self.heap) + 1) // 2 - 1, -1, -1):
            self.max_heapify_top(i)

    def max_heapify_top(self, i):
        """
        from top to down
        O(logn)
        """
        left = i * 2 + 1
        right = i * 2 + 2
        if left < len(self.heap) and self.heap[left] > self.heap[i]:
            largest = left
        else:
            largest = i

        if right < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[largest], self.heap[i] = self.heap[i], self.heap[largest]
            self.max_heapify_top(largest)

    def max_heapify_button(self, i):
        """
        from button to up
        O(logn)
        """
        parent = (i + 1) // 2 - 1
        if parent >= 0 and self.heap[parent] < self.heap[i]:
            smallest = parent
        else:
            smallest = i
        if smallest != i:
            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
            self.max_heapify_button(smallest)

    def pop(self):
        """
        O(logn)
        """
        self.heap[0], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[0]
        value = self.heap.pop()
        self.max_heapify_top(0)
        return value

    def push(self, value):
        """
        O(logn)
        """
        self.heap.append(value)
        self.max_heapify_button(len(self.heap) - 1)
