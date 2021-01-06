# https://docs.microsoft.com/ko-kr/learn/modules/python-lists/5-solution

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

cards = []
for suit in suits:
    for rank in ranks:
        cards.append( suit + ' of ' + rank)
#print (cards)
#cnt_cards = len(suits) * len(ranks)
print(f'There are {len(cards)} cards in the deck.')



# 카드 5장 무작위 딜을 시뮬레이트하려면 적절한 방법을 사용하여 카드를 선택합니다. 플레이어의 손을 나타내는 목록에 카드를 추가합니다. 데크를 나타내는 목록에서 카드를 제거합니다.
import random
from time import sleep

random_idx = list(range(0, 52))
random.shuffle(random_idx)
print(random_idx)
deal_idx = random_idx[:5]
print(deal_idx)
deal_cards = []
for idx in deal_idx:
    print('Dealing... ' + cards[idx])
    deal_cards.append(cards[idx])
    #print('Dealing... ' + cards[idx])
    cards.pop(idx) # pop(x)는 리스트의 x번째 요소를 돌려주고 그 요소는 삭제한다. pop()은 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제한다.
    sleep(1) # 1 second sleep

print(f'There are {len(cards)} cards in the deck.')
print('Player has the following cards in her/his hand:')
print(deal_cards)

