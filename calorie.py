# 현재 날짜(임의의 형식)
# 섭취한 조식 칼로리
# 섭취한 중식 칼로리
# 섭취한 석식 칼로리
# 섭취한 간식 칼로리

from datetime import datetime
today = datetime.today().strftime("%Y/%m/%d %H:%M:%S")

print("Today's date?")
print(today)
print(datetime.today())

print("Breakfast calories?")
breakfast_calories = int(input())
print("Lunch calories?")
lunch_calories = int(input())
print("Dinner calories?")
dinner_calories = int(input())
print("Snack calories?")
snack_calories = int(input())

total_calories = breakfast_calories + lunch_calories + dinner_calories + snack_calories

print("Calorie content for " + datetime.today().strftime("%A") + ":" + str(total_calories))