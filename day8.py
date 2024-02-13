import adventofcode as aoc
import numpy as np
import pandas as pd
import re

class Day8(aoc.Day):
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


if __name__ == '__main__':
    day = Day8()
    day.run()