import random
from time import sleep 

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
deck = []

for  suit in suits:
  for rank in ranks:
    deck.append(f'{rank} of {suit}')

print(f'There are {len(deck)} cards in the deck.')

hand = []

while len(hand) < 5:
    print('Dealing...')
    card = random.choice(deck)
    deck.remove(card)  #random.choice()에서 중복된 것이 있을 수 있으니 제거하고 다시 random.choice()를 한다.
    hand.append(card)  #플레이어가 가질 카드
    sleep(1) # sleep 1 second cf: mili second = 0.001
    print(card)

print(f'There are {len(deck)} cards in the deck.')
print('Player has the following cards in her/his hand:')
print(hand)
