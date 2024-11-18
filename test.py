from ossimulator import cpuscheduling as c
from ossimulator import diskscheduling as d
from ossimulator import memoryallocation as m
from ossimulator import pagereplacement as p
from ossimulator import visualization as v
from ossimulator import processes as pr

# cs = c.CpuScheduler()
# processes = [
#     ["P0", 1, 3, 1],
#     ["P1", 10, 5, 5],
#     ["P2", 17, 2, 4],
#     ["P3", 3, 1, 3],
#     ["P4", 2, 4, 2],
#     # ["P5", 1, 3, 1],
#     # ["P6", 0, 5, 5],
#     # ["P7", 1, 2, 4],
#     # ["P8", 3, 1, 3],
#     # ["P9", 2, 4, 2],
#     # [10010, 1, 3, 1],
#     # [10011, 0, 5, 5],
#     # [10012, 1, 2, 4],
#     # [10013, 3, 1, 3],
#     # [10014, 2, 4, 2],
#     # [10015, 1, 3, 1],
#     # [10016, 0, 5, 5],
#     # [10017, 1, 2, 4],
#     # [10018, 3, 1, 3],
#     # [10019, 2, 4, 2]
# ]

# # cs.addProcesses(processes)
# pro = pr.Process()
# pro.addProcesses(processes)


# fcfsout = cs.fcfs(pro)
# print("FCFS:", fcfsout.result)
# print("Average Turnaround Time: ", cs.avg(fcfsout, "TT"))
# print("Average Waiting Time: ", cs.avg(fcfsout, "WT"))
# print()

# sjfout = cs.sjf(pro)
# print("SJF:", sjfout.result)
# print("Average Turnaround Time: ", cs.avg(sjfout, "TT"))
# print("Average Waiting Time: ", cs.avg(sjfout, "WT"))
# print()

# nprout = cs.prioritynp(pro)
# print("NP Priority:", nprout.result)
# print("Average Turnaround Time: ", cs.avg(nprout, "TT"))
# print("Average Waiting Time: ", cs.avg(nprout, "WT"))
# print()

# rrout = cs.rr(pro, 2)
# print("RR:", rrout.result)
# print("Average Turnaround Time: ", cs.avg(rrout, "TT"))
# print("Average Waiting Time: ", cs.avg(rrout, "WT"))
# print()

# srtfout = cs.srtf(pro)
# print("SRTF:", srtfout.result)
# print("Average Turnaround Time: ", cs.avg(srtfout, "TT"))
# print("Average Waiting Time: ", cs.avg(srtfout, "WT"))
# print()

# prout = cs.priorityp(pro)
# print("P Priority:", prout.result)
# print("Average Turnaround Time: ", cs.avg(prout, "TT"))
# print("Average Waiting Time: ", cs.avg(prout, "WT"))
# print()

visual = v.Visualize()
# visual.ganttchart(fcfsout)
# visual.ganttchart(sjfout)
# visual.ganttchart(nprout)
# visual.ganttchart(rrout)
# visual.ganttchart(srtfout)
# visual.ganttchart(prout)

ds = d.DiskScheduler(200)

requestLst = [50, 91, 150, 92, 130, 18, 140, 70, 60]
ds.addRequests(requestLst)
head = 53

fcfsdout = ds.fcfs(head)
print("FCFS:", fcfsdout.servedorder)
print("Total head movement:", fcfsdout.movement)
print()

sstfout = ds.sstf(head)
print("SSTF:", sstfout.servedorder)
print("Total head movement:", sstfout.movement)
print()

scanout = ds.scan(head)
print("SCAN:", scanout.servedorder)
print("Total head movement:", scanout.movement)
print()

cscanout = ds.cscan(head)
print("C-SCAN:", cscanout.servedorder)
print("Total head movement:", scanout.movement)
print()

lookout = ds.look(head)
print("LOOK:", lookout.servedorder)
print("Total head movement:", lookout.movement)
print()

clookout = ds.clook(head)
print("C-LOOK:", clookout.servedorder)
print("Total head movement:", clookout.movement)
print()

visual.headmovement(fcfsdout)
visual.headmovement(sstfout)
visual.headmovement(scanout)
visual.headmovement(cscanout)
visual.headmovement(lookout)
visual.headmovement(clookout)


# pr = p.PageReplacer(4)
# requestLst = [1,2,3,4,5,3,2,6,1,3,2,4,5,6,5,4,2,3,2,1,2,3,2,5,6]

# randout = pr.rand(requestLst)
# print("Random Hit =", randout.hits)

# pr.clearFrames()
# fifoout = pr.fifo(requestLst)
# print("FIFO Hit =", fifoout.hits)

# pr.clearFrames()
# lruout = pr.lru(requestLst)
# print("LRU Hit =", lruout.hits)

# pr.clearFrames()
# mruout = pr.mru(requestLst)
# print("MRU Hit =", mruout.hits)

# pr.clearFrames()
# lfuout = pr.lfu(requestLst)
# print("LFU Hit =", lfuout.hits)

# pr.clearFrames()
# mfuout = pr.mfu(requestLst)
# print("MFU Hit =", mfuout.hits)

# pr.clearFrames()
# clockout = pr.clock(requestLst)
# print("Clock Hit =", clockout.hits)

# pr.clearFrames()
# optout = pr.optimal(requestLst)
# print("Optimal Hit =", optout.hits)


# visual.replacementtable(randout)
# visual.replacementtable(fifoout)
# visual.replacementtable(lruout)
# visual.replacementtable(mruout)
# visual.replacementtable(lfuout)
# visual.replacementtable(mfuout)
# visual.replacementtable(clockout)
# visual.replacementtable(optout)


# memoryStatus = [100, 320, 500, 200, 300, 600]
# processDict = {
#     "P0": 212,
#     "P1": 98,
#     "P2": 417,
#     "P3": 112,
#     "P4": 426
# }
# ma = m.MemoryAllocator(memoryStatus)

# ffout = ma.firstFit(processDict)
# print("Process Status:", ffout.result)
# print("Available Memory:", ma.getMemoryStatus())
# print("Total Available Memory:", ma.totalFreeMemory())
# print()

# ma.updateBlocks(memoryStatus)

# bfout = ma.bestFit(processDict)
# print("Process Status:", bfout.result)
# print("Available Memory:", ma.getMemoryStatus())
# print("Total Available Memory:", ma.totalFreeMemory())
# print()

# ma.updateBlocks(memoryStatus)

# wfout = ma.worstFit(processDict)
# print("Process Status:", wfout.result)
# print("Available Memory:", ma.getMemoryStatus())
# print("Total Available Memory:", ma.totalFreeMemory())
# print()

# ma.updateBlocks(memoryStatus)

# nfout = ma.nextFit(processDict)
# print("Process Status:", nfout.result)
# print("Available Memory:", ma.getMemoryStatus())
# print("Total Available Memory:", ma.totalFreeMemory())
# print()

# visual.memoryStatus(ffout)
# visual.memoryStatus(bfout)
# visual.memoryStatus(wfout)
# visual.memoryStatus(nfout)


