

def seek(requests, start, near = False):
    head = start
    reqLst = sorted(requests)
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


def fcfs(requests, start, n):
    head = start
    if head>=n or head<0:
        return -1
    movement = 0
    for r in requests:
        if (r>=n or r<0):
            return -1
        movement += abs(head-r)
        head = r
    return requests, movement

def sstf(requests, start, n):
    reqLst = sorted(requests)
    head = start
    outList = []
    movement = 0
    if head>=n or head<0:
        return -1
    # head, movement, index = seek(requests, start)
    # outList.append(reqLst[index])

    while len(reqLst)!=0:
        head, mov, index = seek(reqLst, head, near = True)
        movement += mov
        outList.append(reqLst[index])
        reqLst.pop(index)
    
    return outList, movement


def scan(requests, start, n):
    head = start
    reqLst = sorted(requests)
    outList = []
    if head>=n or head<0:
        return -1

    head, movement, index = seek(requests, start)
    
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

def cscan(requests, start, n):
    head = start
    reqLst = sorted(requests)
    outList = []
    if head>=n or head<0:
        return -1
    head, movement, index = seek(requests, start)
    outList.append(reqLst[index])
    oldind = index
    while index>0:
        index -= 1
        r = reqLst[index]
        movement += abs(head-r)
        head = r
        outList.append(r)
    movement += head
    head = n-1
    movement += head
    
    head, mov, index = seek(requests, head)
    movement += mov

    while index>oldind:
        r = reqLst[index]
        movement += abs(head-r)
        head = r
        outList.append(r)
        index -= 1
    
    return outList, movement

def look(requests, start, n):
    head = start
    reqLst = sorted(requests)
    outList = []
    if head>=n or head<0:
        return -1

    head, movement, index = seek(requests, start)
    
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


def clook(requests, start, n):
    head = start
    reqLst = sorted(requests)
    outList = []
    if head>=n or head<0:
        return -1
    head, movement, index = seek(requests, start)
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

        


            
        
    



    

if __name__=="__main__":
    requestLst = [50, 91, 150, 92, 130, 18, 140, 70, 60]
    print(fcfs(requestLst, 53, 200))
    print(sstf(requestLst, 53, 200))
    print(scan(requestLst, 53, 200))
    print(cscan(requestLst, 53, 200))
    print(look(requestLst, 53, 200))
    print(clook(requestLst, 53, 200))