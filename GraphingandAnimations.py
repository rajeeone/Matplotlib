

import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

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
ax1 = fig2.add_subplot(1,1,1, projection = "3d")
ax1.plot(xs = x, ys = homeTeamGoals, zs = awayTeamGoals)
ax1.set_xlabel("Game number")
ax1.set_ylabel("HomeTeamGoals")
ax1.set_zlabel("awayTeamGoals")
ax1.set_title("3D Line Plots")
ax1.text(10, 10, 10, "goals", horizontalalignment = "center", verticalalignment = "bottom", 
         style = "oblique", weight = 100)
ax1.plot(xs = x, ys = homeTeamGoals, zs = awayTeamGoals)
ax1.view_init(45,60) #elevation angle(top to bottom), rotation angle(left to right)

for angle in range(0,360):
    ax1.view_init(30, angle)
    plt.draw()
    plt.pause(0.01)

fig1 = plt.figure("First Figure", figsize = (10,10))
ax2 = fig1.add_subplot(1,1,1, projection = "3d")
ax2.set_xlabel("Game number")
ax2.set_ylabel("HomeTeamGoals")
ax2.set_zlabel("awayTeamGoals")
ax2.set_title("3D Scatter Plots")
ax2.text(2, 2, 2, "goals", horizontalalignment = "center", verticalalignment = "bottom", 
         style = "oblique", weight ="bold")
ax2.scatter(xs = x, ys = homeTeamGoals, zs = awayTeamGoals, s = 20, color = "blue", 
            depthshade = True)

ax2.view_init(45, 60) #elevation angle(top to bottom), rotation angle(left to right)

for angle in range(0,360):
    ax2.view_init(angle, angle)
    plt.draw()
    plt.pause(0.01)
plt.show()