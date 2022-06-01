# Complete the is_inside_bounds function which takes an x
# coordinate and a y coordinate, and then tests each to
# make sure they're between 0 and 10, inclusive.

def is_inside_bounds(x, y):
    if (x < 10 and x > 0) and (y < 10 and y > 0):
        return True
    return False


x = 1
y = 4
print(is_inside_bounds(x, y))


x2 = 1
y2 = 11
print(is_inside_bounds(x2, y2))