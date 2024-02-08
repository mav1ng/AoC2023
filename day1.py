import adventofcode as aoc
import pandas as pd
import re


class Day1(aoc.Day):
    def __init__(self):
        super().__init__()
        self.input = pd.read_csv('data/aoc/1.csv', header=None)
        self.li = self.input[0].tolist()
        self.num_dict = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}

    def findcal(self, line):
        # Use regular expression to find all digits in the line
        digits = re.findall(r'\d', line)

        # Combine the first and last digit to form a two-digit number
        if digits:
            cal_value = int(digits[0] + digits[-1])
            return cal_value
        else:
            return 0  # Return 0 if no digits are found in the line

    def findcal_2(self, line):
        first = re.findall(r'([0-9]|one|two|three|four|five|six|seven|eight|nine)', line)[0]
        last = re.findall(r'([0-9]|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)', line[::-1])[0][::-1]
        if first in self.num_dict:
            first = self.num_dict[first]
        if last in self.num_dict:
            last = self.num_dict[last]
        return int(str(first) + str(last))

    def run(self):

        total = 0
        for cal in self.li:
            total += self.findcal(cal)
        print(f'Total without replacement: {total}')


        total = 0
        for cal in self.li:
            total += int(self.findcal_2(cal))
        print(f'Total with replacement: {total}')


if __name__ == "__main__":
    day1 = Day1()
    day1.run()