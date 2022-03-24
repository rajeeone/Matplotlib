
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

fig2 = plt.figure("Second", figsize = (6,6))
ax1 = fig2.add_subplot(1,1,1)

img = mpimg.imread("Images/Test.png")
ax1.imshow(img) #M * N * 3

#2x2
#[[1,2],[3,4]]-> [RGB(A),RGB(A)],[RGB(A),RGB(A)]
#RGB(A) = [R,G,B,(A)]
#1 2   x...
#3 4  x....
#y ... ..
#... ... ...

plt.show()