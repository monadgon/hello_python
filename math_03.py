# https://docs.microsoft.com/ko-kr/learn/modules/python-datatypes-numeric-operations/8-solution-2

# 문자열이, 숫자인지 문자인지 판단 함수
def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

print('=' * 30)
print('Simple calculator!'.center(30))
print('=' * 30)

#print(30.5 * 34.9) #1064.45
#print('30.23'.isnumeric()) # False
#print('30.23'.isdigit())   # False
#print('30.23'.isdecimal()) # False


first_number = input('First number? ')
if isNumber(first_number) == False:
    print('Please input a number.')
    exit()

operation = input('Operation? ')

second_number = input('Second number? ')
if isNumber(second_number) == False:
    print('Please input a number.')
    exit()

first_number = float(first_number)
second_number = float(second_number)

result = 0
label = ''
if operation == '+':
    result = first_number + second_number
    label = 'sum'
elif operation == '-':
    result = first_number - second_number
    label = 'difference'
elif operation == '*':
    result = first_number * second_number
    label = 'product'
elif operation == '/':
    result = first_number / second_number
    label = 'quotient'
elif operation == '**':
    result = first_number ** second_number
    label = 'exponent'
elif operation == '%':
    result = first_number ** second_number
    label = 'modulus'
else:
    print('Operation not recognizsed.')
    exit()

print(label + ' of ' + str(first_number) + ' ' + operation + ' ' + str(second_number) + ' eqals ' + str(result))

