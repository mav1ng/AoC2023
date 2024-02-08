import numpy as np
import pandas as pd
from collections import deque
import re


class Day:
    def __init__(self):
        pass

    def run(self):
        raise NotImplementedError

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
