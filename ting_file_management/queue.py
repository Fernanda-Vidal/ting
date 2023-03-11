from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.__len__ == 0:
            return None
        return self.queue.pop(0)

    def search(self, index):
        if index >= 0:
            return self.queue[index]
        raise IndexError
