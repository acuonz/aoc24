import numpy as np
score = 0
text = np.genfromtxt("day1/input_1.txt", delimiter='   ', dtype=int)

row0 = np.sort(text[:,0])
row1 = np.sort(text[:,1])
diff = row0-row1
print(sum(abs(diff)))
for i in range(len(row0)):
    score += (row0[i]*len(np.where(row1 == row0[i])[0]))
print(score)