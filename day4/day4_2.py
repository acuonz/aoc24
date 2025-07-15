import numpy as np
SIZE = 140
count = 0
text = np.genfromtxt("day4/input4.txt", delimiter=1, dtype=str)
# top left to bottom right horiz
for i in range(1,SIZE-1,1):
    for j in range(1,SIZE-1,1):
        is_A = True if text[i][j] == 'A' else False
        if((text[i+1][j+1] == 'S' and text[i-1][j-1] == 'M') or
           (text[i+1][j+1] == 'M' and text[i-1][j-1] == 'S')):
            is_diag1 = True
        else:
            is_diag1 = False
        if((text[i+1][j-1] == 'S' and text[i-1][j+1] == 'M') or
           (text[i+1][j-1] == 'M' and text[i-1][j+1] == 'S')):
            is_diag2 = True
        else:
            is_diag2 = False
        if(is_A and is_diag1 and is_diag2):
            count += 1
    
print(count)