# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.

def has_quorum(attendees_list, members_list):
    if len(attendees_list) >= (.5 * len(members_list)):
        return True
    return False


attendees_list1 = ("bob", "tori", "ludo", "charles", "saul")
members_list1 = ("bob", "tori", "ludo", "chuck")

print(has_quorum(attendees_list1, members_list1))


# attendees_list2 = ("bob", "tori")
# members_list2 = ("bob", "tori", "ludo", "charles", "saul")

# print(has_quorum(attendees_list2, members_list2))
