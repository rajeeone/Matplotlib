

import matplotlib.pyplot as plt

#print(plt.style.available)
plt.style.use("grayscale")

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


fig2 = plt.figure("Second Figure", figsize = (10,10))
ax1 = fig2.add_subplot(3,3,3)
#ax1 = fig2.add_subplot(3,1,3)
ax1.plot(x, homeTeamGoals, color = "orange", marker = "^", markerfacecolor = "r",
         markersize = 4, linestyle = ":", linewidth = 2, label = "HTG")

ax1.plot(x, awayTeamGoals, color = "green", marker = "^", markerfacecolor = "g",
         markersize = 3, linestyle = ":", linewidth = 2, label = "ATG")

ax1.scatter(x, awayTeamGoals, color = "red", s = 20)

ax2 = fig2.add_subplot(3,3,1)
#ax2 = fig2.add_subplot(3,1,1)

ax2.plot(x, homeTeamGoals, color = "red", marker = "^", markerfacecolor = "r",
         markersize = 4, linestyle = ":", linewidth = 2, label = "HTG")

ax3 = fig2.add_subplot(3,3,2)
#ax3 = fig2.add_subplot(3,1,2)

ax3.plot(x, awayTeamGoals, color = "blue", marker = "^", markerfacecolor = "r",
         markersize = 4, linestyle = ":", linewidth = 2, label = "ATG")
ax1.set_xlim(-10,150)
ax1.set_ylim(-0.5,6.5)

ax1.set_title("Home and Away Team Goals", loc = "center", fontdict = {"fontsize":12})
ax2.set_title("Home Team Goals", loc = "center", fontdict = {"fontsize":12}) 
ax3.set_title("Away Team Goals", loc = "center", fontdict = {"fontsize":12})  
#add equations into text
#ax1.set_title(r"$\frac{1}{2}$)


ax1.set_xlabel("Game number", labelpad = 1, fontdict = {"rotation": 0})
ax2.set_xlabel("Game number", labelpad = 1, fontdict = {"rotation": 0})
ax3.set_xlabel("Game number", labelpad = 1, fontdict = {"rotation": 0})

ax1.set_ylabel("HTG and ATG", labelpad = 1, fontdict = {"rotation": 90})
ax2.set_ylabel("HTG", labelpad = 1, fontdict = {"rotation": 90})
ax3.set_ylabel("ATG", labelpad = 1, fontdict = {"rotation": 90})



ax1.spines["right"].set_visible(False)
ax1.spines["top"].set_visible(False)
#ax1.yaxis.set_ticks_position("left")
#axis1.yaxis.set_ticks([])
ax2.spines["right"].set_visible(False)
ax2.spines["top"].set_visible(False)
ax3.spines["right"].set_visible(False)
ax3.spines["top"].set_visible(False)

ax1.legend(loc = "upper right", fontsize = 5)
ax2.legend(loc = "best", fontsize = 5)
ax3.legend(loc = "upper right", fontsize = 5)

#plt.savefig("Images/Test.png", orientation = "portrait", dpi = 100)
plt.show()
    
