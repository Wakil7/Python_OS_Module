from ossimulator import cpuscheduling as c
from ossimulator import diskscheduling as d
from ossimulator import memoryallocation as m
from ossimulator import pagereplacement as p
from ossimulator import visualization as v
from ossimulator import processes as pr

cs = c.CpuScheduler()
processes = [
    ["P0", 1, 3, 1],
    ["P1", 10, 5, 5],
    ["P2", 17, 2, 4],
    ["P3", 3, 1, 3],
    ["P4", 2, 4, 2],
    # ["P5", 1, 3, 1],
    # ["P6", 0, 5, 5],
    # ["P7", 1, 2, 4],
    # ["P8", 3, 1, 3],
    # ["P9", 2, 4, 2],
    # [10010, 1, 3, 1],
    # [10011, 0, 5, 5],
    # [10012, 1, 2, 4],
    # [10013, 3, 1, 3],
    # [10014, 2, 4, 2],
    # [10015, 1, 3, 1],
    # [10016, 0, 5, 5],
    # [10017, 1, 2, 4],
    # [10018, 3, 1, 3],
    # [10019, 2, 4, 2]
]

# cs.addProcesses(processes)
pro = pr.Process()
pro.addProcesses(processes)


fcfsout = cs.fcfs(pro)
print("FCFS:", fcfsout.result)
print("Average Turnaround Time: ", cs.avg(fcfsout, "TT"))
print("Average Waiting Time: ", cs.avg(fcfsout, "WT"))
print()

sjfout = cs.sjf(pro)
print("SJF:", sjfout.result)
print("Average Turnaround Time: ", cs.avg(sjfout, "TT"))
print("Average Waiting Time: ", cs.avg(sjfout, "WT"))
print()

nprout = cs.prioritynp(pro)
print("NP Priority:", nprout.result)
print("Average Turnaround Time: ", cs.avg(nprout, "TT"))
print("Average Waiting Time: ", cs.avg(nprout, "WT"))
print()

rrout = cs.rr(pro, 2)
print("RR:", rrout.result)
print("Average Turnaround Time: ", cs.avg(rrout, "TT"))
print("Average Waiting Time: ", cs.avg(rrout, "WT"))
print()

srtfout = cs.srtf(pro)
print("SRTF:", srtfout.result)
print("Average Turnaround Time: ", cs.avg(srtfout, "TT"))
print("Average Waiting Time: ", cs.avg(srtfout, "WT"))
print()

prout = cs.priorityp(pro)
print("P Priority:", prout.result)
print("Average Turnaround Time: ", cs.avg(prout, "TT"))
print("Average Waiting Time: ", cs.avg(prout, "WT"))
print()

visual = v.Visualize()
visual.ganttchart(fcfsout)
visual.ganttchart(sjfout)
visual.ganttchart(nprout)
visual.ganttchart(rrout)
visual.ganttchart(srtfout)
visual.ganttchart(prout)

# ds = d.DiskScheduler(200)

# requestLst = [50, 91, 150, 92, 130, 18, 140, 70, 60]
# ds.addRequests(requestLst)
# head = 53

# lst, mov = ds.fcfs(head)
# print("FCFS:", lst)
# print("Total head movement:", mov)
# print()

# lst, mov = ds.sstf(head)
# print("SSTF:", lst)
# print("Total head movement:", mov)
# print()

# lst, mov = ds.scan(head)
# print("SCAN:", lst)
# print("Total head movement:", mov)
# print()

# lst, mov = ds.cscan(head)
# print("C-SCAN:", lst)
# print("Total head movement:", mov)
# print()

# lst, mov = ds.look(head)
# print("LOOK:", lst)
# print("Total head movement:", mov)
# print()

# lst, mov = ds.clook(head)
# print("C-LOOK:", lst)
# print("Total head movement:", mov)
# print()

# pr = p.PageReplacer(4)
# requestLst = [1,2,3,4,5,3,2,6,1,3,2,4,5,6,5,4,2,3,2,1,2,3,2,5,6]
# print("Random Hit =", pr.rand(requestLst))
# pr.clearFrames()
# print("FIFO Hit =", pr.fifo(requestLst))
# pr.clearFrames()
# print("LRU Hit =", pr.lru(requestLst))
# pr.clearFrames()
# print("MRU Hit =", pr.mru(requestLst))
# pr.clearFrames()
# print("LFU Hit =", pr.lfu(requestLst))
# pr.clearFrames()
# print("MFU Hit =", pr.mfu(requestLst))
# pr.clearFrames()
# print("Clock Hit =", pr.clock(requestLst))
# pr.clearFrames()
# print("Optimal Hit =", pr.optimal(requestLst))

# memoryStatus = [100, 320, 500, 200, 300, 600]
# processDict = {
#     1000: 212,
#     1001: 98,
#     1002: 417,
#     1003: 112,
#     1004: 426
# }
# ma = m.MemoryAllocator(memoryStatus)

# allocated = ma.firstFit(processDict)
# print("Process Status:", allocated)
# print("Available Memory:", ma.getMemoryStatus())
# print("Total Available Memory:", ma.totalFreeMemory())
# print()

# ma.updateBlocks(memoryStatus)

# allocated = ma.bestFit(processDict)
# print("Process Status:", allocated)
# print("Available Memory:", ma.getMemoryStatus())
# print("Total Available Memory:", ma.totalFreeMemory())
# print()

# ma.updateBlocks(memoryStatus)

# allocated = ma.worstFit(processDict)
# print("Process Status:", allocated)
# print("Available Memory:", ma.getMemoryStatus())
# print("Total Available Memory:", ma.totalFreeMemory())
# print()

# ma.updateBlocks(memoryStatus)

# allocated = ma.nextFit(processDict)
# print("Process Status:", allocated)
# print("Available Memory:", ma.getMemoryStatus())
# print("Total Available Memory:", ma.totalFreeMemory())
# print()

