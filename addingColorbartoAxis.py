
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

counts, xedges, yedges, Image = ax1.hist2d(x=homeTeamGoals, y=awayTeamGoals,
                                bins = [range(8),range(7)], cmap = plt.cm.jet)

extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

#print(yedges)

im = ax1.imshow(counts, extent=extent)   #M*N*4

fig2.colorbar(im,ax=ax1)

#plt.colorbar()

plt.show()

#img = plt.imread("Images/Test.png")
#plt.imshow(img)