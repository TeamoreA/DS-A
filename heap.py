class BinaryHeap:
    def __init__(self, size=10, h_type='Max'):
        self.heap = (size+1)*[None]
        self.max_size = size+1
        self.size = 1
        self.h_type = h_type

    def peek(self):
        return self.heap[1]

    def size(self):
        return self.size

    def level_order_traversal(self):
        for i in range(1, self.size+1):
            if self.heap[i] is not None:
                print(self.heap[i])

    def heapify(self, index):
        if index <= 1:
            return
        parent_index = int(index/2)
        if self.h_type == 'Max':
            if self.heap[index] > self.heap[parent_index]:
                temp = self.heap[parent_index]
                self.heap[parent_index] = self.heap[index]
                self.heap[index] = temp
            self.heapify(parent_index)

        elif self.h_type == 'Min':
            if self.heap[index] < self.heap[parent_index]:
                temp = self.heap[parent_index]
                self.heap[parent_index] = self.heap[index]
                self.heap[index] = temp
            self.heapify(parent_index)

    def insert(self, value):
        if self.size+1 == self.max_size:
            return
        self.heap[self.size] = value
        
        self.heapify(self.size)
        self.size += 1

    def get_deepest_node(self):
        i = 1
        while self.heap[i*2] is not None:
            i *= 2
            # print(i)
        return self.heap[i]

    def heapify_extract(self, index = 1):
        left_index = index * 2
        right_index = index * 2 + 1
        swap_index = 0
        if left_index > self.size:
            return
        elif left_index == self.size:
            if self.h_type == 'Min':
                if self.heap[index] > self.heap[left_index]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[left_index]
                    self.heap[left_index] = temp
                    return

            if self.h_type == 'Max':
                if self.heap[index] < self.heap[left_index]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[left_index]
                    self.heap[left_index] = temp
                    return
        else:
            if self.h_type == 'Min':
                if self.heap[left_index] < self.heap[right_index]:
                    swap_index = left_index
                else:
                    swap_index = right_index
                if self.heap[index] > self.heap[swap_index]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[swap_index]
                    self.heap[swap_index] = temp

            if self.h_type == 'Max':
                if self.heap[left_index] > self.heap[right_index]:
                    swap_index = left_index
                else:
                    swap_index = right_index

                if self.heap[index] < self.heap[swap_index]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[swap_index]
                    self.heap[swap_index] = temp
            self.heapify_extract(swap_index)
    def extract(self):
        if self.heap[1] is None:
            return
        else:
            extracted_node = self.heap[1]
            self.heap[1] = self.heap[self.size - 1]
            self.heap[self.size] = None
            self.size -= 1
            
            self.heapify_extract()
            return extracted_node

        


max_h = BinaryHeap(5, 'Max')
max_h.insert(4)
max_h.insert(5)
max_h.insert(2)
max_h.insert(1)
max_h.level_order_traversal()
print('==============')
print(max_h.extract())