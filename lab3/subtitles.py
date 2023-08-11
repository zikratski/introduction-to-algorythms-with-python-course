import sys
def checkTimeFormat(line):
    try:
        a = int(line[0])
        if line[2] == ':':
            return True
        else:
            return False
    except:
        return False
    # if line[0].isnumeric and line[1].isnumeric and line[2] == ':':
    #     return True
    # else:
    #     return False

def convertToSec(line):
    if line[0] == 0:
        hours_sec = int(line[1])*60*60
    elif line[0] != 0:
        hours_sec = int(line[:2]) * 60 * 60
    if line[3] == 0:
        minutes_sec = int(line[4]) * 60
    elif line[3] != 0:
        minutes_sec = int(line[3:5]) * 60
    if line[6] == 0:
        sec_sec = int(line[7])
    elif line[6] != 0:
        sec_sec = int(line[6:8])
    if line[9] == 0:
        if line[10] == 0:
            mil_sec = int(line[11])*0.001
        else:
            mil_sec = int(line[10:12])*0.001
    elif line[9] != 0:
        mil_sec = int(line[9:12])*0.001
    #print(f"milsec: {mil_sec}")
    sec = hours_sec+minutes_sec+sec_sec+mil_sec
    #print(f"sec: {sec+mil_sec}")
    return sec

def convertToTime(secs, delta):
    secs += delta
    secs = round(secs, 4)
    strtime = '00:00:00,000'
    pind = str(secs).index('.')
    milsec = str(secs)[pind+1:]
    strtime = strtime[:-3] + milsec +'0'*(3-len(milsec))
    hms = int(str(secs)[:pind])
    seconds = str(hms % 60)
    strtime = strtime[:-(4+len(seconds))] + seconds + strtime[8:]
    hm = hms // 60
    minutes = str(hm % 60)
    strtime = strtime[:-(7 + len(minutes))] + minutes + strtime[5:]
    hours = str(hm // 60)
    strtime = strtime[:-(10 + len(hours))] + hours + strtime[2:]
    #print(strtime)
    return strtime

if __name__ == "__main__":
    #fil = 'starwars.srt'
    fil = sys.argv[1]
    delta_time = 0
    if len(sys.argv) > 2:
        delta_time = float(sys.argv[2])
    filcopy = fil[:-4]+'_updated'+fil[-4:]
    copyar = []
    timear = []
    with open(fil,'r', encoding='utf8') as f:
        count = 0
        for line in f:
            # count += 1
            copyar.append(line)
            if checkTimeFormat(line):
                #print("it is time: ")
                # ftime = convertToSec(line[:12])
                # stime = convertToSec(line[17:])
                timear.append([convertToSec(line[:12]),convertToSec(line[17:])])
            #print(line)
            # if count > 100:
            #     break
        #print(copyar)
        with open(filcopy,'w',encoding='utf8') as fcopy:
            k = 0
            for i in copyar:
                if checkTimeFormat(i):
                    convertToTime(timear[k][0], delta_time)
                    newi = convertToTime(timear[k][0], delta_time) + i[12:17] + convertToTime(timear[k][1], delta_time)+'\n'
                    fcopy.write(str(newi))
                    k +=1
                    # if k > 10:
                    #     continue
                else:
                    fcopy.write(str(i))
    # print(f"Array:")
    # for i in timear:
    #     print(i)