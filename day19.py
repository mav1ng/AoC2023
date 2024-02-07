import adventofcode
from collections import namedtuple
import numpy as np
import pandas as pd
import re

cond = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}

class Day19(adventofcode.Day):
    def __init__(self):
        super().__init__()
        with open("data/aoc/19.txt", 'r') as file:
            lines = file.read()

        self.input = []
        for line in lines.split(sep="\n\n"):
            self.input.append(line.split(sep="\n"))

        self.ratings = self.parse_ratings()
        self.workflows = self.parse_workflows()
        self.visited = []
        self.to_visit = self.workflows.keys()

    def run_workflow(self, scrap, starting_wf):
        cond_res = re.compile(r'(?<=:)[a-zA-Z]+$')
        for current_step in self.workflows[starting_wf]:
            if current_step == 'A':
                return scrap
            elif current_step == 'R':
                return None
            elif current_step in self.workflows.keys():
                return self.run_workflow(scrap, current_step)
            elif self.check_cond(scrap, current_step):
                res = re.findall(cond_res, current_step)[0]
                if res == 'A':
                    return scrap
                elif res == 'R':
                    return None
                elif res in self.workflows.keys():
                    return self.run_workflow(scrap, res)
                else:
                    raise NotImplementedError
        raise NotImplementedError

    def calc_workflow(self, cond, step):

        if step == 'A':
            return cond

        if len(self.to_visit) == 0:
            return cond


        while len(to_visit) > 0:


    def check_cond(self, scrap, current_step):
        cond_key = re.compile(r'^[a-z](?=[<>])')
        cond_value = re.compile(r'(?<=[<>])\d+(?=:)')
        cond_op = re.compile(r'[<>]')
        key = re.findall(cond_key, current_step)[0]
        value = re.findall(cond_value, current_step)[0]
        if re.findall(cond_op, current_step)[0] == '<':
            return int(getattr(scrap, key)) < int(value)
        elif re.findall(cond_op, current_step)[0] == '>':
            return int(getattr(scrap, key)) > int(value)
        else:
            raise NotImplementedError
    def parse_workflows(self):
        self.workflows = {}

        key_pattern = re.compile(r'^[a-z]+(?={)')
        value_pattern = re.compile(r'(?<={).+(?=})')

        for r in self.input[0]:
            key = re.findall(key_pattern, r)[0]
            values = re.findall(value_pattern, r)[0]
            values.split(",")
            self.workflows[key] = values.split(",")
        return self.workflows

    def parse_ratings(self):
        self.ratings = []
        key_pattern = re.compile(r'[a-x](?==)')
        value_pattern = re.compile(r'(?<=[a-x]=)\d+(?=[,}])')

        for r in self.input[-1]:
            keys = re.findall(key_pattern, r)
            values = re.findall(value_pattern, r)
            Scrap = namedtuple("Scrap", keys)
            self.ratings.append(Scrap(*values))
        return self.ratings

    def run(self):
        sum = 0
        for scrap in self.ratings:
            res = self.run_workflow(scrap=scrap, starting_wf='in')
            if res:
                for field in scrap._fields:
                    sum += int(getattr(scrap, field))
        print(sum)



    # self.rating = namedtuple("Scrap")

if __name__ == "__main__":
    day = Day19()
    day.run()
