#Get to correct working directory
import os
os.chdir('/home/morgan/Documents/_Programming/challenges/Advent-of-Code-2023/day1')

#read input file
with open("input.txt", "r") as input:
    calibration_doc = input.readlines()

array = []
line_values = []

#create array of strings for each line
def get_line(calibration_doc):
    for line in calibration_doc:
        array.append(line)

def check_nums(string):
    value = ""
    num_array = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    #reverse_num_array = ['eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin']
    for num in num_array:
        if num in string:
            index = num_array.index(num)
            value = str(index+1)
            continue
    return value
    
def get_first_num(line):
    first_num = ""
    analyzed_string = ""
    for char in line:
        if char.isdigit():
            first_num = char
            break
        else:
            analyzed_string += char
            #print("Analyzed String: ", analyzed_string)
            #print("Result of check_nums():", check_nums(analyzed_string))
            if check_nums(analyzed_string) != "":
                first_num = check_nums(analyzed_string)
                break
    #print("First Num: ", first_num)
    return first_num

def get_last_num(line):
    last_num = ""
    analyzed_string = ""
    for char in reversed(line):
        if char.isdigit():
            last_num = char
            break
        else:
            analyzed_string = char + analyzed_string
            if check_nums(analyzed_string) != "":
                last_num = check_nums(analyzed_string)
                break
    #print("Last Num: ", last_num)
    return last_num

#creates array of each calibration value as ints, then totals all of them
def combine_values(array):
    for line in array:
        digit1 = get_first_num(line)
        digit2 = get_last_num(line)
        digits = int(digit1+digit2)
        line_values.append(digits)
    sum = 0
    for num in line_values:
        sum += num
    return sum

get_line(calibration_doc)
print(combine_values(array))