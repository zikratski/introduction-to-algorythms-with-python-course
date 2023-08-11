# Напишите программу checkbrackets.py, которая для текстовой строки, состоящей из круглых скобок,
# проверяет правильность этого скобочного выражения используя стек. Скобочное выражение правильное если:
#
#     скобки сбалансированы, т.е. в каждой паре скобка сначала открывается, а потом закрывается
#     скобка закрывается после того, как закрыты все скобки, открытые внутри нее
#
# Вход: строка вида “(()()(()()))”
#
# Выход: True/False

import sys
from stackdummy import Stack
def checkBraces(inpstr):
    s = Stack()
    for i in inpstr:
        s.push(i)
        if i == ')':
            if s.dequeLen() == 1:
                return False
            s.pop()
            s.pop()
    return True if s.is_empty() else False

if __name__ == '__main__':
    inpstr = sys.argv[1]
    #inpstr = '()()(()((())'
    print(checkBraces(inpstr))
