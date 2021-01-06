import random 

print('########## range, shuffle #################')
list_data = list(range(1,46)) # 1 ~ 45 범위의 숫자를 순서대로 리스트 형태로 가져온다.
print(list_data)              # 1 ~ 45
random.shuffle(list_data)     # list_data 자체의 값이 변경된다. by reference
print('shuffled:\n' + str(list_data))
list_data = list_data[:6]    # 앞에서 6개를 가져오기
list_data.sort()             # list_data 자체를 소팅한다.
print(list_data)

#  while을 사용하여 위와 같이 6개의 렌덤한 숫자를 가져오기
print('########## using while, randint #################')
list_data = list()   # 빈 리스트를 만든다.
#print(list_data)     # []

while True:
    my_random = random.randint(1, 45) # including both end points
    if not (my_random in list_data):
        list_data.append(my_random)
    if len(list_data) >= 6:
        break

list_data.sort()
print(list_data)



