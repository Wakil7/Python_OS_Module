class Process:
    def __init__(self):
        self.processDict = {}

    def addProcess(self, pid, at, bt, pr, size):
        if pid in self.processDict.keys() or type(at)!=int or type(bt)!=int or type(pr)!=int:
            return False
        self.processDict.update({pid: [at, bt, pr, size]})
        return True
    
    def addProcesses(self, processList):
        for p in processList:
            try:
                if p[0] in self.processDict.keys():
                    return False
                if type(p[1])!=int or type(p[2])!=int or type(p[3])!=int or type(p[4])!=int:
                    return False
            except:
                return False
        for p in processList:
            self.processDict.update({p[0]: [p[1], p[2], p[3], p[4]]})
        return True

    def updateProcess(self, pid, value, key):
        d = {"AT": 0, "BT": 1, "PR": 2, "SZ": 3}
        if pid not in self.processDict.keys():
            return False
        if key not in d.keys():
            return False
        if type(value)!=int:
            return False
        self.processDict[pid][key] = value
        return True
    
    def getProcessesInfo(self, pid):
        if pid not in self.processDict.keys():
            return False
        return self.processDict[pid]
    
    def getProcesses(self):
        return self.processDict

    def removeProcess(self, pid):
        if pid not in self.processDict.keys():
            return False
        del self.processDict[pid]
        return True
    
    def clearList(self):
        self.processDict.clear()