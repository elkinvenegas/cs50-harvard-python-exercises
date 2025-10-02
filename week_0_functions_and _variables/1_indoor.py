# Indoor Voice
"""

WRITING IN ALL CAPS IS LIKE YELLING.

Best to use your “indoor voice” sometimes, writing entirely in lowercase.

In a file called "indoor.py", implement a program in Python that
prompts the user for input and then outputs that same input in lowercase.
Punctuation and whitespace should be outputted unchanged.
You’re welcome, but not required, to prompt the user explicitly, as by
passing a "str" of your own as an argument to input.
"""

# Solution

# N. 1

user_text = input("Please enter a message: ").lower()

print(user_text)

#or 

# N. 2

user_text = input("Please enter a message: ")

print(user_text.lower())