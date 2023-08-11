import sys, random, time, copy


def generateNums(n):
    return [random.randrange(0,1000) for _ in range(n)]
def selection_sort(lst):
    for i in range(len(lst)-1):
        imin = i
        for ind in range(i+1, len(lst)):
            if lst[ind] < lst[imin]:
                imin = ind
        lst[i], lst[imin] = lst[imin], lst[i]
    return lst
def bubble_sort(lst):
    n = len(lst)
    for j in range(n - 1):
        flag = False
        for i in range(n - 1 - j):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                flag = True
        if not flag:
            break
    return lst
def insertion_sort(lst):
    for j in range(1,len(lst)):
        key = lst[j]
        i = j - 1
        while i >= 0 and lst[i] > key:
            lst[i+1] = lst[i]
            i -=1
        lst[i+1] = key
    return lst
def quick_sort(lst):
    quicksortLomuto(lst, 0, len(lst)-1)
    return lst
def quicksortLomuto(lst, low, high):
    if low < high:
        pivot_index = partition(lst, low, high)
        quicksortLomuto(lst, low, pivot_index - 1)
        quicksortLomuto(lst, pivot_index + 1, high)
    # return lst
def partition(lst, low, high):
    pivot = lst[high]
    i = low-1
    for j in range(low, high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j]= lst[j], lst[i]

    lst[i+1], lst[high] = lst[high], lst[i+1]
    return i+1
def merge_sort(lst):
    if len(lst) == 1 or len(lst) == 0:
        return lst
    left_part = merge_sort(lst[:len(lst) // 2])
    right_part = merge_sort(lst[len(lst) // 2:])
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
def python_sort(lst):
    min_run = 32
    n = len(lst)
    for i in range(0, n, min_run):
        lst[i:min((i + min_run - 1), n - 1)+1] = insertion_sort(lst[i:min((i + min_run - 1), n - 1)+1])
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            lst[start:end + 1] = sortLists(lst[start:mid + 1], lst[mid + 1:end + 1])
        size *= 2
    return lst
def sortLists(list1, list2):
    merged_list = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    return merged_list


if __name__ == '__main__':
    if len(sys.argv) > 2:
        n = int(sys.argv[1])
        out = sys.argv[2]
    elif len(sys.argv) == 2:
        if sys.argv[1].isalnum():
            n = int(sys.argv[1])
            out = False
        else:
            out = sys.argv[1]
            n = 10
    else:
        n = 10
        out = False
    # out = True
    # n = 1000

    arr = generateNums(n)
    sort_dict = {0:['bubble sort',bubble_sort],1:['insertion sort',insertion_sort],2:['selection sort',selection_sort],
                 3:['quick sort',quick_sort],4:['merge sort',merge_sort],5:['python sort',python_sort]}
    # print(arr)
    # arr = [572, 800, 574, 754, 632, 642, 96, 405, 491, 726]
    for i in sort_dict:
        # if i == 0 or i == 1 or i == 2 or i==3:
        #     continue
        # print(arr)
        start = time.time()
        newar = copy.deepcopy(arr)
        newar = sort_dict[i][1](newar)
        end = time.time()
        print(sort_dict[i][0])
        print(end-start)
        if out:
            print(newar)
        print()





