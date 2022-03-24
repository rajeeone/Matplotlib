
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
    
totalHomeGoalsScored = sum(homeTeamGoals)
totalAwayGoalsScored = sum(awayTeamGoals)

fig2 = plt.figure("Second", figsize = (6,6))
ax1 = fig2.add_subplot(1,1,1)

ax1.pie(x = [totalHomeGoalsScored, totalAwayGoalsScored, 300], 
       labels = ["Home Team", "Away Team", "Rest"], labeldistance = 1.1, colors = ["orange", "red", "blue"], 
       explode =[0,0.1,0], shadow = True, radius = 0.5, center = [1,2])
#sum(x)>1 -> x[i]/sum(x)
#sum(x)<=1 -> no normalization

ax1.pie(x = [totalHomeGoalsScored, totalAwayGoalsScored, 300], 
       labels = ["Home Team", "Away Team", "Rest"], labeldistance = 1.5, colors = ["orange", "red", "blue"], 
       explode =[0, 0.1, 0], shadow = True, radius = 0.5, center = [-1,-2])

plt.show()