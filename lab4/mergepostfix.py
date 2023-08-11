# Напишите программу mergepostfix.py, которая для списка слов находит самую длинную общую строку в
# этих слов. Например, для списка 'starlink hyperlink weblink' такой строкой будет 'link'.
# Если такого постфикса нет, то выводится пустая строка. Для решения примените стратегию “разделяй и властвуй”.

import sys
def getGCD(arr):
    if len(arr) == 2:
        if len(arr[1]) != 0 and len(arr[0]) != 0 and arr[0][-1] == arr[1][-1]:
            last = arr[0][-1]
            df = getGCD([arr[0][:-1], arr[1][:-1]])
            return ''.join([df,last])
        else:
            return ''
    elif len(arr) == 1:
        return arr[0]
    else:
        return getGCD([getGCD(arr[:len(arr)//2]),getGCD(arr[len(arr)//2:])])

if __name__ == '__main__':
    strok = sys.argv[1]
    #strok = 'starlink starlink tarlink'
    strok = strok.split(' ')
    gcd = getGCD(strok)
    print(gcd)