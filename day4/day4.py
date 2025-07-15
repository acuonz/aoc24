import numpy as np
SIZE = 140
count = 0
text = np.genfromtxt("day4/input4.txt", delimiter=1, dtype=str)
# top left to bottom right horiz
for i in range(SIZE):
    test_string = ''
    for j in range(SIZE):
        test_string += text[i][j]
        print(test_string)
    count += test_string.count("XMAS")

# bottom right to to left horiz
for i in range(SIZE-1,-1,-1):
    test_string = ''
    for j in range(SIZE-1,-1,-1):
        test_string += text[i][j]
        print(test_string)
    count += test_string.count("XMAS")

# top left to bottom right vert
for i in range(SIZE):
    test_string = ''
    for j in range(SIZE):
        test_string += text[j][i]
        print(test_string)
    count += test_string.count("XMAS")

# bottom right to to left vert
for i in range(SIZE-1,-1,-1):
    test_string = ''
    for j in range(SIZE-1,-1,-1):
        test_string += text[j][i]
        print(test_string)
    count += test_string.count("XMAS")

# top left to bottom right diag
for i in range(SIZE-3):
    
    for j in range(SIZE-3):
        test_string = ''
        for k in range(4):
            test_string += text[i+k][j+k]
        count += test_string.count("XMAS")

# top right to bottom left diag
for i in range(SIZE-3):
    
    for j in range(SIZE-1,2,-1):
        test_string = ''
        for k in range(4):
            test_string += text[i+k][j-k]
        count += test_string.count("XMAS")
# bottom right to top left diag
for i in range(SIZE-1,2,-1):
    
    for j in range(SIZE-1,2,-1):
        test_string = ''
        for k in range(4):
            test_string += text[i-k][j-k]
        print(test_string)
        count += test_string.count("XMAS")

# bottom left to top right diag
for i in range(SIZE-1,2,-1):
    
    for j in range(SIZE-3):
        test_string = ''
        for k in range(4):
            test_string += text[i-k][j+k]
        print(test_string)
        count += test_string.count("XMAS")

for i in range(SIZE-3):
    print(i)
print(count)