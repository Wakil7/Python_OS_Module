class Process:
    def __init__(self):
        self.processDict = {}

    def addProcess(self, pid, at, bt, pr=-1):
        if pid in self.processDict.keys() or type(at)!=int or type(bt)!=int or type(pr)!=int:
            return -1
        self.processDict.update({pid: [at, bt, pr]})
        return 0
    
    def addProcesses(self, processList):
        for p in processList:
            try:
                if p[0] in self.processDict.keys():
                    return -1
                if type(p[1])!=int or type(p[2])!=int or type(p[3])!=int:
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
    