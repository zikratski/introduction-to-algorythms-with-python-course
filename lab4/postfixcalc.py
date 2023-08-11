# Напишите программу postfixcalc.py, в которой реализуйте вычисление арифметического выражения,
# заданного постфиксной (польской) нотацией, при помощи стека. Алгоритм вычисления приведен там же.
# Выражение задается на входе строкой вида “4 3 2 * +”.Поддерживаются целые числа и арифметические операции +, -, *, /.
# Если выражение содержит другие символы или не является корректным, то выводится “invalid input”.

import sys
from collections import deque
from stackdummy import Stack

def oper(el1,el2, ops, i):
    meth = '__%s__' % ops[i]
    return getattr(el2, meth)(el1)

def revPolNot(inpstr):
    s = Stack()
    operators = {'+': 'add', '-': 'sub', '*': 'mul', '/': 'truediv'}
    for i in inpstr:
        # print(s.items)
        if i.isdigit():
            s.push(i)
        elif i in operators:
            try:
                fir = int(s.pop())
                sec = int(s.pop())
                operat = oper(fir, sec, operators, i)
                s.push(operat)
            except:
                return ('invalid input')
            #s.push(oper(f,s,operators,i))
        else:
            return ('invalid input')
    return s.items[0]
if __name__ == '__main__':
    inpstr = sys.argv[1]
    #inpstr = '3 9 9 * +'
    inpstr = inpstr.split(' ')
    # print(inpstr)
    rez = revPolNot(inpstr)
    print(rez)