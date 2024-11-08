import random
class PageReplacement:
    def __init__(self, n):
        self.size = n
        self.frames = [None]*n

    def clearFrames(self):
        self.frames = [None]*self.size

    def rand(self, requests):
        hit = 0
        for req in requests:
            if req in self.frames:
                hit+=1
            else:
                flag = True
                for i in range(self.size):
                    if self.frames[i]==None:
                        self.frames[i] = req
                        flag = False
                        break
                if flag:
                    x = random.randint(0, self.size-1)
                    self.frames[x] = req
        return hit
    
    def fifo(self, requests):
        index = 0
        hit = 0
        for req in requests:
            if req in self.frames:
                hit+=1
            else:
                self.frames[index] = req
                index = (index + 1) % self.size
        return hit
    
    def lru(self, requests):
        usedDict = {x:1 for x in self.frames if x is not None}
        hit = 0
        for req in requests:
            usedDict = dict(map(lambda x: [x[0], x[1]+1], usedDict.items()))
            if req in self.frames:
                hit += 1
                usedDict[req] = 1
            else:
                flag=True
                for i in range(self.size):
                    if self.frames[i] == None:
                        self.frames[i] = req
                        usedDict[req] = 1
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
                    self.frames[x] = req
                    usedDict[req] = 1
        return hit
    


    def mru(self, requests):
        usedDict = {x:1 for x in self.frames if x is not None}
        hit = 0
        for req in requests:
            usedDict = dict(map(lambda x: [x[0], x[1]+1], usedDict.items()))
            if req in self.frames:
                hit += 1
                usedDict[req] = 1
            else:
                flag=True
                for i in range(self.size):
                    if self.frames[i] == None:
                        self.frames[i] = req
                        usedDict[req] = 1
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
                    self.frames[x] = req
                    usedDict[req] = 1
        return hit
    
    def lfu(self, requests):
        hit = 0
        hitDict = {x:0 for x in self.frames if x is not None}
        for req in requests:
            if req in self.frames:
                hit += 1
                hitDict[req] += 1
            else:
                flag = True
                for i in range(self.size):
                    if self.frames[i]==None:
                        self.frames[i] = req
                        hitDict[req] = 0
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
                    self.frames[x] = req
                    if req in hitDict.keys():
                        hitDict[req]+=1
                    else:
                        hitDict[req]=0
                        
        return hit
    
    def mfu(self, requests):
        hit = 0
        hitDict = {x:0 for x in self.frames if x is not None}
        for req in requests:
            if req in self.frames:
                hit += 1
                hitDict[req] += 1
            else:
                flag = True
                for i in range(self.size):
                    if self.frames[i]==None:
                        self.frames[i] = req
                        hitDict[req] = 0
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
                    self.frames[x] = req
                    if req in hitDict.keys():
                        hitDict[req]+=1
                    else:
                        hitDict[req]=0
                        
        return hit
    
    def clock(self, requests):
        pass

if __name__ == "__main__":
    pr = PageReplacement(4)
    requestLst = [1,2,3,4,5,3,2,6,1,3,2,4,5,6,5,4,2,3,2,1,2,3,2,5,6]
    print(pr.fifo(requestLst))
    pr.clearFrames()
    print(pr.lru(requestLst))
    pr.clearFrames()
    print(pr.rand(requestLst))
    pr.clearFrames()
    print(pr.mru(requestLst))
    pr.clearFrames()
    print(pr.lfu(requestLst))
    pr.clearFrames()
    print(pr.mfu(requestLst))