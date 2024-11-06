# Processes List Structure
# {ProcessName/ProcessId: [ArrivalTime, BurstTime, Priority]}
# [ProcessName/ProcessId, ArrivalTime, BurstTime, Priority]

# Output Structure
# {ProcessName/ProcessId: [CompletionTime, TurnaroundTime, WaitingTime]}

def sortprocesses(processDict, key=""):
    processes = {x[0]:x[1] for x in processDict.items()}
    lst = []
    for process in processes:
        tmpProcess = [process]
        tmpProcess.extend([p for p in processes[process]])
        lst.append(tmpProcess)
    d = {"AT": 1, "BT": 2, "PR": 3}
    if key in d:
        index = d[key]
    else:
        index = 0
    lst.sort(key=lambda x: x[index])
    return lst





def avg(processDict, key):
    processes = {x[0]:x[1] for x in processDict.items()}
    d = {"TT": 1, "WT": 2}
    index = d[key]

    s = sum(list(map(lambda x: x[index], processes.values())))
    # for process in processes:
    #     s += processes[process][index]
    avg = s/len(processes)
    return avg



        
        
            
                
    

def fcfs(processDict):
    processes = {x[0]:x[1] for x in processDict.items()}
    readyQueue = sortprocesses(processes, key="AT")
    outputDict = {}
    time = 0
    for process in readyQueue:
        while time<process[1]:
            time += 1
        time += process[2]
        tt = time-process[1]
        wt = tt-process[2]
        outputDict[process[0]] = [time, tt, wt]
    return outputDict

def sjf(processDict):
    processes = {x[0]:x[1] for x in processDict.items()}
    n = len(processes)
    time = 0
    count = 0
    readyDict = {}
    outputDict = {}
    completedList = []
    while count<n:
        readyDict.update(dict(filter(lambda p: p[0] not in completedList and p[1][0]<=time, processes.items())))
        # for process in processes:
        #     if processes[process][0]<=time:
        #         if process not in completedList:
        #             readyDict[process] = processes[process]
        readyQueue = sortprocesses(readyDict, "BT")
        if readyQueue == []:
            time = time + 1
        else:
            time = time + readyQueue[0][2]
            tt = time-readyQueue[0][1]
            wt = tt-readyQueue[0][2]
            completedList.append(readyQueue[0][0])
            outputDict[readyQueue[0][0]] = [time, tt, wt]
            del readyDict[readyQueue[0][0]]
            count += 1
    return outputDict

def prioritynp(processDict):
    processes = {x[0]:x[1] for x in processDict.items()}
    n = len(processes)
    time = 0
    count = 0
    readyDict = {}
    outputDict = {}
    completedList = []
    while count<n:
        readyDict.update(dict(filter(lambda p: p[0] not in completedList and p[1][0]<=time, processes.items())))
        # for process in processes:
        #     if processes[process][0]<=time:
        #         if process not in completedList:
        #             readyDict[process] = processes[process]
        readyQueue = sortprocesses(readyDict, "PR")
        if readyQueue == []:
            time = time + 1
        else:
            time = time + readyQueue[0][2]
            tt = time-readyQueue[0][1]
            wt = tt-readyQueue[0][2]
            completedList.append(readyQueue[0][0])
            outputDict[readyQueue[0][0]] = [time, tt, wt]
            del readyDict[readyQueue[0][0]]
            count += 1
    return outputDict

def rr(processDict, quantum=1):
    processes = {x[0]:x[1] for x in processDict.items()}
    n = len(processes)
    time = 0
    count = 0
    # index = 0
    outputDict = {}
    sortedList = sortprocesses(processes, key="AT")
    readyQueue = []
    btList = []
    flag = True
    while count<n:
        if sortedList!=[] and readyQueue==[]:
            while time<sortedList[0][1] and readyQueue==[]:
                time += 1
            while sortedList!=[] and sortedList[0][1]==time:
                readyQueue.append(sortedList[0])
                btList.append(sortedList[0][2])
                sortedList.pop(0)

        if btList[0]>quantum:
            # print(readyQueue[0])
            btList[0]-= quantum
            time += quantum
            flag = True
            
        else:
            # print(readyQueue[0])
            time += btList[0]
            tt = time - readyQueue[0][1]
            wt = tt - readyQueue[0][2]
            outputDict[readyQueue[0][0]] = [time, tt, wt]
            readyQueue.pop(0)
            btList.pop(0)
            flag = False
            count += 1

        while sortedList!=[] and sortedList[0][1]<=time:
                readyQueue.append(sortedList[0])
                btList.append(sortedList[0][2])
                sortedList.pop(0)

        if flag:
            tmp = btList[0]
            btList.pop(0)
            btList.append(tmp)
            tmp = readyQueue[0]
            readyQueue.pop(0)
            readyQueue.append(tmp)
    return outputDict


