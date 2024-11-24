import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import copy

class Visualize:

    def showGanttChart(self, data):
        chartLst = copy.deepcopy(data.visualdata)
        n = len(chartLst)

        plt.figure(figsize=(12, 4))
        plt.axis("off")
        plt.xlim(0, n+1)
        plt.ylim(0, 20)
        plt.title(data.name + " Scheduling Gantt Chart", fontsize=20)
        plt.text(0, 11, "0", color="black", fontweight="bold", ha="center", va="center")

        for i, tup in enumerate(chartLst):
            pid = tup[0]
            ct = tup[1]
            if str(pid)=="Idle":
                bgcolor="yellow"
            else:
                bgcolor="skyblue"
            plt.barh(15, 1, left=i, height=5, color=bgcolor, edgecolor="black")
            plt.text(i+0.5, 15, str(pid), color="black", fontweight="bold", ha="center", va="center")
            plt.text(i+1, 11, str(ct), color="black", fontweight="bold", ha="center", va="center")
        
        plt.text(n/2, 5, f"Average Turnaround Time: {data.avgtt} ms", color="black", ha="left", va="center", fontsize=14)
        plt.text(n/2, 3, f"Average Waiting Time:  {data.avgwt} ms", color="black", ha="left", va="center", fontsize=14)
        plt.show()

    def showTable(self, data):
        chartLst = copy.deepcopy(data.visualdata)
        visualdata = []
        
        for i in range(len(chartLst[0][0])):
            tmpLst = []
            for j in range(len(chartLst)):
                tmpLst.append(chartLst[j][0][i])
            visualdata.append(tmpLst)
        
        rows = [f"Frame {i}" for i in range(len(chartLst[0][0]))]
        columns = ["Pages"]+[chartLst[i][1] for i in range(len(chartLst))]

        plt.figure(figsize=(12, 6))
        plt.axis("tight")
        plt.axis("off")
        
        tableData = [columns] + [[rows[i]] + visualdata[i] for i in range(len(rows))]
        tableObj = plt.table(cellText = tableData, loc="center", cellLoc="center")
        tableObj.auto_set_font_size(False)
        tableObj.set_fontsize(20)
        tableObj.auto_set_column_width(col=list(range(len(columns)+1)))

        for (i, j), cell in tableObj.get_celld().items():
            cell.set_height(0.1)
            if i==0:
                tableObj[(i, j)].set_facecolor("#df5dfc") #Purple
            elif j==0:
                tableObj[(i,j)].set_facecolor("#90EE90") #LightGreen
            else:
                tableObj[(i, j)].set_facecolor("#f4ff5e") #Yellow
            cell.set_text_props(verticalalignment='center', horizontalalignment='center')

        for i in range(len(chartLst)):
            colorDict = chartLst[i][2]
            if "H" in colorDict:
                tableObj[(colorDict["H"]+1, i+1)].set_facecolor("#03ff24") #Green
            if "R" in colorDict:
                tableObj[(colorDict["R"]+1, i+1)].set_facecolor("#60d3fc") #Blue

        legend_labels = ["Page Hit", "Replace"]
        legend_colors = ["#03ff24", "#60d3fc"]

        for i, colour in enumerate(legend_colors):
            plt.scatter([], [], color=colour, label=legend_labels[i])

        plt.legend(loc='upper right', fontsize=15, bbox_to_anchor=(1, 1), borderaxespad=0)

        plt.title(data.name + " Page Replacement", fontsize=20)
        plt.show()

    def showMemory(self, data):
        memoryData = data.visualdata

        n = len(memoryData)

        plt.figure(figsize=(12, 4))
        plt.axis("off")
        plt.xlim(0, n+1)
        plt.ylim(0, 20)
        plt.title(data.name + " Memory Status", fontsize=20)

        for i, block in enumerate(memoryData):
            if type(block)==tuple:
                bgcolor="#03ff24"
                size = str(block[1])
                txt = str(block[0])
            else:
                bgcolor="skyblue"
                size = block
                txt = "Free"
            plt.barh(15, 1, left=i, height=5, color=bgcolor, edgecolor="black")
            plt.text(i+0.5, 16, txt, color="black", fontweight="bold", ha="center", va="center")
            
            plt.text(i+0.5, 14, size, color="black", fontweight="bold", ha="center", va="center")
        plt.show()
    
    def showHeadMovement(self, data):
        movementData = copy.deepcopy(data.visualdata)
        size = len(movementData)
        plt.title(data.name + " Head Movement", fontsize=20)
        plt.xlim(0, data.disksize)
        plt.ylim(0, size+1)
        plt.gca().axes.yaxis.set_visible(False)
        line, = plt.plot([], [], color="red", linestyle="-")
        head, = plt.plot([], [], marker="o", color="blue", linestyle="")
        x = []
        y = []

        def addData(n):
            if n<size:
                x.append(movementData[n])
                y.append(size-n)
                head.set_data(x, y)
                line.set_data(x, y)
            return head, line
        
        anim = FuncAnimation(plt.gcf(), addData, frames=size, interval=500, repeat=False)
        plt.show()