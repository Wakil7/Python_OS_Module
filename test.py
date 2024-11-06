from ossimulator import cpuscheduling as cs
from ossimulator import diskscheduling as ds

fcfsout = cs.fcfs({'A':[1, 3], 'B':[0, 5], 'C':[1, 2], 'D': [3, 1], 'E':[2, 4]})
print(fcfsout, cs.avg(fcfsout, "TT"), cs.avg(fcfsout, "WT"))
sjfout = cs.sjf({'A':[1, 3], 'B':[0, 5], 'C':[1, 2], 'D': [3, 1], 'E':[2, 4]})
print(sjfout, cs.avg(sjfout, "TT"), cs.avg(sjfout, "WT"))
nprout = cs.prioritynp({'A':[1, 3, 1], 'B':[0, 5, 5], 'C':[1, 2, 4], 'D': [3, 1, 3], 'E':[2, 4, 2]})
print(nprout, cs.avg(nprout, "TT"), cs.avg(nprout, "WT"))
# rrout = rr({'A':[0, 5, 1], 'B':[1, 6, 5], 'C':[2, 3, 4], 'D': [3, 1, 3], 'E':[4, 5, 2], 'F':[6, 4, 2]},4)
# rrout = rr({'A':[0, 5, 1], 'B':[1, 4, 5], 'C':[2, 2, 4], 'D': [4, 1, 3]},2)
rrout = cs.rr({'A':[1, 3, 1], 'B':[0, 5, 5], 'C':[1, 2, 4], 'D': [3, 1, 3], 'E':[2, 4, 2]},2)
print(rrout, cs.avg(rrout, "TT"), cs.avg(rrout, "WT"))
srtfout = cs.srtf({'A':[1, 3], 'B':[0, 5], 'C':[1, 2], 'D': [3, 1], 'E':[2, 4]})
print(srtfout, cs.avg(srtfout, "TT"), cs.avg(srtfout, "WT"))

prout = cs.priorityp({'A':[1, 3, 1], 'B':[0, 5, 5], 'C':[1, 2, 4], 'D': [3, 1, 3], 'E':[2, 4, 2]})
print(prout, cs.avg(prout, "TT"), cs.avg(prout, "WT"))

requestLst = [50, 91, 150, 92, 130, 18, 140, 70, 60]
print(ds.fcfs(requestLst, 53, 200))
print(ds.sstf(requestLst, 53, 200))
print(ds.scan(requestLst, 53, 200))
print(ds.cscan(requestLst, 53, 200))
print(ds.look(requestLst, 53, 200))
print(ds.clook(requestLst, 53, 200))