import sys
import time

def getWordsToDict(line, words):
    line = line.split(' ')
    #print(line)
    for i in line:
        if i == '\n' or i == '':
            continue
        if '\'' in i:
            i = f'{i}'
        if i[0] == '"' or i[0] == '(' or i[0] == '\'':
            i = i[1:]

        while('.' in i or ',' in i or ';' in i or '!' in i
              or ':' in i or '?' in i or '"' in i or ')' in i
            or '\n' in i or '(' in i):
            i = i[:-1]

        i = i.lower()
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
if __name__ == "__main__":
    start = time.time()
    fil = sys.argv[1]
    if len(sys.argv) > 2:
        n = int(sys.argv[2])
    else:
        n = 3
    #fil = 'karenina.txt'
    #n = 7
    words = {}
    with open(fil, 'r') as f:
        last = 0
        for line in f:
            getWordsToDict(line, words)

    nwords = sorted(words.items(),key = lambda x:x[1])
    #print(nwords)
    nwords.reverse()
    count = 0
    for i in nwords:
        if len(i[0]) >= n:
            count +=1
            print(i[1],'\t',i[0])
        if count == 10:
            break
    end = time.time()
    #print(f"time: {end-start}")
    #print(words)
    #print(nwords)
