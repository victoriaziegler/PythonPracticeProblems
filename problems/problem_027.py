# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#

def max_in_list(values):
    if len(values) == 0:
        return None
    max_value = 0
    for value in values:
        if value > max_value:
            max_value = value
    return max_value


values = (1, 8, 5, 12)
print(max_in_list(values))

values = ()
print(max_in_list(values))
