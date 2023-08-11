import sys, matplotlib.pyplot as plt
def docpars(filename):
    result  = {}
    with open(filename, 'r',encoding='utf-8') as f:
        headings = f.readline().strip('\n').split(',')
        for elem in headings:
            result[elem] = []
        while True:
            cur_row = f.readline()
            if not cur_row:
                break
            else:
                cur_data = cur_row.strip('\n').split(',')
            for i,head in enumerate(headings):
                result[head].append(cur_data[i])

    return result

def benford(numberlist:list):
    first_digits = [int(str(number)[0]) for number in numberlist ]
    first_digits_nozero = [elem for elem in first_digits if elem != 0]
    distrib = {}
    for elem in first_digits_nozero:
        if elem not in distrib:
            distrib[elem] = 1
        else:
            distrib[elem] +=1
    return {k: [v, round(100*v/len(first_digits),2)] for k, v in distrib.items()}
if __name__ == '__main__':
    fil = sys.argv[1]
    #fil = 'covid_history.csv'
    if len(sys.argv) > 2:
        country = sys.argv[2]
    else:
        country = 'all'
    res = docpars(fil)
    # print(res["Belarus"])
    # print(res[country])
    test = []
    for k,v in res.items():
        if k == country or country == 'all':
            for elem in v:
                try:
                    number = float(elem)
                    test.append(number)
                except ValueError:
                    pass
    #print(benford(test))
    test = sorted(benford(test).items())
    #print(test)
    test = [[i[0],i[1][0], i[1][1]] for i in test]
    x = [i[0] for i in test]
    y = [i[1] for i in test]
    print(test)
    plt.figure()
    plt.bar(x,y)
    plt.show()
