colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

# print(f'0-based indexing into the list ... second item: {colors[1]}')

print(f'Last item of the list: {colors[-1]}') # brown

# print(f'Next to last item in the list: {colors[-2]}')

# 슬라이스(:)한 것의 마지막 인덱스는 포함되지 않는다.
print('\nPrint a SLICE, starting at index 2 and excluding index 5:')
print(colors[2:5]) # ['blue', 'yellow', 'orange']
print(type(colors[2:5]))

print('\nPrint a slice, starting at index 0 to index 2 (excluding index 3):')
print(colors[:3]) # ['red', 'green', 'blue']

print('\nPrint a slice, starting a index 4 to the end of the list:')
print(colors[4:]) # ['orange', 'purple', 'brown']

print('\nPrint a slice, from the 4th from the end (but not the last item):')
print(colors[-4:-1]) # ['yellow', 'orange', 'purple']


# reverse(), sort()
colors.reverse()
print(colors)

colors.sort()
print(colors)

print(colors)

color = colors.pop(0)
print('popped', color)

print(colors)

#### append(''), remove('') ####

colors.append('black')
colors.append('white')

colors.remove('yellow')
colors.remove('orange')

print(colors)

#### extend(obj) ####

new_colors = ['lime', 'gray']
colors.extend(new_colors)
print(colors)

#### clear everthing ####
print(colors)
colors.clear()
print(colors)