import numpy as np
import pandas as pd
from collections import deque
import re


class Day:
    def __init__(self):
        pass

    def run(self):
        raise NotImplementedError


class Day1(Day):
    def __init__(self):
        super().__init__()
        self.input = pd.read_csv('data/aoc/1.csv', header=None)
        self.li = self.input[0].tolist()
        self.num_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    def findcal(self, line):
        # Use regular expression to find all digits in the line
        digits = re.findall(r'\d', line)

        # Combine the first and last digit to form a two-digit number
        if digits:
            cal_value = int(digits[0] + digits[-1])
            return cal_value
        else:
            return 0  # Return 0 if no digits are found in the line

    def findcal_2(self, line):
        pat = r'\d|one|two|three|four|five|six|seven|eight|nine'
        pattern = re.compile(pat)
        first = pattern.findall(line)[0]

        pat = r'\d|one|two|three|four|five|six|seven|eight|nine'
        pattern = re.compile(pat)
        last = pattern.findall(line)[-1]

    def run(self):

        total = 0
        for cal in self.li:
            total += self.findcal(cal)
        print(f'Total without replacement: {total}')

        total = 0
        for cal in self.li:
            total += self.findcal_2(cal)
        print(f'Total with replacement: {total}')

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

class Day8(Day):
    def __init__(self):
        super().__init__()
        self.input = pd.read_csv('data/aoc/8.csv', delimiter="=")
        self.directions = self.input.columns.astype(str)[0]
        pattern = re.compile(pattern=r"\w{3}")
        self.graph = {}

        for index, row in self.input.iterrows():
            self.graph[index.strip()] = pattern.findall(row[0])

    def follow_directions(self):
        current_node = "AAA"
        steps = 0
        while current_node != "ZZZ":
            for step in list(self.directions):
                if step == "L":
                    current_node = self.graph[current_node][0]
                elif step == "R":
                    current_node = self.graph[current_node][1]
                else:
                    raise NotImplementedError
                steps += 1
        return steps

    def follow_multiple(self):
        current_nodes = list(filter(lambda x: x[-1] == "A", self.graph.keys()))
        stepslist = []

        for i in range(len(current_nodes)):
            current_node = current_nodes[i]
            steps = 0
            while current_node[-1] != "Z":
                for step in list(self.directions):
                    if step == "L":
                        current_node = self.graph[current_node][0]
                    elif step == "R":
                        current_node = self.graph[current_node][1]
                    else:
                        raise NotImplementedError
                    steps += 1
            print(steps)
            stepslist.append(steps)

        return np.lcm.reduce(stepslist)

    def run(self):
        # print(self.follow_directions())
        print(self.follow_multiple())

class Day13(Day):
    def __init__(self):
        super().__init__()
        with open("data/aoc/13.txt", 'r') as file:
            lines = file.read()

        self.input = []
        for line in lines.split(sep="\n\n"):
            self.input.append(line.split(sep="\n"))

    def check_vertical(self):
        ret = []
        for patch in self.input:
            patch = np.array(patch)
            print(patch[:, 0:3])
            breakpoint()
            ismirror = None
            patchlen = len(patch[0])
            for vmirror in range(1, patchlen - 1):
                width = min(len(patch[0][:vmirror]), len(patch[0][vmirror:]))
                print(patch[:][max(0, vmirror - width):vmirror], patch[:][vmirror:min(patchlen, vmirror + width)])
                if (patch[:][max(0, vmirror - width):vmirror] == patch[:][vmirror:min(patchlen, vmirror + width)]).all():
                    ismirror = vmirror
            ret.append(ismirror)

    def run(self):
        self.check_vertical()
        pass

if __name__ == '__main__':
    day = Day13()
    day.run()
