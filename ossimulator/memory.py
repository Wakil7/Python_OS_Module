import copy
class Memory:
    def __init__(self, mainSize, frameSize):
        self.mainMemory = []
        self.frames = [None]*frameSize
        self.mainSize = mainSize
        self.frameSize = frameSize

    def setMainMemory(self, n, freeLst):
        if n<sum(freeLst):
            return False
        self.mainMemory = copy.deepcopy(freeLst)
        self.size = n
        return True
    
    def setFrames(self, lst):
        if len(lst)!=self.frameSize:
            return False
        self.frames = copy.deepcopy(lst)

    def clearFrames(self):
        self.frames = [None]*self.frameSize

    def getMainMemoryStatus(self):
        return self.mainMemory
    
    def getFrameStatus(self):
        return self.frames
    
    def totalFreeMemory(self):
        return sum(self.mainMemory)
    
    def totalOccupiedMemory(self):
        return self.size - sum(self.mainMemory)