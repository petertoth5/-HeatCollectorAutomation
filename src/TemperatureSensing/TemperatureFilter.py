#!/usr/bin/env python
 
def calculate_average(buffer):
    if buffer.is_empty():
        print("Buffer is empty nothing to filter")
        return None

    sum_of_elements = 0
    current_size = buffer.size
    current_index = buffer.head
    for _ in range(current_size):
        sum_of_elements += buffer.buffer[current_index]
        current_index = (current_index + 1) % buffer.capacity

    return sum_of_elements / current_size

class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0  # pointer to first element
        self.tail = 0  # pointer to last element
        self.size = 0  # actual size, it's 0 by default

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            self.dequeue()
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        if self.size < self.capacity:
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Buffer is empty, nothing to delete")
            return None
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def display(self):
        print("Buffer content")
        if self.is_empty():
            print("Empty")
            return
        for i in range(self.size):
            idx = (self.head + i) % self.capacity
            print(self.buffer[idx], end=" ")
        print()

