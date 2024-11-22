from ossimulator import cpuscheduling as c
from ossimulator import diskscheduling as d
from ossimulator import memoryallocation as m
from ossimulator import pagereplacement as p
from ossimulator import visualization as v
from ossimulator import process as pr
from ossimulator import harddisk as hd


visual = v.Visualize()


# cs = c.CpuScheduler()

# processLst = [
#     ["P0", 1, 3, 1],
#     ["P1", 10, 5, 5],
#     ["P2", 17, 2, 4],
#     ["P3", 3, 1, 3],
#     ["P4", 2, 4, 2],
#     ["P5", 1, 3, 1],
#     ["P6", 0, 5, 5],
# ]


# processes = pr.Process()
# processes.addProcesses(processLst)

# fcfsout = cs.fcfs(processes)
# print("FCFS:", fcfsout.result)
# print("Average Turnaround Time: ", fcfsout.avgtt)
# print("Average Waiting Time: ", fcfsout.avgwt)
# print()

# sjfout = cs.sjf(processes)
# print("SJF:", sjfout.result)
# print("Average Turnaround Time: ", sjfout.avgwt)
# print("Average Waiting Time: ", sjfout.avgtt)
# print()

# nprout = cs.prioritynp(processes)
# print("NP Priority:", nprout.result)
# print("Average Turnaround Time: ", nprout.avgwt)
# print("Average Waiting Time: ", nprout.avgtt)
# print()

# rrout = cs.rr(processes, 2)
# print("RR:", rrout.result)
# print("Average Turnaround Time: ", rrout.avgtt)
# print("Average Waiting Time: ", rrout.avgwt)
# print()

# srtfout = cs.srtf(processes)
# print("SRTF:", srtfout.result)
# print("Average Turnaround Time: ", srtfout.avgtt)
# print("Average Waiting Time: ", srtfout.avgwt)
# print()

# prout = cs.priorityp(processes)
# print("P Priority:", prout.result)
# print("Average Turnaround Time: ", prout.avgtt)
# print("Average Waiting Time: ", prout.avgwt)
# print()


# visual.ganttchart(fcfsout)
# visual.ganttchart(sjfout)
# visual.ganttchart(nprout)
# visual.ganttchart(rrout)
# visual.ganttchart(srtfout)
# visual.ganttchart(prout)


requestLst = [50, 91, 150, 92, 130, 18, 140, 70, 60]

disk = hd.Disk(200)
disk.setHeadPos(53)
disk.addRequests(requestLst)

ds = d.DiskScheduler()

fcfsdout = ds.fcfs(disk)
print("FCFS:", fcfsdout.servedorder)
print("Total head movement:", fcfsdout.movement)
print()

sstfout = ds.sstf(disk)
print("SSTF:", sstfout.servedorder)
print("Total head movement:", sstfout.movement)
print()

scanout = ds.scan(disk)
print("SCAN:", scanout.servedorder)
print("Total head movement:", scanout.movement)
print()

cscanout = ds.cscan(disk)
print("C-SCAN:", cscanout.servedorder)
print("Total head movement:", scanout.movement)
print()

lookout = ds.look(disk)
print("LOOK:", lookout.servedorder)
print("Total head movement:", lookout.movement)
print()

clookout = ds.clook(disk)
print("C-LOOK:", clookout.servedorder)
print("Total head movement:", clookout.movement)
print()

visual.headmovement(fcfsdout)
visual.headmovement(sstfout)
visual.headmovement(scanout)
visual.headmovement(cscanout)
visual.headmovement(lookout)
visual.headmovement(clookout)


# # pr = p.PageReplacer(4)
# # requestLst = [1,2,3,4,5,3,2,6,1,3,2,4,5,6,5,4,2,3,2,1,2,3,2,5,6]

# # randout = pr.rand(requestLst)
# # print("Random Hit =", randout.hits)

# # pr.clearFrames()
# # fifoout = pr.fifo(requestLst)
# # print("FIFO Hit =", fifoout.hits)

# # pr.clearFrames()
# # lruout = pr.lru(requestLst)
# # print("LRU Hit =", lruout.hits)

# # pr.clearFrames()
# # mruout = pr.mru(requestLst)
# # print("MRU Hit =", mruout.hits)

# # pr.clearFrames()
# # lfuout = pr.lfu(requestLst)
# # print("LFU Hit =", lfuout.hits)

# # pr.clearFrames()
# # mfuout = pr.mfu(requestLst)
# # print("MFU Hit =", mfuout.hits)

# # pr.clearFrames()
# # clockout = pr.clock(requestLst)
# # print("Clock Hit =", clockout.hits)

# # pr.clearFrames()
# # optout = pr.optimal(requestLst)
# # print("Optimal Hit =", optout.hits)


# # visual.replacementtable(randout)
# # visual.replacementtable(fifoout)
# # visual.replacementtable(lruout)
# # visual.replacementtable(mruout)
# # visual.replacementtable(lfuout)
# # visual.replacementtable(mfuout)
# # visual.replacementtable(clockout)
# # visual.replacementtable(optout)


# # memoryStatus = [100, 320, 500, 200, 300, 600]
# # processDict = {
# #     "P0": 212,
# #     "P1": 98,
# #     "P2": 417,
# #     "P3": 112,
# #     "P4": 426
# # }
# # ma = m.MemoryAllocator(memoryStatus)

# # ffout = ma.firstFit(processDict)
# # print("Process Status:", ffout.result)
# # print("Available Memory:", ma.getMemoryStatus())
# # print("Total Available Memory:", ma.totalFreeMemory())
# # print()

# # ma.updateBlocks(memoryStatus)

# # bfout = ma.bestFit(processDict)
# # print("Process Status:", bfout.result)
# # print("Available Memory:", ma.getMemoryStatus())
# # print("Total Available Memory:", ma.totalFreeMemory())
# # print()

# # ma.updateBlocks(memoryStatus)

# # wfout = ma.worstFit(processDict)
# # print("Process Status:", wfout.result)
# # print("Available Memory:", ma.getMemoryStatus())
# # print("Total Available Memory:", ma.totalFreeMemory())
# # print()

# # ma.updateBlocks(memoryStatus)

# # nfout = ma.nextFit(processDict)
# # print("Process Status:", nfout.result)
# # print("Available Memory:", ma.getMemoryStatus())
# # print("Total Available Memory:", ma.totalFreeMemory())
# # print()

# # visual.memoryStatus(ffout)
# # visual.memoryStatus(bfout)
# # visual.memoryStatus(wfout)
# # visual.memoryStatus(nfout)


