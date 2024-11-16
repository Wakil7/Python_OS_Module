# {pid: [ArrivalTime, BurstTime, Priority]}
# {pid: [CompletionTime, TurnaroundTime, WaitingTime]}

import copy
from collections import namedtuple

class CpuScheduler:
    
    def sorted(self, pDict, key=""):
        processes = copy.deepcopy(pDict)
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

    def avg(self, data, key):
        processes = copy.deepcopy(data.result)
        d = {"TT": 1, "WT": 2}
        if key not in d:
            return -1
        index = d[key]

        s = sum(list(map(lambda x: x[index], processes.values())))

        avg = s/len(processes)
        return avg


    def fcfs(self, tasks):
        Output = namedtuple("Output", ["name", "chartdata", "result"])
        processes = copy.deepcopy(tasks.processDict)
        readyQueue = self.sorted(processes, key="AT")
        resultDict = {}
        chartLst = []
        time = 0
        idle = 0
        for process in readyQueue:
            while time<process[1]:
                time += 1
                idle+=1
            if idle!=0:
                if chartLst!=[]:
                    idle += chartLst[-1][1]
                chartLst.append(("Idle", idle))
                idle = 0
            time += process[2]
            tt = time-process[1]
            wt = tt-process[2]
            resultDict[process[0]] = [time, tt, wt]
            chartLst.append((process[0], time))
        output = Output("FCFS", chartLst, resultDict)
        return output

    def sjf(self, tasks):
        Output = namedtuple("Output", ["name", "chartdata", "result"])
        processes = copy.deepcopy(tasks.processDict)
        n = len(processes)
        time = 0
        count = 0
        idle=0
        readyDict = {}
        resultDict = {}
        completedList = []
        chartLst = []
        while count<n:
            readyDict.update(dict(filter(lambda p: p[0] not in completedList and p[1][0]<=time, processes.items())))
    
            readyQueue = self.sorted(readyDict, "BT")
            if readyQueue == []:
                time = time + 1
                idle += 1
            else:
                if idle!=0:
                    if chartLst!=[]:
                        idle += chartLst[-1][1]
                    chartLst.append(("Idle", idle))
                    idle = 0
                time = time + readyQueue[0][2]
                tt = time-readyQueue[0][1]
                wt = tt-readyQueue[0][2]
                completedList.append(readyQueue[0][0])
                resultDict[readyQueue[0][0]] = [time, tt, wt]
                chartLst.append((readyQueue[0][0], time))
                del readyDict[readyQueue[0][0]]
                count += 1
        output = Output("SJF", chartLst, resultDict)
        return output

    def prioritynp(self, tasks):
        Output = namedtuple("Output", ["name", "chartdata", "result"])
        processes = copy.deepcopy(tasks.processDict)
        n = len(processes)
        time = 0
        count = 0
        idle = 0
        readyDict = {}
        resultDict = {}
        completedList = []
        chartLst = []
        while count<n:
            readyDict.update(dict(filter(lambda p: p[0] not in completedList and p[1][0]<=time, processes.items())))
    
            readyQueue = self.sorted(readyDict, "PR")
            if readyQueue == []:
                time = time + 1
                idle+=1
            else:
                if idle!=0:
                    if chartLst!=[]:
                        idle += chartLst[-1][1]
                    chartLst.append(("Idle", idle))
                    idle = 0
                time = time + readyQueue[0][2]
                tt = time-readyQueue[0][1]
                wt = tt-readyQueue[0][2]
                completedList.append(readyQueue[0][0])
                resultDict[readyQueue[0][0]] = [time, tt, wt]
                chartLst.append((readyQueue[0][0], time))
                del readyDict[readyQueue[0][0]]
                count += 1
        output = Output("Non-Preemptive Priority", chartLst, resultDict)
        return output

    def rr(self, tasks, quantum=1):
        Output = namedtuple("Output", ["name", "chartdata", "result"])
        processes = copy.deepcopy(tasks.processDict)
        n = len(processes)
        time = 0
        count = 0
        idle=0
        resultDict = {}
        sortedList = self.sorted(processes, key="AT")
        readyQueue = []
        chartLst = []
        btList = []
        flag = True
        while count<n:
            if sortedList!=[] and readyQueue==[]:
                while time<sortedList[0][1] and readyQueue==[]:
                    time += 1
                    idle+=1
                while sortedList!=[] and sortedList[0][1]==time:
                    if idle!=0:
                        if chartLst!=[]:
                            idle+=chartLst[-1][1]
                        chartLst.append(("Idle", idle))
                        idle=0
                    readyQueue.append(sortedList[0])
                    btList.append(sortedList[0][2])
                    sortedList.pop(0)

            if btList[0]>quantum:
                btList[0]-= quantum
                time += quantum
                chartLst.append((readyQueue[0][0], time))
                flag = True
                
            else:
                time += btList[0]
                tt = time - readyQueue[0][1]
                wt = tt - readyQueue[0][2]
                resultDict[readyQueue[0][0]] = [time, tt, wt]
                chartLst.append((readyQueue[0][0], time))
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
        output = Output("Round Robin", chartLst, resultDict)
        return output


    def srtf(self, tasks):
        Output = namedtuple("Output", ["name", "chartdata", "result"])
        processes = copy.deepcopy(tasks.processDict)
        n = len(processes)
        time = 0
        count = 0
        idle=0
        readyDict = {}
        resultDict = {}
        arrivedList = []
        readyQueue=[]
        chartLst = []
        currProcess = None
        arrived=False
        while count<n:
            tempDict = dict(filter(lambda p: p[0] not in arrivedList and p[1][0]==time, processes.items()))
            
            arrived = (tempDict!={})
            arrivedList.extend([p for p in tempDict.keys()])
            readyDict.update(tempDict)

            if arrived:
                readyQueue = self.sorted(readyDict, "BT")
                arrived = False
                if currProcess==None:
                    currProcess=readyQueue[0][0]
            if readyQueue == []:
                time = time + 1
                idle+=1
            else:
                if idle!=0:
                    if chartLst!=[]:
                        idle+=chartLst[-1][1]
                    chartLst.append(("Idle", idle))
                    idle=0
                if readyDict[readyQueue[0][0]][1] == 1:
                    time = time + 1
                    tt = time - readyQueue[0][1]
                    wt = tt - tasks.processDict[readyQueue[0][0]][1]
                    resultDict[readyQueue[0][0]] = [time, tt, wt]
                    chartLst.append((readyQueue[0][0], time))
                    del readyDict[readyQueue[0][0]]
                    readyQueue = self.sorted(readyDict, "BT")
                    count += 1
                else:
                    if currProcess in readyDict.keys() and currProcess!=readyQueue[0][0]:
                        chartLst.append((currProcess, time))
                        currProcess = readyQueue[0][0]
                    time = time + 1
                    readyDict[readyQueue[0][0]][1] -= 1
        output = Output("SRTF", chartLst, resultDict)   
        return output

    def priorityp(self, tasks):
        Output = namedtuple("Output", ["name", "chartdata", "result"])
        processes = copy.deepcopy(tasks.processDict)
        n = len(processes)
        time = 0
        count = 0
        idle = 0
        readyDict = {}
        resultDict = {}
        arrivedList = []
        readyQueue=[]
        chartLst = []
        arrived=False
        currProcess=None
        while count<n:
            tempDict = dict(filter(lambda p: p[0] not in arrivedList and p[1][0]==time, processes.items()))
            arrived = (tempDict!={})
            arrivedList.extend([p for p in tempDict.keys()])
            readyDict.update(tempDict)

            if arrived:
                readyQueue = self.sorted(readyDict, "PR")
                arrived = False
                if currProcess==None:
                    currProcess=readyQueue[0][0]
                arrived = False
            if readyQueue == []:
                time = time + 1
                idle+=1
            else:
                if idle!=0:
                    if chartLst!=[]:
                        idle+=chartLst[-1][1]
                    chartLst.append(("Idle", idle))
                    idle=0
                if readyDict[readyQueue[0][0]][1] == 1:
                    time = time + 1
                    tt = time - readyQueue[0][1]
                    wt = tt - tasks.processDict[readyQueue[0][0]][1]
                    resultDict[readyQueue[0][0]] = [time, tt, wt]
                    chartLst.append((readyQueue[0][0], time))
                    del readyDict[readyQueue[0][0]]
                    readyQueue = self.sorted(readyDict, "PR")
                    count += 1
                else:
                    if currProcess in readyDict.keys() and currProcess!=readyQueue[0][0]:
                        chartLst.append((currProcess, time))
                        currProcess = readyQueue[0][0]
                    time = time + 1
                    readyDict[readyQueue[0][0]][1] -= 1
        output = Output("Preemptive Priority", chartLst, resultDict)   
        return output