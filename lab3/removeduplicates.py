import sys
def remDupl(ar):
    duplicates = 0
    newar = []
    for i in ar:
        if i not in newar:
            newar.append(i)
        else:
            duplicates += 1
            #print(i)
            #print(duplicates)
    #print(duplicates)
    return newar,duplicates

if __name__ == "__main__":
    fil = sys.argv[1]
    #fil ="handles.txt"
    filcopy = fil[:-4]+'_new'+fil[-4:]
    #print(filcopy)
    filarr = []
    with open(fil, 'r') as f:
        cur_elem = "test"
        while cur_elem:
            cur_elem = f.readline().strip("\n\r")
            if cur_elem:
                filarr.append(cur_elem)
        # print(filarr)
        filarr = remDupl(filarr)
        # print(filarr[1])
        with open(filcopy,'w') as fcopy:
            #fcopy.write('start\n')
            for i in filarr[0]:
                fcopy.write(str(i)+"\n")
            #fcopy.write('smth\n')
