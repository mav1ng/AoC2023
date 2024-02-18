

class Day:
    def __init__(self):
        pass

    def run(self):
        raise NotImplementedError


class Day19(Day):
    def __init__(self):
        super().__init__()
        with open("data/aoc/19.txt", 'r') as file:
            lines = file.read()

        self.input = []
        for line in lines.split(sep="\n\n"):
            self.input.append(line.split(sep="\n"))

    def run(self):
        pass

if __name__ == '__main__':
    day = Day19()
    day.run()
