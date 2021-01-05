# https://docs.microsoft.com/ko-kr/learn/modules/python-format-strings/5-challenge
# https://docs.microsoft.com/ko-kr/learn/modules/python-format-strings/6-solution
first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge

print( len(first_value) ) #26
print ( first_value.count(' ')) #12
# strip() returns a copy of the string with both leading and trailing characters removed #FIRST challenge
print('*' + first_value.strip() + '*') # *FIRST challenge*
print('*' + first_value.lower() + '*') # *  first challenge         *
print('*' + first_value.title() + '*') #   First Challenge         *
print('*' + f'{first_value:^30}' + '*')        #*    FIRST challenge           *
print('*' + first_value.center(30, ' ') + '*') #*    FIRST challenge           *
print('*' + first_value.ljust(30) + '*') #*    FIRST challenge           *
print('*' + first_value.rjust(30) + '*') #*    FIRST challenge           *

# Second challenge
print('*' + second_value.replace('-', '') + '*')
print('*' + second_value.replace('-', '').strip() + '*')
print('*' + second_value.capitalize() + '*')
print('*' + second_value.replace('-', '').strip().capitalize() + '*')

# Third challenge
print('*' + third_value.replace(' ', '') + '*')
print('*' + third_value.replace('-', ' ') + '*')
print('*' + third_value.swapcase() + '*')
print('*' + f'{third_value:>30}' + '*')

# Fourth challenge - use only the print() function (no f-strings)
print(fourth_value, fifth_value, sixth_value, sep='#', end='!')
print()

# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
print(f'\t{fourth_value}\n\t{fifth_value}\n\t{sixth_value}')
