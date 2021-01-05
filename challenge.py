# https://docs.microsoft.com/ko-kr/learn/modules/python-if-elif-else/4-challenge
# 사용자가 no 또는 n으로 응답하면 Exiting 구문을 출력합니다.
# 사용자가 yes 또는 y로 응답하면 Continuing ... 및 Complete! 구문을 출력합니다.
# 사용자가 다른 응답을 하면 Please try again and respond with yes or no. 구문을 출력합니다.

x = 6
print(x > 3 or x < 5)

#print('Would you like to continue?')
yes_no = input('Would you like to continue?')
if yes_no == 'no' or yes_no == 'n':
    print('Exiting')
elif yes_no == 'yes' or yes_no == 'y':
    print('Continuing ...')
    print('Complete!')
else:
    print('Please try again and respond with yes or no.')


