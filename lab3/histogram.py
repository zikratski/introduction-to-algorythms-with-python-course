import sys
def hist(seq: list, n: int):
    res = [0] * n
    min_n = min(seq)
    max_n = max(seq)
    interval = max_n - min_n
    for elem in seq:
        if elem == max_n:
            res[-1] += 1
        else:
            position = int(n * (elem - min_n) / interval)
            res[position] += 1
    return res


if __name__ == "__main__":
    fil = sys.argv[1]
    n = int(sys.argv[2])
    res = []

    with open(fil, 'r') as f:
        cur_elem = "none"
        while cur_elem:
            cur_elem = f.readline().strip("\n\r")
            if cur_elem:
                cur_elem = float(cur_elem)
                res.append(cur_elem)
    # print(res)
    print(hist(res, n))
