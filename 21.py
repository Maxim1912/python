from pprint import pprint
from random import shuffle


# функция возвращает колоду карт
def get_deck():
    deck = []
    for suit in ('черви', 'буби', 'крести', 'трефы'):
        for card in range(2, 11):
            deck.append(f'{card} {suit}')
        for card_name in ('валет', 'дама', 'король', 'туз'):
            deck.append(f'{card_name} {suit}')
    shuffle(deck)
    return deck


# функция возврашает очки определённой карты
def get_card_points(card):
    card_points = {}
    for card in range(2, 11):
        card_points[]