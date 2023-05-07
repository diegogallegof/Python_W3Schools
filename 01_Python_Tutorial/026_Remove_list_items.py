# Remove Specified Item
# The remove() method removes the specified item.
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# ValueError: list.remove(x): x not in list
# Remove Specified Index
# The pop() method removes the specified index.

# Example
# Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# If you do not specify the index, the pop() method removes the last item.
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Remove the last item:

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
# The del keyword also removes the specified index:
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)