# Напишите программу wordshuffle.py, которая в заданной текстовой строке перемешивает буквы внутри слов,
# оставляя первую и последнюю буквы на месте. Например, для строки “good news everyone” может быть такой
# вывод “good news eyvorene”. Говорят, что наш мозг вполне способен распознавать такой текст практически
# потери понимания -- проверьте это.
# Замечание: Для простоты считаем, что строка состоит только из строчных букв и пробелов.

import sys
import random

words = sys.argv[1].split(' ')
def randword(words):
    newords = []
    for word in words:
        word = [i for i in word]
        if len(word) == 1:
            newords += word
        else:
            neword = word[1:len(word) - 1]
            random.shuffle(neword)
            neword.insert(0, word[0])
            neword.append(word[len(word) - 1])
            n = ''.join(neword)
            newords += [n]
    res = ' '.join(newords)
    return res
#for i in range(20):
print(randword(words))