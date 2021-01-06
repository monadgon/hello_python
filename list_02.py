import random
numbers = []

while len(numbers) < 5:
  numbers.append(random.randint(1, 100))

for number in numbers:
  print(number)
  if number >= 90:
    print('Found at least one number greater than 90')
    break
else:
  print('No numbers greater than 90')

print('Complete')

########################## continue ###############################
values = ["laptop", 7, "phone", 3, "dslr", 5]
equipment = []

for value in values:
  if isinstance(value, str) == False:
    continue
  equipment.append(value)

print(equipment)


################### 중첩 for loop ##################################################
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

for  suit in suits:
  for rank in ranks:
    print(f'{rank} of {suit}')


########### random.choices(obj) 무작위로 선택 ##################################
## random.choices(sequence, weights=None, cum_weights=None, k=1)
# sequence	Required. A sequence like a list, a tuple, a range of numbers etc.
# weights	Optional. A list were you can weigh the possibility for each value. Default None
# cum_weights	Optional. A list were you can weigh the possibility for each value, only this time the possibility is accumulated.
#                       Example: normal weights list: [2, 1, 1] is the same as this cum_weights list; [2, 3, 4]. Default None
# k	Optional. An integer defining the length of the returned list

import random

numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
selected_number = random.choice(numbers)
print(selected_number)

selected_numbers = random.choices(numbers, k=3)
print(selected_numbers)

