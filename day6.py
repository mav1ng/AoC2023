import copy

import adventofcode as aoc
from collections import deque


class Day6(aoc.Day):
    def __init__(self):
        super().__init__()

        with open("data/aoc/6.txt", 'r') as file:
            lines = file.read()
        self.time = list(map(int, filter(lambda x: x != '', lines.split('\n')[0].strip().split(":")[-1].split(" "))))
        self.distance = list(map(int, filter(lambda x: x != '', lines.split('\n')[1].strip().split(":")[-1].split(" "))))

    def run(self):
        print(self.calculate_possibilites())
        self.load_part2()
        print(self.calculate_possibilites())

    def calculate_possibilites(self):
        n = len(self.time)
        total = 1
        for race in range(n):
            comb = sum(map(lambda x: self.distance[race] < x, [x * (self.time[race] - x) for x in range(1, self.time[race] + 1)]))
            total *= comb
        return total

    def load_part2(self):
        with open("data/aoc/6.txt", 'r') as file:
            lines = file.read()
        self.time = [
            int("".join(list(filter(lambda x: x != '', lines.split('\n')[0].strip().split(":")[-1].split(" ")))))]
        self.distance = [
            int("".join(list(filter(lambda x: x != '', lines.split('\n')[1].strip().split(":")[-1].split(" ")))))]


if __name__ == '__main__':
    day = Day6()
    day.run()
