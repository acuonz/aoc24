import numpy as np

text = np.genfromtxt("input_1.txt", delimiter='   ', dtype=int)

row0 = np.sort(text[:,0])
row1 = np.sort(text[:,1])
diff = row0-row1
print(sum(abs(diff)))
