import sys, matplotlib.pyplot as plt


def getData(file, column, region):
    data = {}
    # print(f"column: {column}")
    with open(file, 'r', encoding='utf-8') as f:
        headline = f.readline().strip('\n').split(',')
        nowline = 'none'
        while True:
            nowline = f.readline()
            # nowline = [elem for elem in nowline if len(elem) != 0]
            # print(nowline)
            # print(len(nowline))
            if not nowline:
                # print('break')
                break
            else:
                nowline = nowline.strip('\n').split(',')
            if len(nowline) > 1:
                if (region == 'all' or region == nowline[1]) and len(nowline[column]) > 1:
                    ind = nowline[column].index('.')
                    data[nowline[2]] = int(nowline[column][:ind])
                    # print(nowline[2])

        # print(data)
    return data, headline[column]


def getMean(arr):
    return sum(arr) / len(arr)


def getSigma(arr, mean):
    summ = 0
    for i in arr:
        summ += (mean - i) ** 2
    return (summ / (len(arr)-1)) ** 0.5


def filterData(data, mean, sigma):
    newdata = {}
    for i in data:
        if not (mean - sigma <= data[i] <= mean + sigma):
            newdata[i] = data[i]
    return newdata


if __name__ == '__main__':
    fil = sys.argv[1]
    #fil = 'covid_latest.csv'
    column_num = 11
    country = 'all'
    data = {}
    if len(sys.argv) > 2:
        try:
            column_num = int(sys.argv[2])
            if len(sys.argv) > 3:
                country = sys.argv[3]
        except ValueError:
            country = sys.argv[2]
        except:
            pass
    data = getData(fil, column_num, country)[0]
    column = getData(fil, column_num, country)[1]
    # print(data)
    mean = getMean(data.values())
    sigma = getSigma(data.values(), mean)
    # print(data)
    newdata = filterData(data, mean, sigma)
    # print(newdata)
    xdata = [i for i in range(len(data))]
    # print(list(data.values()))
    plt.figure()
    plt.subplot(1,2,1)
    plt.plot([0,len(data)],[mean,mean],c='red')
    plt.plot([0, len(data)], [mean - sigma, mean - sigma], c='blue',linestyle='--')
    plt.plot([0, len(data)], [mean + sigma, mean + sigma], c='blue',linestyle='--')
    plt.scatter(xdata, list(data.values()), s=2)
    plt.subplot(1, 2, 2)
    plt.axis(False)
    text_high = ''
    text_low = ''
    for i in newdata:
        if newdata[i] > mean + sigma:
            text_high = text_high + i +': '+str(round(newdata[i])) + '\n'
        elif newdata[i] < mean - sigma:
            text_low = text_low + i+': '+str(round(newdata[i])) + '\n'
    # print(text_high)
    # print(text_low)
    plt.text(0.1, 1,column+'\n\n'+f'Mean: {round(mean,2)}'+'\n'
             +f'St.dev: {[round(mean - sigma,2), round(mean + sigma,2)]}'
             +'\n\n'+'Too high: \n'+text_high+'\n\n'+'Too low: \n'+text_low,
             horizontalalignment='left', verticalalignment='top')
    plt.show()
