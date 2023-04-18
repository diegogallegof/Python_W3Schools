# Escape Character
"""
To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.
An example of an illegal character is a double quote inside a 
string that is surrounded by double quotes:
"""
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
"""
You will get an error if you use double quotes inside a 
string that is surrounded by double quotes:

txt = "We are the so-called "Vikings" from the north."
SyntaxError: invalid syntax
To fix this problem, use the escape character \":
"""
# Example
"""
The escape character allows you to use double quotes when you normally would not be allowed:
"""
txt = "We are the so-called \"Vikings\" from the north."

# Escape Characters
# Other escape characters used in Python:

# Code	Result	Try it
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value