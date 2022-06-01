# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"


def gear_for_day(is_workday, is_sunny):
    day = []
    for gear in day:
        if day == is_workday and day != is_sunny:
            day.append('laptop' + 'umbrella')
        elif day != is_sunny:
            day.append('umbrella')
        elif day != is_workday:
            day.append('surfboard')
        return day
