# Processes List Structure
# {ProcessName/ProcessId: [ArrivalTime, BurstTime, Priority]}
# [ProcessName/ProcessId, ArrivalTime, BurstTime, Priority]

def sortprocesses(processes, key=""):
    sortedList = []
    for process in processes:
        tmpProcess = [process]
        for p in processes[process]:
            tmpProcess.append(p)
        sortedList.append(tmpProcess)
    if key=="AT":
        index = 1
    elif key=="BT":
        index = 2
    elif key=="PR":
        index = 3
    else:
        index = 0
    n = len(sortedList)
    for i in range(1, n):
        swapped = False
        for j in range(0, n-i):
            if sortedList[j][index]>sortedList[j+1][index]:
                tmp = sortedList[j]
                sortedList[j] = sortedList[j+1]
                sortedList[j+1] = tmp
                swapped = True
        if not(swapped):
            break
    return sortedList



# def sortperfect(processes, key="AT"):
#     sortedList = []
#     time = 0
#     lastAt = 0
#     n = len(processes)
#     count = 0
#     for process in processes:
#         if processes[process][0]>lastAt:
#             lastAt = processes[process][0]
#     while count<n:
#         newList = []
#         for process in processes:
#             if processes[process][0]<=time:
#                 tmpList = [process]
#                 tmpList.extend(processes[process])
#                 count = count + 1
#                 if processes[process][1] > time:
#                     time = processes[process][1]
#     pass

def avg(processes, key):
    s = 0
    count = 0
    if key=="TT":
        index = 1
    if key=="WT":
        index = 2
    for process in processes:
        s += processes[process][index]
        count += 1
    avg = s/count
    return avg


    
        
        
            
                
    

def fcfs(processes):
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

def sjf(processes):
    n = len(processes)
    time = 0
    count = 0
    readyDict = {}
    outputDict = {}
    completedList = []
    while count<n:
        for process in processes:
            if processes[process][0]<=time:
                if process not in completedList:
                    readyDict[process] = processes[process]
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

def prioritynp(processes):
    n = len(processes)
    time = 0
    count = 0
    readyDict = {}
    outputDict = {}
    completedList = []
    while count<n:
        for process in processes:
            if processes[process][0]<=time:
                if process not in completedList:
                    readyDict[process] = processes[process]
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

def rr(processes, quantum=1):
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
            print(readyQueue[0])
            btList[0]-= quantum
            time += quantum
            flag = True
            
        else:
            print(readyQueue[0])
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
        # if sortedList!=[] and readyQueue==[0]*len(readyQueue):
        #     while time<sortedList[0][1] and readyQueue==[0]*len(readyQueue):
        #         time += 1
        #     while sortedList!=[] and sortedList[0][1]==time:
        #         readyQueue.append(sortedList[0])
        #         btList.append(sortedList[0][2])
        #         sortedList.pop(0)
        # if readyQueue[index]!=0:
        #     if btList[index]>quantum:
        #         print(readyQueue[index])
        #         btList[index]-= quantum
        #         time += quantum
                
        #     else:
        #         print(readyQueue[index])
        #         time += btList[index]
        #         tt = time - readyQueue[index][1]
        #         wt = tt - readyQueue[index][2]
        #         outputDict[readyQueue[index][0]] = [time, tt, wt]
        #         readyQueue[index] = 0
        #         count += 1

        # while sortedList!=[] and sortedList[0][1]<=time:
        #         readyQueue.append(sortedList[0])
        #         btList.append(sortedList[0][2])
        #         sortedList.pop(0)
        # index = (index + 1) % len(readyQueue)

        
        # index = (index + 1) % len(readyQueue)

        # if readyQueue != []:
        #     currProcess = readyQueue[0]
        #     readyQueue.pop(0)
        #     readyQueue.append(currProcess)
    return outputDict

        
        

        


    
    

fcfsout = fcfs({'A':[1, 3], 'B':[0, 5], 'C':[1, 2], 'D': [3, 1], 'E':[2, 4]})
print(fcfsout, avg(fcfsout, "TT"), avg(fcfsout, "WT"))
sjfout = sjf({'A':[1, 3], 'B':[0, 5], 'C':[1, 2], 'D': [3, 1], 'E':[2, 4]})
print(sjfout, avg(sjfout, "TT"), avg(sjfout, "WT"))
prout = prioritynp({'A':[1, 3, 1], 'B':[0, 5, 5], 'C':[1, 2, 4], 'D': [3, 1, 3], 'E':[2, 4, 2]})
print(prout, avg(prout, "TT"), avg(sjfout, "WT"))
# rrout = rr({'A':[0, 5, 1], 'B':[1, 6, 5], 'C':[2, 3, 4], 'D': [3, 1, 3], 'E':[4, 5, 2], 'F':[6, 4, 2]},4)
# rrout = rr({'A':[0, 5, 1], 'B':[1, 4, 5], 'C':[2, 2, 4], 'D': [4, 1, 3]},2)
rrout = rr({'A':[1, 3, 1], 'B':[0, 5, 5], 'C':[1, 2, 4], 'D': [3, 1, 3], 'E':[2, 4, 2]},2)
print(rrout, avg(rrout, "TT"), avg(rrout, "WT"))
