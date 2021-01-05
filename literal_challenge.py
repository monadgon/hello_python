# https://docs.microsoft.com/ko-kr/learn/modules/python-format-strings/5-challenge
first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
first_value = first_value.strip() # returns a copy of the string with both leading and trailing characters removed 
print('#' + first_value + '#')

print(first_value.title())

# Second challenge
print(second_value.ljust(20))

# Third challenge
print(third_value.rjust(20))

print(first_value)
print(second_value)
print(third_value)

# Fourth challenge - use only the print() function (no f-strings)


# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
