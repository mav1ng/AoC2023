import adventofcode as aoc


class Day3(aoc.Day):
    def __init__(self):
        super().__init__()

        self.input = []
        with open("data/aoc/3.txt", 'r') as file:
            lines = file.read()
        self.input = lines.split("\n")

    def run(self):
        print(self.find_numbers())


    def find_numbers(self):
        rows = len(self.input)
        columns = len(self.input[0])
        symbols = []
        total = 0
        print("\n".join(self.input))
        for i in range(0, len(self.input) - 1):
            for k in range(len(self.input[0])):
                if not self.input[i][k].isalnum() and not self.input[i][k] == ".":
                    symbols.append(k)
            for s in symbols:
                for m in range(-1, 2, 1):
                    for n in range(-1, 2, 1):
                        if 0 <= i + n < rows and 0 <= s + m < columns:
                            total += self.matchNumber(row=i + n, index=s + m)
            symbols = []
        print("\n", "\n".join(self.input))
        return total


    def matchNumber(self, row, index):
        if not self.input[row][index].isdigit():
            return 0
        line = self.input[row]
        left = index
        right = index
        while left > 0:
            if line[left - 1].isdigit():
                left -= 1
            else:
                break
        while right < len(line) - 1:
            if line[right + 1].isdigit():
                right += 1
            else:
                break
        ret = line[left:right + 1]
        change = list(self.input[row])
        change[left:right + 1] = len(ret) * ["."]
        self.input[row] = "".join(change)
        return int("".join(ret))


if __name__ == '__main__':
    day = Day3()
    day.run()
