from ossimulator import process as pr
from ossimulator import harddisk as hd
from ossimulator import memory as m
from ossimulator import cpuscheduling as c
from ossimulator import diskscheduling as d
from ossimulator import memoryallocation as ma
from ossimulator import pagereplacement as p
from ossimulator import visualization as v



visual = v.Visualize()


cs = c.CpuScheduler()

processLst = [
    ["P0", 1, 3, 1, 212],
    ["P1", 10, 5, 5, 98],
    ["P2", 17, 2, 4, 417],
    ["P3", 3, 1, 3, 112],
    ["P4", 2, 4, 2, 426]
]


processes = pr.Process()
processes.addProcesses(processLst)

fcfsout = cs.fcfs(processes)
print("FCFS:", fcfsout.result)
print("Average Turnaround Time: ", fcfsout.avgtt)
print("Average Waiting Time: ", fcfsout.avgwt)
print()

sjfout = cs.sjf(processes)
print("SJF:", sjfout.result)
print("Average Turnaround Time: ", sjfout.avgtt)
print("Average Waiting Time: ", sjfout.avgwt)
print()

nprout = cs.prioritynp(processes)
print("NP Priority:", nprout.result)
print("Average Turnaround Time: ", nprout.avgtt)
print("Average Waiting Time: ", nprout.avgwt)
print()

rrout = cs.rr(processes, 2)
print("RR:", rrout.result)
print("Average Turnaround Time: ", rrout.avgtt)
print("Average Waiting Time: ", rrout.avgwt)
print()

srtfout = cs.srtf(processes)
print("SRTF:", srtfout.result)
print("Average Turnaround Time: ", srtfout.avgtt)
print("Average Waiting Time: ", srtfout.avgwt)
print()

prout = cs.priorityp(processes)
print("P Priority:", prout.result)
print("Average Turnaround Time: ", prout.avgtt)
print("Average Waiting Time: ", prout.avgwt)
print()

print(cs.compare(fcfsout, prout, nprout, rrout, srtfout, sjfout))

visual.showGanttChart(fcfsout)
visual.showGanttChart(sjfout)
visual.showGanttChart(nprout)
visual.showGanttChart(rrout)
visual.showGanttChart(srtfout)
visual.showGanttChart(prout)


requestLst = [50, 91, 150, 92, 130, 18, 140, 70, 60]

disk = hd.Disk(200)
disk.setHeadPos(100)
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

scanout = ds.scan(disk, direction="right")
print("SCAN:", scanout.servedorder)
print("Total head movement:", scanout.movement)
print()

cscanout = ds.cscan(disk, direction="right")
print("C-SCAN:", cscanout.servedorder)
print("Total head movement:", cscanout.movement)
print()

lookout = ds.look(disk, direction="right")
print("LOOK:", lookout.servedorder)
print("Total head movement:", lookout.movement)
print()

clookout = ds.clook(disk, direction="right")
print("C-LOOK:", clookout.servedorder)
print("Total head movement:", clookout.movement)
print()

print(ds.compare(fcfsdout, sstfout, scanout, cscanout, lookout, clookout))

visual.showHeadMovement(fcfsdout)
visual.showHeadMovement(sstfout)
visual.showHeadMovement(scanout)
visual.showHeadMovement(cscanout)
visual.showHeadMovement(lookout)
visual.showHeadMovement(clookout)

memory = m.Memory(1024, 4)
pr = p.PageReplacer()
requestLst = [1,2,3,4,5,3,2,6,1,3,2,4,5,6,5,4,2,3,2,1,2,3,2,5,6]

randout = pr.rand(requestLst, memory)
print("Random Hit =", randout.hits)

memory.clearFrames()
fifoout = pr.fifo(requestLst, memory)
print("FIFO Hit =", fifoout.hits)

memory.clearFrames()
lruout = pr.lru(requestLst, memory)
print("LRU Hit =", lruout.hits)

memory.clearFrames()
mruout = pr.mru(requestLst, memory)
print("MRU Hit =", mruout.hits)

memory.clearFrames()
lfuout = pr.lfu(requestLst, memory)
print("LFU Hit =", lfuout.hits)

memory.clearFrames()
mfuout = pr.mfu(requestLst, memory)
print("MFU Hit =", mfuout.hits)

memory.clearFrames()
clockout = pr.clock(requestLst, memory)
print("Clock Hit =", clockout.hits)

memory.clearFrames()
optout = pr.optimal(requestLst, memory)
print("Optimal Hit =", optout.hits)

print(pr.compare(randout, fifoout, mfuout, clockout))

visual.showTable(randout)
visual.showTable(fifoout)
visual.showTable(lruout)
visual.showTable(mruout)
visual.showTable(lfuout)
visual.showTable(mfuout)
visual.showTable(clockout)
visual.showTable(optout)


memoryStatus = [100, 320, 500, 200, 300, 600]

allocator = ma.MemoryAllocator()

memory.setMainMemory(memoryStatus, 10000)
ffout = allocator.firstFit(processes, memory)
print("Process Status:", ffout.result)
print("Available Memory:", memory.getMainMemoryStatus())
print("Total Available Memory:", memory.totalFreeMemory())
print()

memory.setMainMemory(memoryStatus, 10000)

bfout = allocator.bestFit(processes, memory)
print("Process Status:", bfout.result)
print("Available Memory:", memory.getMainMemoryStatus())
print("Total Available Memory:", memory.totalFreeMemory())
print()

memory.setMainMemory(memoryStatus, 10000)

wfout = allocator.worstFit(processes, memory)
print("Process Status:", wfout.result)
print("Available Memory:", memory.getMainMemoryStatus())
print("Total Available Memory:", memory.totalFreeMemory())
print()

memory.setMainMemory(memoryStatus, 10000)

nfout = allocator.nextFit(processes, memory)
print("Process Status:", nfout.result)
print("Available Memory:", memory.getMainMemoryStatus())
print("Total Available Memory:", memory.totalFreeMemory())
print()

visual.showMemory(ffout)
visual.showMemory(bfout)
visual.showMemory(wfout)
visual.showMemory(nfout)


