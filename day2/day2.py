import numpy as np
def check_list(arr):
        
    sort_arr = np.sort(arr)
    is_sorted_forward = np.all(arr == sort_arr)
    sort_arr = np.flip(sort_arr)
    is_sorted_reverse = np.all(arr == sort_arr)
    if (not (is_sorted_forward or is_sorted_reverse)):
        return False
    if (len(np.unique(arr)) != len(arr)):
        return False
    
    for i in range(len(arr)-1):
        if(abs(arr[i] - arr[i+1]) > 3):
            return False
    
    return True

count = 0
with open("day2/input2.txt", "r") as file:
    while True:
        errors = 0
        line = file.readline()
        arr = [int(num) for num in line.split()]
        if not line: # Check for EOF (empty string)
            for i in range(len(arr)):
                tmp = arr.pop(i)
                print(arr)
                if(check_list(arr)):
                    count+=1
                    break
                arr.insert(i, tmp)
                print(arr)

        
print(count)

