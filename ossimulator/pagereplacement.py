import random
import copy
from collections import namedtuple

class PageReplacer:

    def rand(self, requests, memoryObj):
        Output = namedtuple("Output", ["name", "chartdata", "hits"])
        framesLst = [] #[memoryObj.frames, req, {"H":index, "R":index}]
        hit = 0
        for req in requests:
            if req in memoryObj.frames:
                hit+=1
                framesLst.append([copy.deepcopy(memoryObj.frames), req, {"H": memoryObj.frames.index(req)}])
            else:
                flag = True
                for i in range(memoryObj.frameSize):
                    if memoryObj.frames[i]==None:
                        memoryObj.frames[i] = req
                        framesLst.append([copy.deepcopy(memoryObj.frames), req, {}])
                        flag = False
                        break
                if flag:
                    x = random.randint(0, memoryObj.frameSize-1)
                    tmpDict = copy.deepcopy(framesLst[-1][2])
                    tmpDict["R"] = x
                    framesLst[-1] = [copy.deepcopy(memoryObj.frames), framesLst[-1][1], tmpDict]
                    memoryObj.frames[x] = req
                    framesLst.append([copy.deepcopy(memoryObj.frames), req, {}])
        output = Output("Random Page Replacement", framesLst, hit)
        return output
    
    def fifo(self, requests, memoryObj):
        Output = namedtuple("Output", ["name", "chartdata", "hits"])
        framesLst = [] 
        index = 0
        hit = 0
        for req in requests:
            if req in memoryObj.frames:
                hit+=1
                framesLst.append([copy.deepcopy(memoryObj.frames), req, {"H": memoryObj.frames.index(req)}])
            else:
                flag = True
                for i in range(memoryObj.frameSize):
                    if memoryObj.frames[i]==None:
                        memoryObj.frames[i] = req
                        index = (i + 1) % memoryObj.frameSize
                        framesLst.append([copy.deepcopy(memoryObj.frames), req, {}])
                        flag = False
                        break
                if flag:
                    tmpDict = copy.deepcopy(framesLst[-1][2])
                    tmpDict["R"] = index
                    framesLst[-1] = [copy.deepcopy(memoryObj.frames), framesLst[-1][1], tmpDict]
                    memoryObj.frames[index] = req
                    framesLst.append([copy.deepcopy(memoryObj.frames), req, {}])
                    index = (index + 1) % memoryObj.frameSize
        output = Output("FIFO Page Replacement", framesLst, hit)
        return output
    
    def lru(self, requests, memoryObj):
        Output = namedtuple("Output", ["name", "chartdata", "hits"])
        framesLst = [] 
        usedDict = {x:1 for x in memoryObj.frames if x is not None}
        hit = 0
        for req in requests:
            usedDict = dict(map(lambda x: [x[0], x[1]+1], usedDict.items()))
            if req in memoryObj.frames:
                hit += 1
                framesLst.append([copy.deepcopy(memoryObj.frames), req, {"H": memoryObj.frames.index(req)}])
                usedDict[req] = 1
            else:
                flag=True
                for i in range(memoryObj.frameSize):
                    if memoryObj.frames[i] == None:
                        memoryObj.frames[i] = req
                        usedDict[req] = 1
                        framesLst.append([copy.deepcopy(memoryObj.frames), req, {}])
                        flag=False
                        break
                        
                if flag:
                    m = 0
                    for k in usedDict.keys():
                        if usedDict[k]>m:
                            m = usedDict[k]
                            page = k
                    
                    del usedDict[page]
                    x = memoryObj.frames.index(page)
                    tmpDict = copy.deepcopy(framesLst[-1][2])
                    tmpDict["R"] = x
                    framesLst[-1] = [copy.deepcopy(memoryObj.frames), framesLst[-1][1], tmpDict]
                    memoryObj.frames[x] = req
                    framesLst.append([copy.deepcopy(memoryObj.frames), req, {}])
                    usedDict[req] = 1
        output = Output("LRU Page Replacement", framesLst, hit)
        return output
    
    def mru(self, requests, memoryObj):
        Output = namedtuple("Output", ["name", "chartdata", "hits"])
        framesLst = [] 
        usedDict = {x:1 for x in memoryObj.frames if x is not None}
        hit = 0
        for req in requests:
            usedDict = dict(map(lambda x: [x[0], x[1]+1], usedDict.items()))
            if req in memoryObj.frames:
                hit += 1
                framesLst.append([copy.deepcopy(memoryObj.frames), req, {"H": memoryObj.frames.index(req)}])
                usedDict[req] = 1
            else:
                flag=True
                for i in range(memoryObj.frameSize):
                    if memoryObj.frames[i] == None:
                        memoryObj.frames[i] = req
                        usedDict[req] = 1
                        framesLst.append([copy.deepcopy(memoryObj.frames), req, {}])
                        flag=False
                        break
                        
                if flag:
                    m = None
                    for k in usedDict.keys():
                        if m == None or usedDict[k]<m:
                            m = usedDict[k]
                            page = k
                    
                    del usedDict[page]
                    x = memoryObj.frames.index(page)
                    tmpDict = copy.deepcopy(framesLst[-1][2])
                    tmpDict["R"] = x
                    framesLst[-1] = [copy.deepcopy(memoryObj.frames), framesLst[-1][1], tmpDict]
                    memoryObj.frames[x] = req
                    framesLst.append([copy.deepcopy(memoryObj.frames), req, {}])
                    usedDict[req] = 1
        output = Output("MRU Page Replacement", framesLst, hit)
        return output
    
    def lfu(self, requests, memoryObj):
        Output = namedtuple("Output", ["name", "chartdata", "hits"])
        framesLst = [] 
        hit = 0
        hitDict = {x:0 for x in memoryObj.frames if x is not None}
        for req in requests:
            if req in memoryObj.frames:
                hit += 1
                framesLst.append([copy.deepcopy(memoryObj.frames), req, {"H": memoryObj.frames.index(req)}])
                hitDict[req] += 1
            else:
                flag = True
                for i in range(memoryObj.frameSize):
                    if memoryObj.frames[i]==None:
                        memoryObj.frames[i] = req
                        hitDict[req] = 0
                        framesLst.append([copy.deepcopy(memoryObj.frames), req, {}])
                        flag = False
                        break
                if flag:
                    m = None
                    tempDict = dict(filter(lambda x: True if x[0] in memoryObj.frames else False, hitDict.items()))
                    for k in tempDict.keys():
                        if m==None or tempDict[k]<m:
                            m = tempDict[k]
                            page = k
                    
                    x = memoryObj.frames.index(page)
                    tmpDict = copy.deepcopy(framesLst[-1][2])
                    tmpDict["R"] = x
                    framesLst[-1] = [copy.deepcopy(memoryObj.frames), framesLst[-1][1], tmpDict]
                    memoryObj.frames[x] = req
                    framesLst.append([copy.deepcopy(memoryObj.frames), req, {}])
                    if req in hitDict.keys():
                        hitDict[req]+=1
                    else:
                        hitDict[req]=0
                        
        output = Output("LFU Page Replacement", framesLst, hit)
        return output
    
    def mfu(self, requests, memoryObj):
        Output = namedtuple("Output", ["name", "chartdata", "hits"])
        framesLst = [] 
        hit = 0
        hitDict = {x:0 for x in memoryObj.frames if x is not None}
        for req in requests:
            if req in memoryObj.frames:
                hit += 1
                framesLst.append([copy.deepcopy(memoryObj.frames), req, {"H": memoryObj.frames.index(req)}])
                hitDict[req] += 1
            else:
                flag = True
                for i in range(memoryObj.frameSize):
                    if memoryObj.frames[i]==None:
                        memoryObj.frames[i] = req
                        hitDict[req] = 0
                        framesLst.append([copy.deepcopy(memoryObj.frames), req, {}])
                        flag = False
                        break
                if flag:
                    m = None
                    tempDict = dict(filter(lambda x: True if x[0] in memoryObj.frames else False, hitDict.items()))
                    for k in tempDict.keys():
                        if m==None or tempDict[k]>m:
                            m = tempDict[k]
                            page = k
                    
                    x = memoryObj.frames.index(page)
                    tmpDict = copy.deepcopy(framesLst[-1][2])
                    tmpDict["R"] = x
                    framesLst[-1] = [copy.deepcopy(memoryObj.frames), framesLst[-1][1], tmpDict]
                    memoryObj.frames[x] = req
                    framesLst.append([copy.deepcopy(memoryObj.frames), req, {}])
                    if req in hitDict.keys():
                        hitDict[req]+=1
                    else:
                        hitDict[req]=0
                        
        output = Output("MFU Page Replacement", framesLst, hit)
        return output
    
    def clock(self, requests, memoryObj):
        Output = namedtuple("Output", ["name", "chartdata", "hits"])
        framesLst = [] 
        useBitDict = {x:1 for x in memoryObj.frames if x is not None}
        hit = 0
        index = 0
        for req in requests:
            if req in memoryObj.frames:
                hit += 1
                framesLst.append([copy.deepcopy(memoryObj.frames), req, {"H": memoryObj.frames.index(req)}])
                useBitDict[req] = 1
            else:
                flag = True
                for i in range(memoryObj.frameSize):
                    if memoryObj.frames[i]==None:
                        memoryObj.frames[i]=req
                        useBitDict[req] = 1
                        index = (i + 1) % memoryObj.frameSize
                        framesLst.append([copy.deepcopy(memoryObj.frames), req, {}])
                        flag = False
                        break
                if flag:
                    while (useBitDict[memoryObj.frames[index]]!=0):
                        useBitDict[memoryObj.frames[index]] = 0
                        index = (index + 1) % memoryObj.frameSize

                    del useBitDict[memoryObj.frames[index]]
                    
                    tmpDict = copy.deepcopy(framesLst[-1][2])
                    tmpDict["R"] = index
                    framesLst[-1] = [copy.deepcopy(memoryObj.frames), framesLst[-1][1], tmpDict]
                    memoryObj.frames[index] = req
                    framesLst.append([copy.deepcopy(memoryObj.frames), req, {}])
                    index = (index + 1) % memoryObj.frameSize
                    useBitDict[req]=1
        output = Output("Clock Page Replacement", framesLst, hit)
        return output
    
    def optimal(self, requests, memoryObj):
        Output = namedtuple("Output", ["name", "chartdata", "hits"])
        framesLst = [] 
        hit = 0
        for index, req in enumerate(requests):
            if req in memoryObj.frames:
                hit += 1
                framesLst.append([copy.deepcopy(memoryObj.frames), req, {"H": memoryObj.frames.index(req)}])
            else:
                flag = True
                for i in range(memoryObj.frameSize):
                    if memoryObj.frames[i]==None:
                        memoryObj.frames[i] = req
                        framesLst.append([copy.deepcopy(memoryObj.frames), req, {}])
                        flag = False
                        break
                if flag:
                    s = set()
                    for r in requests[index+1:]:
                        if r in memoryObj.frames:
                            s.add(r)
                            if len(s)==memoryObj.frameSize:
                                x = memoryObj.frames.index(r)
                                tmpDict = copy.deepcopy(framesLst[-1][2])
                                tmpDict["R"] = x
                                framesLst[-1] = [copy.deepcopy(memoryObj.frames), framesLst[-1][1], tmpDict]
                                memoryObj.frames[x] = req
                                framesLst.append([copy.deepcopy(memoryObj.frames), req, {}])
                                break
                    if len(s)!=memoryObj.frameSize:
                        for x, r in enumerate(memoryObj.frames):
                            if r not in s:
                                tmpDict = copy.deepcopy(framesLst[-1][2])
                                tmpDict["R"] = x
                                framesLst[-1] = [copy.deepcopy(memoryObj.frames), framesLst[-1][1], tmpDict]
                                memoryObj.frames[x] = req
                                framesLst.append([copy.deepcopy(memoryObj.frames), req, {}])
                                break
        output = Output("Optimal Page Replacement", framesLst, hit)
        return output