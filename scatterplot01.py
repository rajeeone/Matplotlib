

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter

with open("Goals.txt", "r") as goalData:
    homeTeamLine = goalData.readline()
    homeTeamLine = homeTeamLine.strip(" \n")
    homeTeamLine = homeTeamLine.split(" ")
    homeTeamGoals = [int(x) for x in homeTeamLine]
    
    awayTeamLine = goalData.readline()
    awayTeamLine = awayTeamLine.strip(" \n")
    awayTeamLine = awayTeamLine.split(" ")
    awayTeamGoals = [int(x) for x in awayTeamLine]

majorTickLocation = MultipleLocator(1)
minorTickLocation = MultipleLocator(1)    
fig1 = plt.figure("First Figure", figsize = (10,6),facecolor = "g")
fig2 = plt.figure("Second Figure", figsize = (10,10),facecolor = "r")
    
ax1 = fig1.add_subplot(3,3,2)
ax1.set_xlim(-1,7)
ax1.set_ylim(-1,6)
ax1.xaxis.set_major_locator(majorTickLocation)
ax1.yaxis.set_major_locator(minorTickLocation)
majorTickFormat = FormatStrFormatter("%02d")
ax1.xaxis.set_major_formatter(majorTickFormat)
ax1.yaxis.set_major_formatter(majorTickFormat)
ax1.scatter(homeTeamGoals, awayTeamGoals, s=70, c = [1,0,1], 
            marker = "*", alpha = 0.5)
ax2 = fig1.add_subplot(3,1,3)
ax2.set_xlim(-1,7)
ax2.set_ylim(-1,6)
ax2.xaxis.set_major_locator(majorTickLocation)
ax2.yaxis.set_major_locator(minorTickLocation)
ax1.xaxis.set_major_formatter(majorTickFormat)
ax1.yaxis.set_major_formatter(majorTickFormat)
ax2.xaxis.set_major_formatter(majorTickFormat)
ax2.yaxis.set_major_formatter(majorTickFormat)
ax2.scatter(homeTeamGoals, awayTeamGoals, s=70, c = "#FAAACA", 
            marker = "*", alpha = 0.5)

axList  = []
for i in range(1,10):
    axList.append(fig2.add_subplot(3,3,i))
    #plt.figure("First Figure")
    plt.scatter(homeTeamGoals, awayTeamGoals, s=70, c = range(len(homeTeamGoals)), 
                marker = "*", alpha = 0.5)
    

    

plt.show()
    
