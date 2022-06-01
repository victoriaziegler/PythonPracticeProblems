# Complete the calculate_grade function which accepts
# a list of numerical scores each between 0 and 100.
#
# Based on the average of the scores, the function
# returns
#   * An "A" for an average greater than or equal to 90
#   * A "B" for an average greater than or equal to 80
#     and less than 90
#   * A "C" for an average greater than or equal to 70
#     and less than 80
#   * A "D" for an average greater than or equal to 60
#     and less than 70
#   * An "F" for any other average

def calculate_grade(values):
    sum = 0
    for value in values:
        sum = sum + value
        average = sum / (len(values))
    if average >= 90:  
        return "A"
    if average >= 80:  
        return "B"  
    if average >= 70:  
        return "C"  
    if average >= 60:  
        return "D"
    else:
        return "F"


values = (90, 85, 90, 94, 94)
print(calculate_grade(values))

values2 = (60, 85, 50, 74, 94)
print(calculate_grade(values2))