from ossimulator import diskscheduling as ds
from ossimulator import cpuscheduling as cs


requestLst = [50, 91, 150, 92, 130, 18, 140, 70, 60]
print("FCFS:", ds.fcfs(requestLst, 53, 200))
print("SSTF:", ds.sstf(requestLst, 53, 200))
print("SCAN:", ds.scan(requestLst, 53, 200))
print("C-SCAN:", ds.cscan(requestLst, 53, 200))
print("LOOK:", ds.look(requestLst, 53, 200))
print("C-LOOK:", ds.clook(requestLst, 53, 200))


#{ProcessName/ProcessId: [ArrivalTime, BurstTime, Priority]}
processes = {
    1000:[1, 3, 1],
    1001:[0, 5, 5],
    1002:[1, 2, 4],
    1003:[3, 1, 3],
    1004:[2, 4, 2]
}
fcfsout = cs.fcfs(processes)
print("FCFS:", fcfsout, cs.avg(fcfsout, "TT"), cs.avg(fcfsout, "WT"))

sjfout = cs.sjf(processes)
print("SJF:", sjfout, cs.avg(sjfout, "TT"), cs.avg(sjfout, "WT"))

nprout = cs.prioritynp(processes)
print("NP Priority:", nprout, cs.avg(nprout, "TT"), cs.avg(nprout, "WT"))

# rrout = rr(processes,4)
# rrout = rr(processes,2)
rrout = cs.rr(processes,2)
print("RR:", rrout, cs.avg(rrout, "TT"), cs.avg(rrout, "WT"))

srtfout = cs.srtf(processes)
print("SRTF:", srtfout, cs.avg(srtfout, "TT"), cs.avg(srtfout, "WT"))

prout = cs.priorityp(processes)
print("P Priority:", prout, cs.avg(prout, "TT"), cs.avg(prout, "WT"))

