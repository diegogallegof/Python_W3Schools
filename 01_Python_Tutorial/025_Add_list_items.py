# Python - Add List Items
# Append Items
# To add an item to the end of the list, use the append() method:
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
# Insert Items
# To insert a list item at a specified index, use the insert() method.

# The insert() method inserts an item at the specified index:
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
# Note: As a result of the examples above, the lists will now contain 4 items.
# Extend List
# To append elements from another list to the current list, use the extend() method.
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)