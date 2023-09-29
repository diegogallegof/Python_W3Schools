# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:

# Example
# Get the value of the "model" key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

# There is also a method called get() that will give you the same result:
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Get the value of the "model" key:

x = thisdict.get("model")