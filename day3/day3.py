with open("day3/input3.txt", "r") as file:
    count = 0
    is_do = True
    while True:
        
        line = file.readline()
        if not line: # Check for EOF (empty string)
            break
        for i in range(len(line)):
            num1_1digit = False
            num1_2digit = False
            num1_3digit = False
            num2_1digit = False
            num2_2digit = False
            num2_3digit = False
            has_comma = False
            ends_in_para = False
            if(line[i:].find("do()") == 0):
                
                is_do = True
            if(line[i:].find("don't()") == 0):
                is_do = False
            if(line[i:i+4] == "mul("):
                if(line[i+4:i+7].isdigit()):
                    num1_3digit = True
                    end_index = i+7
                    digit1 = int(line[i+4:i+7])
                elif(line[i+4:i+6].isdigit()):
                    num1_2digit = True
                    end_index = i+6
                    digit1 = int(line[i+4:i+6])
                elif(line[i+4:i+5].isdigit()):
                    num1_1digit = True
                    end_index = i+5
                    digit1 = int(line[i+4:i+5])
                if(line[end_index] == ','):
                    has_comma = True
                if(line[end_index+1:end_index+4].isdigit()):
                    num2_3digit = True
                    digit2 = int(line[end_index+1:end_index+4])
                    end_index = end_index+4
                elif(line[end_index+1:end_index+3].isdigit()):
                    num2_2digit = True
                    digit2 = int(line[end_index+1:end_index+3])
                    end_index = end_index+3
                elif(line[end_index+1:end_index+2].isdigit()):
                    num2_1digit = True
                    digit2 = int(line[end_index+1:end_index+2])
                    end_index = end_index+2
                if(line[end_index] == ')'):
                    ends_in_para = True
            valid = (num1_1digit or num1_2digit or num1_3digit) and (num2_1digit or num2_2digit or num2_3digit) and has_comma and ends_in_para and is_do
            if (valid):
                count += digit1 * digit2
    print(count)
                