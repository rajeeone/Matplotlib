import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
#from matplotlib.patches import Rectangle

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
    
avgGoalsScoredHome = sum(homeTeamGoals)/len(homeTeamGoals)
avgGoalsScoredAway = sum(awayTeamGoals)/len(awayTeamGoals)

fig2 = plt.figure("Second", figsize = (6,6))
ax1 = fig2.add_subplot(1,1,1)

ax1.bar(x = [1.5,2], height = [avgGoalsScoredHome, avgGoalsScoredAway], 
       width = 0.1, align = "center", color = ["red", "black"], bottom = [0.2,0.1])

ax1.bar(x = [1,1], height = [avgGoalsScoredHome, avgGoalsScoredAway], 
        width = 0.15, align = "center", color = ["red", "orange"], bottom = [0, avgGoalsScoredHome],
        xerr = [[0.1, 0.2],[0.2, 0.1]], yerr = [[0.1, 0.05],[0.1, 0.3]], ecolor = "blue")

plt.xticks([1,2], ["Home Team", "Away Team"])
ax1.set_ylim(0,4)
ax1.set_xlim(0.5,2.5)



plt.show()
