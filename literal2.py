message = str.capitalize('first message')
print(message)

message = 'second message'.capitalize()
print(message)

message = 'third message'
print(message.capitalize())

print('---------------')

message = 'hello world'
print(message.lower())
print(message.upper())

message = message.title()
print('str.title():' + message) # Hello World
print(message.swapcase())

print('---------------')

location = 'MississippiS'
print(location.count('s')) #대소문자 구분함
print(len('how many letters in this string?'))
message = 'racecar'
print(message.startswith('r'))
print(message.startswith('a'))
print(message.startswith('ra'))

print(message.endswith('r'))
print(message.endswith('a'))
print(message.endswith('ar'))

message = 'The quick brown fox jumps over the lazy dog'
print(message.find('q')) # 4

print(message.find('t')) # 31
print(message.find('T')) # 0

message = '    middle     '
print('.' + message.lstrip() + '.')
print('.' + message.rstrip() + '.')
print('.' + message.strip() + '.')

message = 'brevity is the essence of wit'
message = message.replace('essence', 'soul')
print(message)

message = 'howdy'
print(message.rjust(20))
print(message.rjust(20, '-'))
print('*' + message.ljust(20) + '*')
print(message.ljust(20, '-'))