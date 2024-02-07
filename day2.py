import adventofcode as aoc
import re


class Day2(aoc.Day):
    def __init__(self):
        super().__init__()
        with open("data/aoc/2.txt", 'r') as file:
            lines = file.readlines()
        id_pat = re.compile(r'(?<=Game )[\d]+(?=:)')
        num_pat = re.compile(r'[0-9]+')
        color_pat = re.compile(r'[a-z]+')

        self.input = []
        self.dic = {}
        for game, line in enumerate(lines, 1):
            self.dic[game] = {'red': 0, 'blue': 0, 'green': 0}
            for entry in line.split(":")[1].split(";"):
                numbers = num_pat.findall(entry)
                colors = color_pat.findall(entry)
                for color, number in zip(colors, numbers):
                    self.dic[game][color] = max(int(number), self.dic[game][color])

    def run(self):
        total = 0
        for game in self.dic:
            if self.check_game(game_id=game):
                total += game
        return total

    def check_game(self, game_id):
        max_numbers = [12, 13, 14]
        for color, max_number in zip(['red', 'green', 'blue'], max_numbers):
            if self.dic[game_id][color] > max_number:
                return False
        return True

if __name__ == '__main__':
    day = Day2()
    print(day.run())
