import sys
def checkLine(line,year,country):
    flag = False
    if len(country) == 0:
        nowcountry = country
        flag2 = False
    else:
        nowcountry = ''
        flag2 = True
    newline = ''
    for i in range(len(line)):
        if line[i].isnumeric():
            try:
                nowyear = int(line[i+5:i+9])+71
            except:
                break
            if flag2:
                nowcountry = line[i+10:-1].lower()
            if year == nowyear and country == nowcountry:
                flag = True
            newline = line[:i-1]+' ('+line[i:i+4]+'-'+line[i+5:i+9]+') '+line[i+10:-1]
            break
    return flag, newline

if __name__ == "__main__":
    year = 2023
    country = ''
    infile = sys.argv[1]
    if len(sys.argv) > 2:
        year = int(sys.argv[2])
        if len(sys.argv) > 3:
            country = sys.argv[3].lower()
    #infile = "authors.tsv"
    #year = 2045
    with open(infile, 'r',encoding='utf8') as f:
        i = 0
        for line in f:
            if i == 0:
                i = 1
                continue
            if checkLine(line,year,country)[0]:
                print(checkLine(line, year,country)[1])