
import matplotlib.pyplot as plt

with open("Goals.txt", "r") as goalData:
    homeTeamLine = goalData.readline()
    homeTeamLine = homeTeamLine.strip(" \n")
    homeTeamLine = homeTeamLine.split(" ")
    homeTeamGoals = [int(x) for x in homeTeamLine]
    
    awayTeamLine = goalData.readline()
    awayTeamLine = awayTeamLine.strip(" \n")
    awayTeamLine = awayTeamLine.split(" ")
    awayTeamGoals = [int(x) for x in awayTeamLine]
    
x = []
for i in range(1, len(homeTeamGoals)+1):
    x.append(i)

fig2 = plt.figure("Second", figsize = (6,6))
ax1 = fig2.add_subplot(1,1,1)

ax1.boxplot(x = [homeTeamGoals, awayTeamGoals], sym = "+", whis = [10,90],
            notch = True, conf_intervals = [[0.9, 1.1], [0.2, 1.9]])
#positions = [0.5,5], #widths = 0.1

ax1.set_ylim(0,7)
plt.show()