from collections import namedtuple

class DiskScheduler:
    
    def seek(self, diskObj, start, near = False, d="left", lst=[]):
        head = start
        if lst==[]:
            reqLst = sorted(diskObj.requests)
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
                    if d.lower()=="right":
                        movement = abs(head-reqLst[i])
                        head = reqLst[i]
                        index = i
                    else:
                        movement = abs(head-reqLst[i-1])
                        head = reqLst[i-1]
                        index = i-1

                    break
        return head, movement, index


    def fcfs(self, diskObj):
        Output = namedtuple("Output", ["name", "visualdata", "disksize", "movement"])
        head = diskObj.head
        reqLst = [head]
        movement = 0
        for r in diskObj.requests:
            if (r>=diskObj.size or r<0):
                return False
            movement += abs(head-r)
            head = r
        reqLst.extend(diskObj.requests)
        output = Output("FCFS", reqLst, diskObj.size, movement)
        return output

    def sstf(self, diskObj):
        Output = namedtuple("Output", ["name", "visualdata", "disksize", "movement"])
        
        reqLst = sorted(diskObj.requests)
        head = diskObj.head
        outList = [head]
        movement = 0

        while len(reqLst)!=0:
            head, mov, index = self.seek(diskObj, head, near = True, lst=reqLst)
            r = reqLst[index]
            if (r>=diskObj.size or r<0):
                return False
            movement += mov
            outList.append(r)
            reqLst.pop(index)
        
        output = Output("SSTF", outList, diskObj.size, movement)
        return output


    def scan(self, diskObj, direction="left"):
        Output = namedtuple("Output", ["name", "visualdata", "disksize", "movement"])
        head = diskObj.head
        reqLst = sorted(diskObj.requests)
        n = len(reqLst)
        outList = [head]
        
        head, movement, index = self.seek(diskObj, head, d=direction)
        oldind = index

        def fetch():
            nonlocal movement, head, outList, index
            r = reqLst[index]
            if (r>=diskObj.size or r<0):
                return False
            movement += abs(head-r)
            head = r
            outList.append(r)

        if direction.lower()=="right":
            while index<n:
                if fetch()==False:
                    return False
                index +=1
            r = diskObj.size-1
            movement += abs(head-r)
            head = r
            outList.append(r)
            index = oldind-1
            while index>=0:
                fetch()
                index -= 1
        else:
            while index>=0:
                fetch()
                index -= 1
            movement += head
            head = 0
            outList.append(0)
            index = oldind + 1
            while index<n:
                fetch()
                index += 1
        
        output = Output("SCAN", outList, diskObj.size, movement)
        return output

    def cscan(self, diskObj, direction="left"):
        Output = namedtuple("Output", ["name", "visualdata", "disksize", "movement"])
        head = diskObj.head
        reqLst = sorted(diskObj.requests)
        n = len(reqLst)
        outList = [head]

        head, movement, index = self.seek(diskObj, head, d=direction)
        oldind = index

        def fetch():
            nonlocal movement, head, outList, index
            r = reqLst[index]
            if (r>=diskObj.size or r<0):
                return False
            movement += abs(head-r)
            head = r
            outList.append(r)

        if direction.lower()=="right":
            while index<n:
                fetch()
                index += 1
            r = diskObj.size-1
            movement += abs(head-r)
            outList.append(r)
            movement += diskObj.head-1
            outList.append(0)
            head = 0
            head, mov, index = self.seek(diskObj, head, d=direction)
            movement += mov
            while index<oldind:
                fetch()
                index += 1
        else:
            while index>=0:
                fetch()
                index -= 1
            movement += head
            outList.append(0)
            head = diskObj.size-1
            movement += head
            outList.append(diskObj.size-1)
            head, mov, index = self.seek(diskObj, head, d=direction)
            movement += mov
            while index>oldind:
                fetch()
                index -= 1
        
        output = Output("C-SCAN", outList, diskObj.size, movement)
        return output

    def look(self, diskObj, direction="left"):
        Output = namedtuple("Output", ["name", "visualdata", "disksize", "movement"])
        head = diskObj.head
        reqLst = sorted(diskObj.requests)
        n = len(reqLst)
        outList = [head]

        head, movement, index = self.seek(diskObj, head, d=direction)
        oldind = index

        def fetch():
            nonlocal movement, head, outList, index
            r = reqLst[index]
            if (r>=diskObj.size or r<0):
                return False
            movement += abs(head-r)
            head = r
            outList.append(r)

        if direction.lower()=="right":
            while index<n:
                fetch()
                index += 1
            index = oldind - 1
            while index>=0:
                fetch()
                index -= 1
        else:
            while index>=0:
                fetch()
                index -= 1
            index = oldind + 1
            while index<n:
                fetch()
                index += 1
        
        output = Output("LOOK", outList, diskObj.size, movement)
        return output


    def clook(self, diskObj, direction="left"):
        Output = namedtuple("Output", ["name", "visualdata", "disksize", "movement"])
        head = diskObj.head
        reqLst = sorted(diskObj.requests)
        n = len(reqLst)
        outList = [head]

        head, movement, index = self.seek(diskObj, head, d=direction)
        oldind = index

        def fetch():
            nonlocal movement, head, outList, index
            r = reqLst[index]
            if (r>=diskObj.size or r<0):
                return False
            movement += abs(head-r)
            head = r
            outList.append(r)

        if direction.lower()=="right":
            while index<n:
                fetch()
                index += 1
            index = 0
            while index<oldind:
                fetch()
                index += 1
        else:
            while index>=0:
                fetch()
                index -= 1
            index = n-1
            while index>oldind:
                fetch()
                index -= 1
        
        output = Output("C-LOOK", outList, diskObj.size, movement)
        return output