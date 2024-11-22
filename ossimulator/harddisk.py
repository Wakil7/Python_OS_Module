class Disk:
    def __init__(self, n):
        self.size = n
        self.requests = []
        self.head = 0

    def setHeadPos(self, pos):
        if pos<0 or pos>=self.size:
            return False
        self.head=pos
        return True
    
    def getHeadPos(self):
        return self.head

    def addRequest(self, req):
        if type(req)!=int:
            return False
        if req<0 or req>=self.size:
            return False
        
        self.requests.append(req)
        return True
    
    def addRequests(self, lst):
        for req in lst:
            if type(req)!=int:
                return False
            if req<0 or req>=self.size:
                return True
        
        self.requests.extend(lst)
    
    def removeRequest(self, req):
        if req in self.requests:
            self.requests.remove(req)
            return True
        else:
            return False