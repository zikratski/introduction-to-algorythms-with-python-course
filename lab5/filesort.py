import sys, time, tracemalloc

def sortfile(filename: str):
    with open(filename, 'r', encoding='utf-8') as f_old:
        lens = [i for i in range(len(f_old.readlines()))]
        newfilename = filename[:-4]+'_out'+filename[-4:]
        with open(newfilename,'w', encoding='utf-8') as f_new:
            for line in f_old:
                sorted_line = ' '.join(sorted(line.split()))
                f_new.write(sorted_line+'\n')
    with open(newfilename,'w', encoding='utf-8') as f:
       merge_sort_file(lens, f)

def getline(f, ind):
    for count, line in enumerate(f,1):
        if count == ind:
            pass


def merge_sort_file(lst, filename):
        if len(lst) == 1 or len(lst) == 0:
            return lst
        left_part = merge_sort_file(lst[:len(lst) // 2],filename)
        right_part = merge_sort_file(lst[len(lst) // 2:],filename)
        l = r = t = 0
        temp = [0 for i in range(len(lst))]
        while l < len(left_part) and r < len(right_part):
            if left_part[l] <= right_part[r]:
                temp[t] = left_part[l]
                l += 1
            else:
                temp[t] = right_part[r]
                r += 1
            t += 1
        while l < len(left_part):
            temp[t] = left_part[l]
            l += 1
            t += 1
        while r < len(right_part):
            temp[t] = right_part[r]
            r += 1
            t += 1
        for i in range(len(lst)):
            lst[i] = temp[i]
        return lst


if __name__ == '__main__':
    # filename = sys.argv[1]
    filename = '../big.txt'
    sortfile(filename)