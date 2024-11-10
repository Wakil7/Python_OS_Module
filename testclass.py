import copy
class MemoryAllocation:
    def __init__(self, freeLst):
        self.memory = freeLst

    def updateBlocks(self, freeLst):
        self.memory = freeLst

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

if __name__=="__main__":
    memoryStatus = [100, 320, 500, 200, 300, 600]
    processDict = {
        1000: 212,
        1001: 98,
        1002: 417,
        1003: 112,
        1004: 426
    }
    ma = MemoryAllocation(memoryStatus)
    allocated = ma.firstFit(processDict)
    print(allocated)
    print(ma.getMemoryStatus())
    print(ma.totalFreeMemory())
    