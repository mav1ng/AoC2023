from collections import deque

import pandas as pd

from adventofcode import Day


class Day7(Day):
    def __init__(self, level):
        super().__init__()
        self.input = pd.read_csv('data/aoc/7.csv', header=None)
        self.labels = {'A': 13., 'K':12., 'Q': 11., 'J': 10., 'T': 9., '9': 8., '8': 7., '7': 6., '6': 5., '5': 4., '4': 3., '3': 2., '2': 1.}
        self.level = level
        if self.level == 2:
            # set joker weakest
            self.labels['J'] = 0.
        self.type = {'five': 70000000000., 'four': 60000000000., 'fullhouse': 50000000000., 'three': 40000000000., 'twopairs': 30000000000., 'onepair': 20000000000., 'highcard': 10000000000.}
        self.bids = {}
        self.scores = [] # list of all scores
        self.ranks = {} # hands auf rank
        self.scorehand = {} # score auf hand
        self.hands = []
        self.winnings = {}
        for line in self.input[0]:
            hand, bid = line.split(" ")
            self.hands.append(hand)
            self.bids[hand] = float(bid)

    @staticmethod
    def optimal_count(cards_present, counts, current_hand):
        if 'J' in cards_present:
            cards_present.remove('J')
            targets = cards_present

            optimal_target = None
            optimal_count = counts
            max_count = 0
            first_occurence = -1

            for target in targets:
                # using jokers
                nb_J = current_hand.count('J')
                joker_hand = deque()
                for i in range(-1, -len(current_hand) - 1, -1):
                    if current_hand[i] == 'J' and nb_J > 0:
                        joker_hand.appendleft(target)
                        nb_J -= 1
                    else:
                        joker_hand.appendleft(current_hand[i])
                counts = []
                for card in list(set(joker_hand)):
                    counts.append(joker_hand.count(card))
                if max(counts) > max_count:
                    optimal_target = target
                    optimal_count = counts
                    max_count = max(counts)
                elif max(counts) == max_count and nb_J > 0:
                    if joker_hand.index('J') > first_occurence:
                        optimal_target = target
                        optimal_count = counts
            counts = optimal_count
        return counts

    def det_type(self, hand):
        current_hand = list(hand)
        cards_present = list(set(current_hand))
        counts = []
        for card in cards_present:
            counts.append(current_hand.count(card))
        counts.sort(reverse=True)
        if self.level == 2:
            counts = self.optimal_count(cards_present=cards_present, counts=counts, current_hand=current_hand)
        counts.sort(reverse=True)

        if counts == [5]:
            return 'five'
        elif counts == [4, 1]:
            return 'four'
        elif counts == [3, 2]:
            return 'fullhouse'
        elif counts == [3, 1, 1]:
            return 'three'
        elif counts == [2, 2, 1]:
            return 'twopairs'
        elif counts == [2, 1, 1, 1]:
            return 'onepair'
        elif counts == [1, 1, 1, 1, 1]:
            return 'highcard'
        else:
            print(f'The current hand is {hand}.')
            raise TypeError

    def run(self):
        for hand in self.hands:
            score = self.type[self.det_type(hand)] + self.labels[hand[0]] * 10 ** 8 + self.labels[hand[1]] * 10 ** 6 + \
                    self.labels[hand[2]] * 10 ** 4 + self.labels[hand[3]] * 10 ** 2 + self.labels[hand[4]]
            self.scores.append(score)
            self.scorehand[score] = hand
        self.scores.sort()
        for i, score in enumerate(self.scores):
            self.ranks[self.scorehand[score]] = i + 1

        summe = 0.
        for hand in self.hands:
            self.winnings[hand] = self.bids[hand] * self.ranks[hand]
            summe = summe + self.bids[hand] * self.ranks[hand]

        print(f'the toal winnings of the cards are {int(sum(self.winnings.values()))}')