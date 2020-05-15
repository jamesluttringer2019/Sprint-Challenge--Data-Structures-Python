class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest = 0
        self.values = []
    def append(self, item):
        if len(self.values)<self.capacity:
            self.values.append(item)
        else:
            self.values[self.oldest] = item
            if self.oldest < self.capacity-1:
                self.oldest += 1
            else:
                self.oldest = 0
    def get(self):
        return self.values