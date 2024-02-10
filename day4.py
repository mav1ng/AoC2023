import adventofcode as aoc


class Day4(aoc.Day):
    def __init__(self):
        super().__init__()

        with open("data/aoc/4.txt", 'r') as file:
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
        print(self.calcWinning())
        print(self.collectCards())

    def calcWinning(self):
        total = 0
        for i, line in enumerate(self.winning):
            check = set()
            counter = 0
            for num in line:
                check.add(num)
            for k in self.yours[i]:
                if k in check:
                    counter += 1

            if counter >= 1:
                total += 2 ** (counter - 1)
        return total

    def matchingNumbers(self, line_i):
        check = set()
        counter = 0
        for num in self.winning[line_i]:
            check.add(num)
        for k in self.yours[line_i]:
            if k in check:
                counter += 1
        return counter

    def collectCards(self):
        total = 0
        for i in range(len(self.cards)):
            matching_number = self.matchingNumbers(i)
            if matching_number > 0:
                for k in range(1, matching_number + 1):
                    self.cards[i + k] += self.cards[i]
            total += self.cards[i]
        return total



if __name__ == '__main__':
    day = Day4()
    day.run()
