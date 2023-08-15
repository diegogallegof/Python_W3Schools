# Add Items
# Once a set is created, you cannot change its items, but you can add new items.

# To add one item to a set use the add() method.
# ----------------------------------------------------------------
# Example
#----------------------------------------------------------------
# Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# Add Sets
# To add items from another set into the current set, use the update() method.
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)