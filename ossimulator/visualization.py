import matplotlib.pyplot as plt
class Visualize:

    def ganttchart(self, data):
        chartLst = data.chartdata
        n = len(chartLst)

        plt.figure(figsize=(12, 4))
        plt.xlim(0, n+1)
        plt.ylim(0, 30)
        plt.title(data.name + " Gantt Chart")
        plt.xticks([])
        plt.yticks([])
        plt.text(0.1, 11, "0", color="black", fontweight="bold", ha="center", va="center")

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

    