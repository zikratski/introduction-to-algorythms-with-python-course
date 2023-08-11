import sys
#data[Name,Games,Won,Drawn,Lost,Score,sb,[losers],[sames]")
def updateData(name,arr,score,opponent):
    score = float(score)
    for i in range(len(arr)):
        if arr[i][0] == name:
            arr[i][1] += 1 #games
            if score == 1:
                arr[i][2] += 1
                arr[i][7] += [opponent]
            elif score == 0.5:
                arr[i][3] += 1
                arr[i][8] += [opponent]
            else:
                arr[i][4] += 1
            arr[i][5] += score
            scorear[i] += score
            return 0
    namesar.append(name)
    scorear.append(score)
    i = len(arr)
    arr.append([])
    arr[i] = [name,1,0,0,0,score,0,[],[]]
    if score == 1:
        arr[i][2] += 1
        arr[i][7] += [opponent]
    elif score == 0.5:
        arr[i][3] += 1
        arr[i][8] += [opponent]
    else:
        arr[i][4] += 1

def scoreBerger(line,arr):
    winnersum = 0
    drawnsum = 0
    for loser in line[7]:
        ind = namesar.index(loser)
        winnersum += arr[ind][5]
    for drawn in line[8]:
        ind = namesar.index(drawn)
        drawnsum += arr[ind][5]

    line[6]=winnersum+drawnsum/2
    #sbar
def sortByScore(ar,scorear, sbar):
    for i in range(len(ar) - 1):
        for j in range(len(ar) - i - 1):
            if scorear[j] == scorear[j+1]:
                if sbar[j] < sbar[j + 1]:
                    scorear[j], scorear[j + 1] = scorear[j + 1], scorear[j]
                    ar[j], ar[j + 1] = ar[j + 1], ar[j]
                    sbar[j], sbar[j + 1] = sbar[j + 1], sbar[j]
            elif scorear[j] < scorear[j + 1]:
                scorear[j], scorear[j + 1] = scorear[j + 1], scorear[j]
                ar[j], ar[j + 1] = ar[j + 1], ar[j]
                sbar[j], sbar[j + 1] = sbar[j + 1], sbar[j]





if __name__ == "__main__":
    tables = []
    namesar = []
    scorear = []
    sbar = []
    tata = sys.argv[1]
    #tata = 'tata.tsv'
    with open(tata, 'r',encoding='utf8') as f:
        i = 0
        for line in f:
            line_arr = line.split('\t')
            if '\n' in line_arr[-1]:
                line_arr[-1] = line_arr[-1][:-1]
            updateData(line_arr[0],tables,line_arr[2],line_arr[1])
            updateData(line_arr[1], tables, line_arr[3], line_arr[0])
        for line in tables:
            scoreBerger(line, tables)
        print(namesar)
        print(scorear)
        sbar = [i[6] for i in tables]
        print(sbar)
        sortByScore(tables,scorear,sbar)
        #for line in tables:


    print("#\t Name\t Games\t Won\t Drawn\t Lost\t Score\t SB")
    for i in range(len(tables)):
        print(f"{i}\t {tables[i][0]}\t {tables[i][1]}\t {tables[i][2]}\t "
              f"{tables[i][3]}\t {tables[i][4]}\t {tables[i][5]}\t {tables[i][6]}")
    # print(namesar)
    # print(scorear)

