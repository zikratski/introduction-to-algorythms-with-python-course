import sys, time

def giftTime(method):
    def timed(*args, **kwargs):
        ts = time.time()
        result = method(*args,**kwargs)
        tend = time.time()
        return (result,'\n'+str(tend-ts))
    return timed

def getTasks(tasks):
    return [tuple([int(i[0]),int(i[-1])]) for i in tasks.split(' ')]

@giftTime
def greedyTasks(tasks):
    tasks = sorted(tasks, key=lambda x: x[-1])
    start = tasks[0][0]
    temp = tasks[0]
    for i in tasks:
        if i[-1] != tasks[0][1]:
            break
        else:
            if i[0] < start:
                start = i[0]
                temp = i
    newtasks = [temp]
    for task in tasks:
        if task[0] < temp[1] or task == temp:
            continue
        else:
            newtasks.append(task)
            temp = task
    return len(newtasks), newtasks


if __name__ == '__main__':
    tasks = sys.argv[1]
    # tasks = '1,2 2,6 2,3 4,6'
    # tasks2 = '1,2 2,6 2,3 4,6 1,1 5,4 1,2'
    tasks = getTasks(tasks)
    # tasks2 = getTasks(tasks2)
    # print(tasks2)
    end_tasks = greedyTasks(tasks)
    # end_tasks2 = greedyTasks(tasks2)
    print(end_tasks[0],end_tasks[1])
