#https://docs.microsoft.com/ko-kr/learn/modules/python-standard-library/4-exercise-pip
################################################
# py -m pip install emoji
################################################
# import없이 이하와 같이 유니코드로 바로 호출 가능
print("\U0001f600")
print("winking face:" + "\N{winking face}")
print('sun with face:' + '\N{sun with face}') 

import emoji
message = emoji.emojize('Howdy :sun_with_face:') 
print(message)
# AttributeError: partially initialized module 'emoji' has no attribute 'emojize' (most likely due to a circular import)
# SOLUTION) import 하려는 모듈과 같은 이름으로 파일을 생성하지 말 것!!!

# py -m pip install --upgrade pip
