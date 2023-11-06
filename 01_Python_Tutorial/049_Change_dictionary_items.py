# Change Values
# You can change the value of a specific item by referring to its key name:
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Change the "year" to 2018:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.

# The argument must be a dictionary, or an iterable object with key:value pairs.

# Example
# Update the "year" of the car by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})