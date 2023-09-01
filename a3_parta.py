class MinHeap:
    
    def __init__(self, arr=None):
        self.heap = arr or []

        if len(self.heap) > 1:

            # As soon as we recieve a new array, we have to make sure that it is made minheap. So, we start from last nonleaf node allt he way up.
            for i in range(((len(self.heap) - 2) // 2), -1, -1): # go backwards in loop starting from 1st non leaf node.
                self._min_heapify(i)


    def insert(self, element):
        self.heap.append(element)

        idx = len(self.heap) - 1 # This is the last index of the array 

        #parent_idx = (idx - 1) // 2 # This is to find the parent of the last index.
        #OR
        parent_idx = (len(self.heap) - 2) // 2 # last non leaf node

        # THis is done to maintain the min heap property -

        while idx > 0 and self.heap[idx] < self.heap[parent_idx]:
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx
            parent_idx = (idx - 1) // 2


    def get_min(self):
        if self.heap:
            return self.heap[0]
        return None

    def extract_min(self):
        if not self.heap:
            return None

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_element = self.heap.pop()
        self._min_heapify(0)
        return min_element

    def is_empty(self):
        return len(self.heap) == 0

    def __len__(self):
        return len(self.heap)
    
    def _min_heapify(self, initial_idx):
        smallest = initial_idx
        left_child = 2 * smallest + 1
        right_child = 2 * smallest + 2
        
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        if smallest != initial_idx:
            self.heap[smallest], self.heap[initial_idx] = self.heap[initial_idx], self.heap[smallest]
            self._min_heapify(smallest)
