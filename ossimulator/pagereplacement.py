import random
import copy
from collections import namedtuple
class PageReplacer:
    def __init__(self, n):
        self.size = n
        self.frames = [None]*n

    def clearFrames(self):
        self.frames = [None]*self.size

    def rand(self, requests):
        Output = namedtuple("Output", ["name", "chartdata", "hits"])
        chartLst = [] #[self.frames, req, {"H":index, "R":index}]
        hit = 0
        for req in requests:
            if req in self.frames:
                hit+=1
                chartLst.append([copy.deepcopy(self.frames), req, {"H": self.frames.index(req)}])
            else:
                flag = True
                for i in range(self.size):
                    if self.frames[i]==None:
                        self.frames[i] = req
                        chartLst.append([copy.deepcopy(self.frames), req, {}])
                        flag = False
                        break
                if flag:
                    x = random.randint(0, self.size-1)
                    tmpDict = copy.deepcopy(chartLst[-1][2])
                    tmpDict["R"] = x
                    chartLst[-1] = [copy.deepcopy(self.frames), chartLst[-1][1], tmpDict]
                    self.frames[x] = req
                    chartLst.append([copy.deepcopy(self.frames), req, {}])
        output = Output("Random Page Replacement", chartLst, hit)
        return output
    
    def fifo(self, requests):
        Output = namedtuple("Output", ["name", "chartdata", "hits"])
        chartLst = [] 
        index = 0
        hit = 0
        for req in requests:
            if req in self.frames:
                hit+=1
                chartLst.append([copy.deepcopy(self.frames), req, {"H": self.frames.index(req)}])
            else:
                flag = True
                for i in range(self.size):
                    if self.frames[i]==None:
                        self.frames[i] = req
                        index = (i + 1) % self.size
                        chartLst.append([copy.deepcopy(self.frames), req, {}])
                        flag = False
                        break
                if flag:
                    tmpDict = copy.deepcopy(chartLst[-1][2])
                    tmpDict["R"] = index
                    chartLst[-1] = [copy.deepcopy(self.frames), chartLst[-1][1], tmpDict]
                    self.frames[index] = req
                    chartLst.append([copy.deepcopy(self.frames), req, {}])
                    index = (index + 1) % self.size
        output = Output("FIFO Page Replacement", chartLst, hit)
        return output
    
    def lru(self, requests):
        Output = namedtuple("Output", ["name", "chartdata", "hits"])
        chartLst = [] 
        usedDict = {x:1 for x in self.frames if x is not None}
        hit = 0
        for req in requests:
            usedDict = dict(map(lambda x: [x[0], x[1]+1], usedDict.items()))
            if req in self.frames:
                hit += 1
                chartLst.append([copy.deepcopy(self.frames), req, {"H": self.frames.index(req)}])
                usedDict[req] = 1
            else:
                flag=True
                for i in range(self.size):
                    if self.frames[i] == None:
                        self.frames[i] = req
                        usedDict[req] = 1
                        chartLst.append([copy.deepcopy(self.frames), req, {}])
                        flag=False
                        break
                        
                if flag:
                    m = 0
                    for k in usedDict.keys():
                        if usedDict[k]>m:
                            m = usedDict[k]
                            page = k
                    
                    del usedDict[page]
                    x = self.frames.index(page)
                    tmpDict = copy.deepcopy(chartLst[-1][2])
                    tmpDict["R"] = x
                    chartLst[-1] = [copy.deepcopy(self.frames), chartLst[-1][1], tmpDict]
                    self.frames[x] = req
                    chartLst.append([copy.deepcopy(self.frames), req, {}])
                    usedDict[req] = 1
        output = Output("LRU Page Replacement", chartLst, hit)
        return output
    
    def mru(self, requests):
        Output = namedtuple("Output", ["name", "chartdata", "hits"])
        chartLst = [] 
        usedDict = {x:1 for x in self.frames if x is not None}
        hit = 0
        for req in requests:
            usedDict = dict(map(lambda x: [x[0], x[1]+1], usedDict.items()))
            if req in self.frames:
                hit += 1
                chartLst.append([copy.deepcopy(self.frames), req, {"H": self.frames.index(req)}])
                usedDict[req] = 1
            else:
                flag=True
                for i in range(self.size):
                    if self.frames[i] == None:
                        self.frames[i] = req
                        usedDict[req] = 1
                        chartLst.append([copy.deepcopy(self.frames), req, {}])
                        flag=False
                        break
                        
                if flag:
                    m = None
                    for k in usedDict.keys():
                        if m == None or usedDict[k]<m:
                            m = usedDict[k]
                            page = k
                    
                    del usedDict[page]
                    x = self.frames.index(page)
                    tmpDict = copy.deepcopy(chartLst[-1][2])
                    tmpDict["R"] = x
                    chartLst[-1] = [copy.deepcopy(self.frames), chartLst[-1][1], tmpDict]
                    self.frames[x] = req
                    chartLst.append([copy.deepcopy(self.frames), req, {}])
                    usedDict[req] = 1
        output = Output("MRU Page Replacement", chartLst, hit)
        return output
    
    def lfu(self, requests):
        Output = namedtuple("Output", ["name", "chartdata", "hits"])
        chartLst = [] 
        hit = 0
        hitDict = {x:0 for x in self.frames if x is not None}
        for req in requests:
            if req in self.frames:
                hit += 1
                chartLst.append([copy.deepcopy(self.frames), req, {"H": self.frames.index(req)}])
                hitDict[req] += 1
            else:
                flag = True
                for i in range(self.size):
                    if self.frames[i]==None:
                        self.frames[i] = req
                        hitDict[req] = 0
                        chartLst.append([copy.deepcopy(self.frames), req, {}])
                        flag = False
                        break
                if flag:
                    m = None
                    tempDict = dict(filter(lambda x: True if x[0] in self.frames else False, hitDict.items()))
                    for k in tempDict.keys():
                        if m==None or tempDict[k]<m:
                            m = tempDict[k]
                            page = k
                    
                    x = self.frames.index(page)
                    tmpDict = copy.deepcopy(chartLst[-1][2])
                    tmpDict["R"] = x
                    chartLst[-1] = [copy.deepcopy(self.frames), chartLst[-1][1], tmpDict]
                    self.frames[x] = req
                    chartLst.append([copy.deepcopy(self.frames), req, {}])
                    if req in hitDict.keys():
                        hitDict[req]+=1
                    else:
                        hitDict[req]=0
                        
        output = Output("LFU Page Replacement", chartLst, hit)
        return output
    
    def mfu(self, requests):
        Output = namedtuple("Output", ["name", "chartdata", "hits"])
        chartLst = [] 
        hit = 0
        hitDict = {x:0 for x in self.frames if x is not None}
        for req in requests:
            if req in self.frames:
                hit += 1
                chartLst.append([copy.deepcopy(self.frames), req, {"H": self.frames.index(req)}])
                hitDict[req] += 1
            else:
                flag = True
                for i in range(self.size):
                    if self.frames[i]==None:
                        self.frames[i] = req
                        hitDict[req] = 0
                        chartLst.append([copy.deepcopy(self.frames), req, {}])
                        flag = False
                        break
                if flag:
                    m = None
                    tempDict = dict(filter(lambda x: True if x[0] in self.frames else False, hitDict.items()))
                    for k in tempDict.keys():
                        if m==None or tempDict[k]>m:
                            m = tempDict[k]
                            page = k
                    
                    x = self.frames.index(page)
                    tmpDict = copy.deepcopy(chartLst[-1][2])
                    tmpDict["R"] = x
                    chartLst[-1] = [copy.deepcopy(self.frames), chartLst[-1][1], tmpDict]
                    self.frames[x] = req
                    chartLst.append([copy.deepcopy(self.frames), req, {}])
                    if req in hitDict.keys():
                        hitDict[req]+=1
                    else:
                        hitDict[req]=0
                        
        output = Output("MFU Page Replacement", chartLst, hit)
        return output
    
    def clock(self, requests):
        Output = namedtuple("Output", ["name", "chartdata", "hits"])
        chartLst = [] 
        useBitDict = {x:1 for x in self.frames if x is not None}
        hit = 0
        index = 0
        for req in requests:
            if req in self.frames:
                hit += 1
                chartLst.append([copy.deepcopy(self.frames), req, {"H": self.frames.index(req)}])
                useBitDict[req] = 1
            else:
                flag = True
                for i in range(self.size):
                    if self.frames[i]==None:
                        self.frames[i]=req
                        useBitDict[req] = 1
                        index = (i + 1) % self.size
                        chartLst.append([copy.deepcopy(self.frames), req, {}])
                        flag = False
                        break
                if flag:
                    while (useBitDict[self.frames[index]]!=0):
                        useBitDict[self.frames[index]] = 0
                        index = (index + 1) % self.size

                    del useBitDict[self.frames[index]]
                    
                    tmpDict = copy.deepcopy(chartLst[-1][2])
                    tmpDict["R"] = index
                    chartLst[-1] = [copy.deepcopy(self.frames), chartLst[-1][1], tmpDict]
                    self.frames[index] = req
                    chartLst.append([copy.deepcopy(self.frames), req, {}])
                    index = (index + 1) % self.size
                    useBitDict[req]=1
        output = Output("Clock Page Replacement", chartLst, hit)
        return output
    
    def optimal(self, requests):
        Output = namedtuple("Output", ["name", "chartdata", "hits"])
        chartLst = [] 
        hit = 0
        for index, req in enumerate(requests):
            if req in self.frames:
                hit += 1
                chartLst.append([copy.deepcopy(self.frames), req, {"H": self.frames.index(req)}])
            else:
                flag = True
                for i in range(self.size):
                    if self.frames[i]==None:
                        self.frames[i] = req
                        chartLst.append([copy.deepcopy(self.frames), req, {}])
                        flag = False
                        break
                if flag:
                    s = set()
                    for r in requests[index+1:]:
                        if r in self.frames:
                            s.add(r)
                            if len(s)==self.size:
                                x = self.frames.index(r)
                                tmpDict = copy.deepcopy(chartLst[-1][2])
                                tmpDict["R"] = x
                                chartLst[-1] = [copy.deepcopy(self.frames), chartLst[-1][1], tmpDict]
                                self.frames[x] = req
                                chartLst.append([copy.deepcopy(self.frames), req, {}])
                                break
                    if len(s)!=self.size:
                        for x, r in enumerate(self.frames):
                            if r not in s:
                                tmpDict = copy.deepcopy(chartLst[-1][2])
                                tmpDict["R"] = x
                                chartLst[-1] = [copy.deepcopy(self.frames), chartLst[-1][1], tmpDict]
                                self.frames[x] = req
                                chartLst.append([copy.deepcopy(self.frames), req, {}])
                                break
        output = Output("Optimal Page Replacement", chartLst, hit)
        return output