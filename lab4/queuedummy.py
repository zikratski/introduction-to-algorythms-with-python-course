from collections import deque
import random, time

class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return True if not self.items else False

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft() if not self.is_empty() else "Error: empty stack"

    def peek(self):
        el = self.items.popleft()
        self.enqueue(el)
        for i in range(len(self.items)-1):
            curr_el = self.items.popleft()
            self.enqueue(curr_el)
        return el
    def queueLen(self):
        return len(self.items)
    def changeFirstEl(self, sdvig):
        el = self.items.popleft()
        el +=sdvig
        self.enqueue(el)
        for i in range(len(self.items) - 1):
            curr_el = self.items.popleft()
            self.enqueue(curr_el)
        return el

if  __name__ == '__main__':
    q = Queue()
    start = time.time()
    for i in range(100000):
        q.enqueue(random.random())
    print(len(q.items))
    # print(f"dsfsdf: {s.items[-1]} + {s.items[-2]} = {s.pop()+s.pop()}")
    while not q.is_empty():
        q.dequeue()
    end = time.time()
    print(end - start)
    print(len(q.items))

