import sys
import time


def giftTime(method):
    def timed(*args, **kwargs):
        ts = time.time()
        result = method(*args,**kwargs)
        tend = time.time()
        return (result,'\n'+str(tend-ts))
    return timed

def getAr(filename):
    arr = []
    with open(filename, encoding='utf-8') as f:
        for line in f:
            arr.append(line.strip('\n'))
    return arr

@giftTime
def linearSearch(arr, word):
    newarr = []
    flag = False
    for i in arr:
        if word == i:
            flag = True
        if flag == True:
            try:
                if i[len(word)-1] == word[-1]:
                    newarr.append(i)
                else:
                    return newarr
            except:
                return newarr
    if flag == False:
        return newarr

@giftTime
def binarySearch(arr, word):
    low = 0
    newar = []
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == word:
            for i in arr[mid:]:
                try:
                    if i[len(word) - 1] == word[-1]:
                        newar.append(i)
                    else:
                        return newar
                except:
                    return newar
        elif guess < word:
            low = mid + 1
        else:
            high = mid - 1
    return newar

if __name__ == '__main__':
    filename = sys.argv[1]
    word = sys.argv[2]
    # filename = 'dict.txt'
    # word = 'virus'
    ar_dict = getAr(filename)
    newar = linearSearch(ar_dict, word)
    print(newar[0],'\n'+newar[1])
    newar = binarySearch(ar_dict,word)
    print(newar[0],'\n'+newar[1])