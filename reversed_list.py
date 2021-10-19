"""
Task #2
# reverse the string
# e.g. new_string = 'desrever eb ot'
"""
string = 'to be reversed'

#Option 1
reversed_string = string[::-1]
print(f"Here is reversed string '{reversed_string}' of the string '{string}'")


#Option 2
def reversed_string():
    new_str = ''.join(reversed(string))
    print(f"\nReversed string of the '{string}' is '{new_str}'")
    return new_str

reversed_string()












