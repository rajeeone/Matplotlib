
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Rectangle

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
ax1 = fig2.add_subplot(1,1,1)

N, bins, patches = ax1.hist(x = (homeTeamGoals, awayTeamGoals), bins = [0,1,2,3,4,5,6,7],#int/sequence/range(8)
         align = "mid", color = ("red", "blue"), cumulative = False)

print(N)
#N[0], N[1], N[1][0]

print(patches)
patches[1][1].set_facecolor("green")
patches[1][1].set_width(0.5)

redRectangle = Rectangle((0,0), 1, 1, color = "red")
blueRectangle = Rectangle((0,0), 1, 1, color = "blue")

Boxes = [redRectangle, blueRectangle, patches[1][1]]
#patches[0][0], patches[1][0]
labels = ["HomeTeamGoals", "AwayTeamGoals", "Special"]

plt.legend(Boxes, labels)

plt.show()