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