def srtf(processDict):
    processes = {x[0]:x[1] for x in processDict.items()}
    n = len(processes)
    time = 0
    count = 0
    readyDict = {}
    outputDict = {}
    arrivedList = []
    readyQueue=[]
    arrived=False
    while count<n:
        tempDict = dict(filter(lambda p: p[0] not in arrivedList and p[1][0]==time, processes.items()))
        arrived = (tempDict!={})
        arrivedList.extend([p for p in tempDict.keys()])
        readyDict.update(tempDict)

        # for process in processes:
        #     if processes[process][0]==time:
        #         if process not in arrivedList:
        #             readyDict[process] = processes[process]
        #             arrivedList.append(process)
        #             arrived = True

        if arrived:
            readyQueue = sortprocesses(readyDict, "BT")
            arrived = False
        if readyQueue == []:
            time = time + 1
        else:
            if readyDict[readyQueue[0][0]][1] == 1:
                time = time + 1
                tt = time - readyQueue[0][1]
                wt = tt - processDict[readyQueue[0][0]][1]
                outputDict[readyQueue[0][0]] = [time, tt, wt]
                del readyDict[readyQueue[0][0]]
                readyQueue = sortprocesses(readyDict, "BT")
                count += 1
            else:
                time = time + 1
                readyDict[readyQueue[0][0]][1] -= 1
    return outputDict

def priorityp(processDict):
    processes = {x[0]:x[1] for x in processDict.items()}
    n = len(processes)
    time = 0
    count = 0
    readyDict = {}
    outputDict = {}
    arrivedList = []
    readyQueue=[]
    arrived=False
    while count<n:
        tempDict = dict(filter(lambda p: p[0] not in arrivedList and p[1][0]==time, processes.items()))
        arrived = (tempDict!={})
        arrivedList.extend([p for p in tempDict.keys()])
        readyDict.update(tempDict)
        # for process in processes:
        #     if processes[process][0]==time:
        #         if process not in arrivedList:
        #             readyDict[process] = processes[process]
        #             arrivedList.append(process)
        #             arrived = True

        if arrived:
            readyQueue = sortprocesses(readyDict, "PR")
            arrived = False
        if readyQueue == []:
            time = time + 1
        else:
            if readyDict[readyQueue[0][0]][1] == 1:
                time = time + 1
                tt = time - readyQueue[0][1]
                wt = tt - processDict[readyQueue[0][0]][1]
                outputDict[readyQueue[0][0]] = [time, tt, wt]
                del readyDict[readyQueue[0][0]]
                readyQueue = sortprocesses(readyDict, "PR")
                count += 1
            else:
                time = time + 1
                readyDict[readyQueue[0][0]][1] -= 1
    return outputDict




    
    
if __name__=="__main__":
    fcfsout = fcfs({'A':[1, 3], 'B':[0, 5], 'C':[1, 2], 'D': [3, 1], 'E':[2, 4]})
    print(fcfsout, avg(fcfsout, "TT"), avg(fcfsout, "WT"))
    sjfout = sjf({'A':[1, 3], 'B':[0, 5], 'C':[1, 2], 'D': [3, 1], 'E':[2, 4]})
    print(sjfout, avg(sjfout, "TT"), avg(sjfout, "WT"))
    nprout = prioritynp({'A':[1, 3, 1], 'B':[0, 5, 5], 'C':[1, 2, 4], 'D': [3, 1, 3], 'E':[2, 4, 2]})
    print(nprout, avg(nprout, "TT"), avg(nprout, "WT"))
    # rrout = rr({'A':[0, 5, 1], 'B':[1, 6, 5], 'C':[2, 3, 4], 'D': [3, 1, 3], 'E':[4, 5, 2], 'F':[6, 4, 2]},4)
    # rrout = rr({'A':[0, 5, 1], 'B':[1, 4, 5], 'C':[2, 2, 4], 'D': [4, 1, 3]},2)
    rrout = rr({'A':[1, 3, 1], 'B':[0, 5, 5], 'C':[1, 2, 4], 'D': [3, 1, 3], 'E':[2, 4, 2]},2)
    print(rrout, avg(rrout, "TT"), avg(rrout, "WT"))
    srtfout = srtf({'A':[1, 3], 'B':[0, 5], 'C':[1, 2], 'D': [3, 1], 'E':[2, 4]})
    print(srtfout, avg(srtfout, "TT"), avg(srtfout, "WT"))

    prout = priorityp({'A':[1, 3, 1], 'B':[0, 5, 5], 'C':[1, 2, 4], 'D': [3, 1, 3], 'E':[2, 4, 2]})
    print(prout, avg(prout, "TT"), avg(prout, "WT"))
