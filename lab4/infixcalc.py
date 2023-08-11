# Напишите программу infixcalc.py, в которой реализуйте вычисление арифметического выражения
# заданного обычной инфиксной формой, например, “(4 + 2) / 3 + 2 * (7 -3) / 4” при помощи алгоритма Дейкстры.
# Этот алгоритм служит для преобразования инфиксной записи в постфиксную, ну а вычисление постфиксного выражение
# вы уже сделали выше. Выражение задается на входе строкой вида “(4 + 2) / 3 + 2 * (7 -3) / 4”.
# Поддерживаются целые числа,  арифметические операции +, -, *, / и скобки ().
# Если выражение содержит другие символы или не является корректным, то выводится “invalid input”.

import sys
from queuedummy import Queue
from stackdummy import Stack
import postfixcalc

def getPostfix(infstr):
    q = Queue()
    s = Stack()
    high_oper =  {'*': 'mul', '/': 'truediv'}
    low_oper = {'+': 'add', '-': 'sub'}
    postf = ''
    flag = 0
    for i in infstr:
        if i.isdigit():
            q.enqueue(i)
        elif i in high_oper or i in low_oper:
            if s.is_empty() or s.peek() == '(':
                s.push(i)
            elif s.peek() in low_oper and i in high_oper:
                s.push(i)
            elif i in low_oper or (i in high_oper and s.peek() in high_oper):
                while not s.is_empty() and s.peek() not in low_oper and s.peek() != '(':
                    q.enqueue(s.pop())
                s.push(i)

        elif i == '(':
            s.push(i)
        elif i == ')':
            while s.peek() != '(':
                elem = s.pop()
                if elem != '(':
                    q.enqueue(elem)
        else:
            return ('invalid input')
    while s.items:
        elem = s.pop()
        if elem != '(':
            q.enqueue(elem)
    return q.items
if __name__ == '__main__':
    #inf_str = sys.argv[1]
    inf_str = '-( 3 + 9 ) / 2 * 5 - ( 15 - 10 ) / 5'
    #operators = {'+': 'add', '-': 'sub', '*': 'mul', '/': 'truediv'}
    inf_str = inf_str.split(' ')
    #print(inf_str)
    pst_str = getPostfix(inf_str)
    #print(pst_str)
    rez = postfixcalc.revPolNot(pst_str)
    print(rez)
