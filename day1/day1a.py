#Get to correct working directory
import os
os.chdir('/home/morgan/Documents/_Programming/challenges/Advent-of-Code-2023/day1')

#read input file
with open("sample.txt", "r") as input:
    calibration_doc = input.readlines()

array = []
line_values = []

#create array of strings for each line
def get_line(calibration_doc):
    for line in calibration_doc:
        array.append(line)

def get_first_num(line):
    first_num = ""
    for char in line:
        if char.isdigit():
            first_num = char
            break
    return first_num

def get_last_num(line):
    last_num = ""
    for char in reversed(line):
        if char.isdigit():
            last_num = char
            break
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