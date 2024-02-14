import copy

import adventofcode as aoc


class Day5(aoc.Day):
    def __init__(self):
        super().__init__()

        with open("data/aoc/5.txt", 'r') as file:
            lines = file.read()
        blocks = lines.split('\n\n')
        self.seeds = list(map(int, blocks[0].split(" ")[1:]))
        self.starting_seeds = copy.copy(self.seeds)
        self.category = "seed"
        self.maps = {}
        for block in blocks[1:]:
            block_ = block.split("\n")
            line_ = block_[0].split(" ")[0].split("-")
            self.maps[line_[0]] = [line_[-1]]

            for i in range(1, len(block_)):
                self.maps[line_[0]].append(list(map(int, block_[i].split(" "))))

    def run(self):
        self.almanac()
        self.consider_ranges()
        self.category = "seed"
        self.almanac()
        self.lowest()
        print(self.seeds)

    def almanac(self):
        while self.category != 'location':
            self.map()
        print(f"Lowest location number is {min(self.seeds)}!")

    def map(self):
        instructions = self.maps[self.category]
        self.category = instructions[0]
        for nb, seed in enumerate(self.seeds):
            for i in range(1, len(instructions)):
                if 0 <= seed - instructions[i][1] < instructions[i][-1]:
                    self.seeds[nb] = instructions[i][0] + (seed - instructions[i][1])
                    break

    #def consider_ranges(self):
    #    n = len(self.seeds)
    #    self.seeds = []
    #    for i in range(0, n, 2):
    #        self.seeds.extend([self.starting_seeds[i]]) #, self.starting_seeds[i] + self.starting_seeds[i+1]])

    def consider_ranges(self):
        min_start = float('inf')
        for i in range(0, len(self.starting_seeds), 2):
            start = self.starting_seeds[i]
            if start < min_start:
                min_start = start
        self.seeds = [min_start]

    def lowest(self):
        print(min(self.seeds))

if __name__ == '__main__':
    day = Day5()
    day.run()
