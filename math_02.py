# https://docs.microsoft.com/ko-kr/learn/modules/python-datatypes-numeric-operations/6-solution
fahrenheit = input('What is the temperature in Fahrenheit?')
if fahrenheit.isnumeric() == False:
    print('Input is not a number')
    exit()

fahrenheit = int(fahrenheit)

celsius = int((fahrenheit - 32) * 5/9)
print('Temperature in celsius is ' + str(celsius))

