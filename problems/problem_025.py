# Complete the calculate_sum function which accepts
# a list of numerical values and returns the sum of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#

def calculate_sum(values):
    sum = 0
    if len(values) == 0:
        return None
    for value in values:
        sum = sum + value
    return(sum)


values = ()
print(calculate_sum(values))

values2 = (1, 3, 5)
print(calculate_sum(values2))
