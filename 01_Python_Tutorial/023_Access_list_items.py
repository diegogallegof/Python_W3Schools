# Access Items
# List items are indexed and you can access them by referring to the index number:
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# Note: The first item has index 0.

# Negative Indexing
# Negative indexing means start from the end

# -1 refers to the last item, -2 refers to the second last item etc.
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new list with the specified items.
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[5])
print(thislist[2:5]) # ['cherry', 'orange', 'kiwi']
# Note: The search will start at index 2 (included) and end at index 5 (not included).
