import sys, time
def giftTime(method):
    def timed(*args, **kwargs):
        ts = time.time()
        result = method(*args,**kwargs)
        tend = time.time()
        return (result,'\n'+str(tend-ts))
    return timed

def is_valid_state(state,n):
        if state[-1] in state[:-1]:
            return False
        not_valid = set()
        for ind, i in enumerate(state[:-1]):
            if abs(len(state)-1 - ind) == abs(state[-1] - i):
                return False
        return True

def get_candidates(state, n):
    candidates = [i for i in range(n)]
    return list(filter(lambda x: x not in state, candidates))


def search(state, solutions, n, now):
    if now == 0:
        if is_valid_state(state,n):
            solutions.append(state.copy())
    for candidate in get_candidates(state, n):
        state.append(candidate)
        if is_valid_state(state,n):
            search(state, solutions, n, now-1)
        state.remove(candidate)


@giftTime
def solve(n):
    solutions = []
    state = list()
    search(state, solutions, n, now=n)
    return len(solutions), solutions

if __name__ == '__main__':
    n = int(sys.argv[1])
    # n = 8
    print(solve(n)[-1], solve(n)[0][0],solve(n)[0][1])
    # print(solve(n)[0])

