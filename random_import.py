import random 

roll = 0
count = 0

print('=' * 50)
print('Roll a dice. First person to roll a 5 wins!'.center(50))
print('=' * 50)

while roll != 5:
  name = input('Enter a name, or \'q\' to quit:  ' )

  if name.strip() == '':
    continue

  if name.strip() == 'q':
    break
  
  count = count + 1
  roll = random.randint(1, 5)
  print(f'{name} rolled {roll}')
else:
    print(f'{name} Wins!!!')

print(f'You rolled the dice {count} times.')


# https://docs.microsoft.com/ko-kr/learn/modules/python-while/5-solution
# https://docs.microsoft.com/ko-kr/learn/modules/python-while/7-solution-2

print('+' * 30)
print('Guess number'.center(30))
print('+' * 30)
print('Guess a number between 1 and 10')

#random.shuffle()
#list_data = list(range(1,46)) # 1 ~ 45
#print(list_data)              # 1 ~ 45
#random.shuffle(list_data)
#print(list_data)
#exit()

value = random.randint(1, 10)
count = 0
guess = 0
while guess != value:
    count += 1
    guess = input(f'Enter guess #{count}: ')
    if guess.isnumeric():
        guess = int(guess)
        if value < guess:
            print('Your guess is too high, try again!')
        elif value > guess:
            print('Your guess is too low, try again!')
    else:
        print('Numbers only, please!')
else:
    print(f'You guessed it in {count} tries!')

