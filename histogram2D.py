
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

#plt.hist2d(x = homeTeamGoals, y = awayTeamGoals, bins = [range(8), range(7)],
#           cmap = plt.cm.jet_r)

#plt.colorbar()

cmap = plt.cm.get_cmap("jet", 8)
colors = cmap(range(8))
n, bins, patches= ax1.hist(homeTeamGoals, bins = range(8))

#for i in range(len(colors)):
#   color = colors[i]
#    patch = patches[i]

for color, patch in zip(colors, patches):
    patch.set_facecolor(color)
plt.show()