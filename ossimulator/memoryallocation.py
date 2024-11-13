import copy

class MemoryAllocator:
    def __init__(self, freeLst):
        self.memory = copy.deepcopy(freeLst)
        self.pointer = 0
    def updateBlocks(self, freeLst):
        self.memory = copy.deepcopy(freeLst)
        self.pointer = 0

    def getMemoryStatus(self):
        return self.memory
    
    def totalFreeMemory(self):
        return sum(self.memory)

    def firstFit(self, processDict):
        processes = copy.deepcopy(processDict)
        allotedDict = {}
        for pid in processes.keys():
            flag = True
            for i, block in enumerate(self.memory):
                if block>=processes[pid]:
                    self.memory[i] -= processes[pid]
                    flag = False
                    allotedDict[pid] = 1
                    break
            if flag:
                allotedDict[pid] = 0
        return allotedDict
    
    def bestFit(self, processDict):
        processes = copy.deepcopy(processDict)
        allotedDict = {}
        for pid in processes.keys():
            m = None
            for i, block in enumerate(self.memory):
                if m==None and block>=processes[pid]:
                    m = block - processes[pid]
                    index = i
                elif block>=processes[pid] and block-processes[pid]<m:
                    m = block - processes[pid] 
                    index = i
            if m==None:
                allotedDict[pid] = 0
            else:
                self.memory[index] = self.memory[index] - processes[pid]
                allotedDict[pid] = 1
        return allotedDict
    
    def worstFit(self, processDict):
        processes = copy.deepcopy(processDict)
        allotedDict = {}
        for pid in processes.keys():
            m = None
            for i, block in enumerate(self.memory):
                if m==None and block>=processes[pid]:
                    m = block - processes[pid]
                    index = i
                elif block>=processes[pid] and block-processes[pid]>m:
                    m = block - processes[pid] 
                    index = i
            if m==None:
                allotedDict[pid] = 0
            else:
                self.memory[index] = self.memory[index] - processes[pid]
                allotedDict[pid] = 1
        return allotedDict
    
    def nextFit(self, processDict):
        processes = copy.deepcopy(processDict)
        allotedDict = {}
        size = len(self.memory)
        for pid in processes.keys():
            prevIndex = (self.pointer + size - 1) % size
            flag = True
            while self.pointer!=prevIndex:
                if self.memory[self.pointer]>=processes[pid]:
                    self.memory[self.pointer] -= processes[pid]
                    allotedDict[pid] = 1
                    flag = False
                    break
                else:
                    self.pointer = (self.pointer + 1) % size
            if self.memory[self.pointer]>=processes[pid]:
                self.memory[self.pointer] -= processes[pid]
                allotedDict[pid] = 1
                flag = False
            if flag:
                allotedDict[pid] = 0
        return allotedDict
    