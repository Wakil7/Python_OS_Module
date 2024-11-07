import ossimulator

cs = ossimulator.CpuScheduler()
processes = [
    [1000, 1, 3, 1],
    [1001, 0, 5, 5],
    [1002, 1, 2, 4],
    [1003, 3, 1, 3],
    [1004, 2, 4, 2]
]

cs.addProcesses(processes)
fcfsout = cs.fcfs()
print("FCFS:", fcfsout)
print("Average Turnaround Time: ", cs.avg(fcfsout, "TT"))
print("Average Waiting Time: ", cs.avg(fcfsout, "WT"))
print()

sjfout = cs.sjf()
print("SJF:", sjfout)
print("Average Turnaround Time: ", cs.avg(sjfout, "TT"))
print("Average Waiting Time: ", cs.avg(sjfout, "WT"))
print()

nprout = cs.prioritynp()
print("NP Priority:", nprout)
print("Average Turnaround Time: ", cs.avg(nprout, "TT"))
print("Average Waiting Time: ", cs.avg(nprout, "WT"))
print()

rrout = cs.rr(2)
print("RR:", rrout)
print("Average Turnaround Time: ", cs.avg(rrout, "TT"))
print("Average Waiting Time: ", cs.avg(rrout, "WT"))
print()

srtfout = cs.srtf()
print("SRTF:", srtfout)
print("Average Turnaround Time: ", cs.avg(srtfout, "TT"))
print("Average Waiting Time: ", cs.avg(srtfout, "WT"))
print()

prout = cs.priorityp()
print("P Priority:", prout)
print("Average Turnaround Time: ", cs.avg(prout, "TT"))
print("Average Waiting Time: ", cs.avg(prout, "WT"))
print()

ds = ossimulator.DiskScheduler(200)

requestLst = [50, 91, 150, 92, 130, 18, 140, 70, 60]
ds.addRequests(requestLst)
head = 53

lst, mov = ds.fcfs(head)
print("FCFS:", lst)
print("Total head movement:", mov)
print()

lst, mov = ds.sstf(head)
print("SSTF:", lst)
print("Total head movement:", mov)
print()

lst, mov = ds.scan(head)
print("SCAN:", lst)
print("Total head movement:", mov)
print()

lst, mov = ds.cscan(head)
print("C-SCAN:", lst)
print("Total head movement:", mov)
print()

lst, mov = ds.look(head)
print("LOOK:", lst)
print("Total head movement:", mov)
print()

lst, mov = ds.clook(head)
print("C-LOOK:", lst)
print("Total head movement:", mov)
print()

