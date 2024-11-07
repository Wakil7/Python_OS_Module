class CpuScheduler:
    def __init__(self):
        self.processDict = {}

    def addProcess(self, pid, at, bt, pr=-1):
        if pid in self.processDict.keys():
            return -1
        self.processDict.update({pid: [at, bt, pr]})
        return 0
    
    def addProcesses(self, processList):
        for p in processList:
            try:
                if p[0] in self.processDict.keys():
                    return -1
                if type(p[0])!=int or type(p[1])!=int or type(p[2])!=int or type(p[3])!=int:
                    return -1
            except:
                return -1
        
        for p in processList:
            self.processDict.update({p[0]: [p[1], p[2], p[3]]})
        return 0

    def updateProcess(self, pid, value, key):
        d = {"AT": 0, "BT": 1, "PR": 2}
        if pid not in self.processDict.keys():
            return -1
        
        if key not in d.keys():
            return -1
        
        if type(value)!=int:
            return -1
        
        self.processDict[pid][key] = value
        return 0
    
    def removeProcess(self, pid):
        if pid not in self.processDict.keys():
            return -1
        
        del self.processDict[pid]
        return 0
    
    def clearList(self):
        self.processDict.clear()
    
    def sorted(self, pDict, key=""):
        processes = {x[0]:x[1] for x in pDict.items()}
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

    def avg(self, pDict, key):
        processes = {x[0]:x[1] for x in pDict.items()}
        d = {"TT": 1, "WT": 2}
        if key not in d:
            return -1
        index = d[key]

        s = sum(list(map(lambda x: x[index], processes.values())))

        avg = s/len(processes)
        return avg


    def fcfs(self):
        processes = {x[0]:x[1] for x in self.processDict.items()}
        readyQueue = self.sorted(processes, key="AT")
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

    def sjf(self):
        processes = {x[0]:x[1] for x in self.processDict.items()}
        n = len(processes)
        time = 0
        count = 0
        readyDict = {}
        outputDict = {}
        completedList = []
        while count<n:
            readyDict.update(dict(filter(lambda p: p[0] not in completedList and p[1][0]<=time, processes.items())))
    
            readyQueue = self.sorted(readyDict, "BT")
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

    def prioritynp(self):
        processes = {x[0]:x[1] for x in self.processDict.items()}
        n = len(processes)
        time = 0
        count = 0
        readyDict = {}
        outputDict = {}
        completedList = []
        while count<n:
            readyDict.update(dict(filter(lambda p: p[0] not in completedList and p[1][0]<=time, processes.items())))
    
            readyQueue = self.sorted(readyDict, "PR")
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

    def rr(self, quantum=1):
        processes = {x[0]:x[1] for x in self.processDict.items()}
        n = len(processes)
        time = 0
        count = 0
        outputDict = {}
        sortedList = self.sorted(processes, key="AT")
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
                btList[0]-= quantum
                time += quantum
                flag = True
                
            else:
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


    def srtf(self):
        processes = {x[0]:x[1] for x in self.processDict.items()}
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

            if arrived:
                readyQueue = self.sorted(readyDict, "BT")
                arrived = False
            if readyQueue == []:
                time = time + 1
            else:
                if readyDict[readyQueue[0][0]][1] == 1:
                    time = time + 1
                    tt = time - readyQueue[0][1]
                    wt = tt - self.processDict[readyQueue[0][0]][1]
                    outputDict[readyQueue[0][0]] = [time, tt, wt]
                    del readyDict[readyQueue[0][0]]
                    readyQueue = self.sorted(readyDict, "BT")
                    count += 1
                else:
                    time = time + 1
                    readyDict[readyQueue[0][0]][1] -= 1
        return outputDict

    def priorityp(self):
        processes = {x[0]:x[1] for x in self.processDict.items()}
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

            if arrived:
                readyQueue = self.sorted(readyDict, "PR")
                arrived = False
            if readyQueue == []:
                time = time + 1
            else:
                if readyDict[readyQueue[0][0]][1] == 1:
                    time = time + 1
                    tt = time - readyQueue[0][1]
                    wt = tt - self.processDict[readyQueue[0][0]][1]
                    outputDict[readyQueue[0][0]] = [time, tt, wt]
                    del readyDict[readyQueue[0][0]]
                    readyQueue = self.sorted(readyDict, "PR")
                    count += 1
                else:
                    time = time + 1
                    readyDict[readyQueue[0][0]][1] -= 1
        return outputDict
    
