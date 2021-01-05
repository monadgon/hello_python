# print(), input(), int(), str(), type(), isinstance(), isnumeric()
print(type('7'))  # <class 'str'>
print(type(7))    # <class 'int'>
print(type(7.1))  # <class 'float'>

print(isinstance('7', str))  #True
print(isinstance(7, int))    #True
print(isinstance(7.1, float))#True

print(type('7') == str)   # True
print(type(7) == int)     # True
print(type(7.1) == float) # True

x = 'a string'
print(type(x)) # <class 'str'>
x = 7
print(type(x)) # <class 'int'>
x = False 
print(type(x)) # <class 'float'>

#isalnum()	문자열에 %, $, #, @ 또는 ! 같은 특수 문자가 없도록 합니다.
#isalpha()	문자열에 알파벳 문자만 포함되도록 합니다.
#isdecimal()	문자열에 10진수 값(숫자)만 포함되도록 합니다.
#istitle()	문자열이 (문장에서처럼) 대문자 표시 규칙을 따르도록 합니다.
#isupper()	문자열에 대문자만 포함되도록 합니다.
#islower()	문자열에 소문자만 포함되도록 합니다.

first_value = 5
second_value = 4

sum = first_value + second_value
difference = first_value - second_value
product = first_value * second_value
quotient = first_value / second_value
modulus = first_value % second_value
exponent = first_value ** second_value 

print('Sum: ' + str(sum))
print('Difference: ' + str(difference))
print('Product: ' + str(product))
print('Quotient: ' + str(quotient))
print('Modulus: ' + str(modulus))
print('Exponent: ' + str(exponent))

# https://docs.microsoft.com/ko-kr/learn/modules/python-datatypes-numeric-operations/4-exercise-numeric-operations

#Python은 연산을 수행해야 하는 순서를 나타내는 PEMDAS 머리글자어를 따릅니다.

#P arentheses(괄호): 괄호 사이의 연산을 먼저 해결합니다.
#E xponents(지수): 지수를 해결합니다.
#M ultiplication(곱하기): 왼쪽에서 오른쪽으로 곱하기를 수행합니다.
#D ivision(나누기): 왼쪽에서 오른쪽으로 나누기를 수행합니다.
#A ddition(더하기): 왼쪽에서 오른쪽으로 더하기를 수행합니다.
#S ubtraction(빼기): 왼쪽에서 오른쪽으로 빼기를 수행합니다.

first_value = round(7.654321, 2)
print(first_value)

second_value = round(9.87654, 3)
print(second_value)