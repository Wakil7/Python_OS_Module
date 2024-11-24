import copy
from collections import namedtuple

class MemoryAllocator:
    def __init__(self):
        self.pointer = 0

    def firstFit(self, processObj, memoryObj):
        Output = namedtuple("Output", ["name", "visualdata", "result"])
        processes = {x[0]: x[1][3] for x in processObj.processDict.items()}
        newMemory = copy.deepcopy(memoryObj.mainMemory)
        allotedDict = {}
        for pid in processes.keys():
            flag = True
            tmpMemory = copy.deepcopy(newMemory)
            for i, block in enumerate(tmpMemory):
                if type(block)!=tuple:
                    if block>=processes[pid]:
                        newMemory[i] = (pid, processes[pid])
                        self.pointer = i + 1
                        if block!=processes[pid]:
                            newMemory.insert(i+1, block-processes[pid])
                        flag = False
                        allotedDict[pid] = 1
                        break
            if flag:
                allotedDict[pid] = 0
        memoryObj.mainMemory = [x for x in newMemory if type(x)!=tuple]
    
        output = Output("First Fit", newMemory, allotedDict)
        return output
    
    def bestFit(self, processObj, memoryObj):
        Output = namedtuple("Output", ["name", "visualdata", "result"])
        processes = {x[0]: x[1][3] for x in processObj.processDict.items()}
        newMemory = copy.deepcopy(memoryObj.mainMemory)
        allotedDict = {}
        for pid in processes.keys():
            m = None
            tmpMemory = copy.deepcopy(newMemory)
            for i, block in enumerate(tmpMemory):
                if type(block)!=tuple:
                    if m==None and block>=processes[pid]:
                        m = block - processes[pid]
                        index = i
                    elif block>=processes[pid] and block-processes[pid]<m:
                        m = block - processes[pid] 
                        index = i
            if m==None:
                allotedDict[pid] = 0
            else:
                tmp = newMemory[index]
                newMemory[index] = (pid, processes[pid])
                self.pointer = index + 1
                if tmp!=processes[pid]:
                    newMemory.insert(index+1, tmp-processes[pid])
                allotedDict[pid] = 1
        memoryObj.mainMemory = [x for x in newMemory if type(x)!=tuple]
    
        output = Output("Best Fit", newMemory, allotedDict)
        return output
    
    def worstFit(self, processObj, memoryObj):
        Output = namedtuple("Output", ["name", "visualdata", "result"])
        processes = {x[0]: x[1][3] for x in processObj.processDict.items()}
        newMemory = copy.deepcopy(memoryObj.mainMemory)
        allotedDict = {}
        for pid in processes.keys():
            m = None
            tmpMemory = copy.deepcopy(newMemory)
            for i, block in enumerate(tmpMemory):
                if type(block)!=tuple:
                    if m==None and block>=processes[pid]:
                        m = block - processes[pid]
                        index = i
                    elif block>=processes[pid] and block-processes[pid]>m:
                        m = block - processes[pid] 
                        index = i
            if m==None:
                allotedDict[pid] = 0
            else:
                tmp = newMemory[index]
                newMemory[index] = (pid, processes[pid])
                self.pointer = index + 1
                if tmp!=processes[pid]:
                    newMemory.insert(index+1, tmp-processes[pid])
                allotedDict[pid] = 1
        memoryObj.mainMemory = [x for x in newMemory if type(x)!=tuple]
    
        output = Output("Worst Fit", newMemory, allotedDict)
        return output
    
    def nextFit(self, processObj, memoryObj):
        Output = namedtuple("Output", ["name", "visualdata", "result"])
        processes = {x[0]: x[1][3] for x in processObj.processDict.items()}
        newMemory = copy.deepcopy(memoryObj.mainMemory)
        allotedDict = {}
        n = len(newMemory)
        for pid in processes.keys():
            prevIndex = (self.pointer + n - 1) % n
            flag = True
            while self.pointer!=prevIndex:

                if type(newMemory[self.pointer])==int and newMemory[self.pointer]>=processes[pid]:
                    tmp = newMemory[self.pointer]
                    newMemory[self.pointer] = (pid, processes[pid])
                    self.pointer = self.pointer + 1
                    if tmp!=processes[pid]:
                        newMemory.insert(self.pointer, tmp-processes[pid])
                        n += 1
                    allotedDict[pid] = 1
                    flag = False
                    break
                else:
                    self.pointer = (self.pointer + 1) % n
            if type(newMemory[self.pointer])==int and newMemory[self.pointer]>=processes[pid] and flag:
                tmp = newMemory[self.pointer]
                newMemory[self.pointer] = (pid, processes[pid])
                self.pointer = self.pointer + 1
                if tmp!=processes[pid]:
                    newMemory.insert(self.pointer, tmp-processes[pid])
                    n += 1
                allotedDict[pid] = 1
                flag = False
            if flag:
                allotedDict[pid] = 0

        memoryObj.mainMemory = [x for x in newMemory if type(x)!=tuple]
        output = Output("Next Fit", newMemory, allotedDict)
        return output