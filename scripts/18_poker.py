#! -*- coding:utf-8 -*-

from enum import Enum,unique
import random

@unique
class Suite(Enum):
    #枚举值
    SPADE, HEART, CLUB, DIAMOND = range(4)
    #实现比较函数
    def __lt__(self, other):
        return self.value < other.value

class Card(object):
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def show(self):
        suites = ['♠️', '♥️', '♣️', '♦️']
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]} {faces[self.face]}'

    def __str__(self):
        return self.show()

    def __repr__(self):
        return self.show()

class Poker():
    def __init__(self):
        self.index = 0
        #卡片初始化
        self.cards = [Card(suite, face) for suite in Suite for face in range(1, 14)]

    def shuffle(self):
        random.shuffle(self.cards)
        self.index = 0

    def deal(self):
        #从牌组中取出一张牌，并发牌
        card = self.cards[self.index]
        self.index += 1
        return card

    @property
    def has_more(self):
        return self.index < len(self.cards)


class Player():
    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        self.cards.append(card)

    def sort(self, comp=lambda card:(card.suite, card.face)):
        self.cards.sort(key=comp)


def poker_play():
    poker = Poker()
    poker.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    while poker.has_more:
        for player in players:
                player.get_one(poker.deal())
    for player in players:
        player.sort()
        print(player.name, end=': ')
        print(player.cards)


if __name__ == "__main__":
    poker_play()
