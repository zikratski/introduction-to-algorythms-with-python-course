# Напишите программу stackdummy.py, в которой реализуйте следующий набор стековых операций используя
# list или collections.deque:
#
#     def create_stack() – создает пустой стек и возвращает его
#     def is_empty(stack) – проверяет, пуст ли стек (возвращает true – пуст и false – нет)
#     def push(stack, item) – добавляет элемент в стек
#     def pop(stack) – возвращает верхний элемент и удаляет его из стека (если стек не пуст, иначе сообщение “stack is empty”)
#     def peek(stack) – возвращает верхний элемент стека без удаления (если стек не пуст, иначе сообщение “stack is empty”)
#
# Далее создайте стек (используя create_stack), добавьте туда 100 тыс. случайных чисел от 0 до 1 (push),
# потом достаньте их (pop) всех пока стек не станет пустым (делая проверку is_empty).
# Выведите время выполнения и результат применения peek.



import random
import time
from collections import deque


class Stack:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return True if not self.items else False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else print("Error: empty stack")

    def peek(self):
        el = self.items.pop()
        self.push(el)
        return el

    def dequeLen(self):
        return len(self.items)


if __name__ == '__main__':
    s = Stack()
    start = time.time()
    for i in range(100000):
        s.push(random.random())
    #print(len(s.items))
    while not s.is_empty():
        s.pop()
    end = time.time()
    print(end - start)
    s.pop()
    #print(len(s.items))