class DiskScheduler:
    def __init__(self, n):
        self.requests = []
        self.size = n
    
    def addRequest(self, req):
        if type(req)!=int:
            return -1
        if req<0 or req>=self.size:
            return -1
        
        self.requests.append(req)
        return 0
    
    def addRequests(self, lst):
        for req in lst:
            if type(req)!=int:
                return -1
            if req<0 or req>=self.size:
                return -1
        
        self.requests.extend(lst)
    
    def removeRequest(self, req):
        if req in self.requests:
            self.requests.remove(req)
    
    def seek(self, start, near = False, lst=[]):
        head = start
        if lst==[]:
            reqLst = sorted(self.requests)
        else:
            reqLst = sorted(lst)
        if head<=reqLst[0]:
            movement = abs(head-reqLst[0])
            head = reqLst[0]
            index = 0
        elif head>=reqLst[-1]:
            movement = abs(head-reqLst[-1])
            head = reqLst[-1]
            index = len(reqLst)-1
        else:
            for i in range(1, len(reqLst)):
                if reqLst[i-1]<=head<=reqLst[i]:
                    if near:
                        if abs(reqLst[i-1]-head)<abs(reqLst[i]-head):
                            movement = abs(head-reqLst[i-1])
                            head = reqLst[i-1]
                            index = i-1
                        else:
                            movement = abs(head-reqLst[i])
                            head = reqLst[i]
                            index = i
                        return head, movement, index
                    movement = abs(head-reqLst[i-1])
                    head = reqLst[i-1]
                    index = i-1
                    break
        return head, movement, index


    def fcfs(self, start):
        head = start
        if head>=self.size or head<0:
            return -1
        movement = 0
        for r in self.requests:
            if (r>=self.size or r<0):
                return -1
            movement += abs(head-r)
            head = r
        return self.requests, movement

    def sstf(self, start):
        reqLst = sorted(self.requests)
        head = start
        outList = []
        movement = 0
        if head>=self.size or head<0:
            return -1

        while len(reqLst)!=0:
            head, mov, index = self.seek(head, near = True, lst=reqLst)
            movement += mov
            outList.append(reqLst[index])
            reqLst.pop(index)
        
        return outList, movement


    def scan(self, start):
        head = start
        reqLst = sorted(self.requests)
        outList = []
        if head>=self.size or head<0:
            return -1

        head, movement, index = self.seek(start)
        
        oldind = index
        while index>=0:
            r = reqLst[index]
            movement += abs(head-r)
            head = r
            outList.append(r)
            index -= 1

        movement += head
        head = 0
        index = oldind + 1
        while index<len(reqLst):
            r = reqLst[index]
            movement += abs(head-r)
            head = r
            outList.append(r)
            index += 1
        
        return outList, movement

    def cscan(self, start):
        head = start
        reqLst = sorted(self.requests)
        outList = []
        if head>=self.size or head<0:
            return -1
        head, movement, index = self.seek(start)
        outList.append(reqLst[index])
        oldind = index
        while index>0:
            index -= 1
            r = reqLst[index]
            movement += abs(head-r)
            head = r
            outList.append(r)
        movement += head
        head = self.size-1
        movement += head
        
        head, mov, index = self.seek(head)
        movement += mov

        while index>oldind:
            r = reqLst[index]
            movement += abs(head-r)
            head = r
            outList.append(r)
            index -= 1
        
        return outList, movement

    def look(self, start):
        head = start
        reqLst = sorted(self.requests)
        outList = []
        if head>=self.size or head<0:
            return -1

        head, movement, index = self.seek(start)
        
        oldind = index
        while index>=0:
            r = reqLst[index]
            movement += abs(head-r)
            head = r
            outList.append(r)
            index -= 1

        index = oldind + 1

        while index<len(reqLst):
            r = reqLst[index]
            movement += abs(head-r)
            head = r
            outList.append(r)
            index += 1
        
        return outList, movement


    def clook(self, start):
        head = start
        reqLst = sorted(self.requests)
        outList = []
        if head>=self.size or head<0:
            return -1
        head, movement, index = self.seek(start)
        outList.append(reqLst[index])
        oldind = index
        while index>0:
            index -= 1
            r = reqLst[index]
            movement += abs(head-r)
            head = r
            outList.append(r)
        
        index = len(reqLst)-1
        

        while index>oldind:
            r = reqLst[index]
            movement += abs(head-r)
            head = r
            outList.append(r)
            index -= 1
        
        return outList, movement
