import adventofcode as aoc


class Day5(aoc.Day):
    def __init__(self):
        super().__init__()

        with open("data/aoc/5.txt", 'r') as file:
            lines = file.readlines()
        self.winning = []
        self.yours = []
        self.cards = {}
        for i, line in enumerate(lines):
            le = line.split(":")[-1].strip().split(" | ")
            self.cards[i] = 1
            self.winning.append(list(map(int, filter(lambda x: x != "", le[0].strip().split(" ")))))
            self.yours.append(list(map(int, filter(lambda x: x != "", le[-1].strip().split(" ")))))

    def run(self):
        pass


if __name__ == '__main__':
    day = Day5()
    day.run()
