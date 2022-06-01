# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you

def calculate_average(values):
    sum = 0
    number_items = len(values)
    if number_items == 0:
        return None
    for value in values:
        sum = sum + value
        average = sum / number_items
    return(average)


values = (1, 3, 5)
print(calculate_average(values))

values2 = ()
print(calculate_average(values2))
