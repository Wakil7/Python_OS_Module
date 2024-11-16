import matplotlib.pyplot as plt
import copy
class Visualize:

    def ganttchart(self, data):
        chartLst = copy.deepcopy(data.chartdata)
        n = len(chartLst)

        plt.figure(figsize=(12, 4))
        plt.axis("off")
        plt.xlim(0, n+1)
        plt.ylim(0, 20)
        plt.title(data.name + " Gantt Chart")
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
        plt.show()

    def replacementtable(self, data):
        chartLst = copy.deepcopy(data.chartdata)
        chartData = []
        
        for i in range(len(chartLst[0][0])):
            tmpLst = []
            for j in range(len(chartLst)):
                tmpLst.append(chartLst[j][0][i])
            chartData.append(tmpLst)
        
        rows = [f"Frame {i}" for i in range(len(chartLst[0][0]))]
        columns = ["Pages"]+[chartLst[i][1] for i in range(len(chartLst))]

        plt.axis("tight")
        plt.axis("off")
        
        tableData = [columns] + [[rows[i]] + chartData[i] for i in range(len(rows))]
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

        plt.title(data.name, fontsize=25)
        plt.show()


    