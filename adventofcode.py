import numpy as np
import pandas as pd
from collections import deque
import re


class Day:
    def __init__(self):
        pass

    def run(self):
        raise NotImplementedError


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
