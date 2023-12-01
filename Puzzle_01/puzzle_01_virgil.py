# This is where I am at so far, ignore the commented out section in the middle, i have left that in for now with my original working where I was working
# on a single string.

# Where I am up to is if works through the text file line by line and gets the first and last digits, joins them together into a two digit number then keeps
# a running total adding each line to the previous total. 

# The issue I have at the moment is if the line only has a single number in it. It counts that number as both the first and last digit and makes a two digit
# number of the same values... eg. line 7 "onedpsckg3xdhmgtsixthreefivejlncszkxeight"returns the value 33 as the 3 is both the first and last digit.

#Finds the value of the first digit in a string
def find_first_digit(string):
    for char in string:
        if char.isdigit():
            return int(char)
    return None
#Finds the value of the last digit in a string
def find_last_digit(string):
    for char in reversed(string):
        if char.isdigit():
            return int(char)
    return None

RUNNING_TOTAL = 0
#input_string = "jbdkj2jansld23sad"

# Finds the values in the current string
##last_digit = find_last_digit(input_string)

#converts the two digits into string value so I can join them together
#first_digit_str = str(first_digit)
#last_digit_str = str(last_digit)
#final_digit = first_digit_str + last_digit_str

#Converts it back to an Integer so i can use it later to add all rows together.
#final_digit_int = int(final_digit)

#Check work row
#print(final_digit_int)

#moves the above stuff down and runs it per line
with open("task_1.txt") as INPUT_FILE:
    for line in INPUT_FILE:
        input_string = line
        first_digit = find_first_digit(input_string)
        last_digit = find_last_digit(input_string)

        #converts the two digits into string value so I can join them together
        first_digit_str = str(first_digit)
        last_digit_str = str(last_digit)
        join_digit = first_digit_str + last_digit_str

        #Converts it back to an Integer so i can use it later to add all rows together.
        join_digit_int = int(join_digit)

        #takes the running total and adds the current 2 digit number to it, then moves to the next line. 
        RUNNING_TOTAL = RUNNING_TOTAL + join_digit_int

        #Prints the running total per line but could move this out of the for loop to just have the final total, see issues at top though. 
        print(RUNNING_TOTAL)
