# Complete the is_inside_bounds function which has the
# following parameters:
#   x: the x coordinate to check
#   y: the y coordinate to check
#   rect_x: The left of a rectangle
#   rect_y: The top of a rectangle
#   rect_width: The width of the rectangle
#   rect_height: The height of the rectangle
#
# The is_inside_bounds function returns true if all of
# the following are true
#   * x is greater than or equal to rect_x
#   * y is greater than or equal to rect_y
#   * x is less than or equal to rect_x + rect_width
#   * y is less than or equal to rect_y + rect_height

def is_inside_bounds(x, y, rect_x, rect_y, rect_width, rect_height):
    rect_x_specs = rect_x + rect_width
    rect_y_specs = rect_y + rect_height
    rect_x_range = range(rect_x, rect_x_specs)
    rect_y_range = range(rect_y, rect_y_specs)
    if (x in rect_x_range) and (y in rect_y_range):
        return True
    return False

