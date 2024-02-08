import adventofcode as aoc


class Day9(aoc.Day):
    def __init__(self):
        super().__init__()

        self.input = []
        with open("data/aoc/9.txt", 'r') as file:
            lines = file.readlines()
        for line in lines:
            self.input.append(list(map(int, line.strip().split())))

    def run(self):
        total = 0
        for line in self.input:
            total += self.extrapolate(line)
        print("Extrapolating forwards.", total)

        total = 0
        for line in self.input:
            total += self.extrapolate_backwards(line)
        print("Extrapolating backwards.", total)

    def extrapolate(self, sequence):
        if all(x == 0 for x in sequence):
            return 0
        ret = []
        for i in range(len(sequence) - 1):
            ret.append(sequence[i + 1] - sequence[i])
        return sequence[-1] + self.extrapolate(ret)

    def extrapolate_backwards(self, sequence):
        if all(x == 0 for x in sequence):
            return 0
        ret = []
        for i in range(len(sequence) - 1):
            ret.append(sequence[i + 1] - sequence[i])
        return sequence[0] - self.extrapolate_backwards(ret)



if __name__ == '__main__':
    day = Day9()
    day.run()
