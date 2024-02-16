import copy

import adventofcode as aoc
from collections import deque


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
        print(f'Lowest location number is {self.lowest(ranges=self.map_ranges())}!')

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

    def map_ranges(self):
        to_convert = self.seeds
        seeds = []

        while self.category != 'location':

            instructions = self.maps[self.category]
            self.category = instructions[0]
            while to_convert:
                (start, end) = to_convert.pop()

                for i in range(1, len(instructions)):
                    i_start = int(instructions[i][1])
                    i_range = int(instructions[i][-1])
                    i_end = i_start + i_range
                    i_dest = int(instructions[i][0])

                    # if out of conversion range
                    if start >= i_end or end <= i_start:
                        continue
                    # if perfectly in conversion range
                    elif start >= i_start and end <= i_end:
                        seeds.append((i_dest + (start - i_start), i_dest + (end - i_start)))
                        break
                    # if partly in conversion range, end is outside
                    elif start >= i_start and end > i_end:
                        to_convert.append((i_end, end))
                        seeds.append((i_dest + (start - i_start), i_dest + (i_end - i_start)))
                        break
                    # if partly in conversion range, start is outside
                    elif start < i_start and end <= i_end:
                        to_convert.append((start, i_start))
                        seeds.append((i_dest + (i_start - i_start), i_dest + (end - i_start)))
                        break
                    # if start end past conversion range
                    elif start < i_start and end > i_end:
                        to_convert.append((start, i_start))
                        to_convert.append((i_end, end))
                        seeds.append((i_dest, i_dest + i_range))
                        break
                    else:
                        raise NotImplementedError

                else:
                    seeds.append((start, end))

            to_convert = seeds
            seeds = []
        return to_convert




    def consider_ranges(self):
        n = len(self.seeds)
        self.seeds = []
        for i in range(0, n, 2):
            self.seeds.extend([(self.starting_seeds[i], self.starting_seeds[i] + self.starting_seeds[i+1])])


    def lowest(self, ranges):
        return(min(list(map(lambda x: x[0], ranges))))

if __name__ == '__main__':
    day = Day5()
    day.run()
