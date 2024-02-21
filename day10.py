import adventofcode as aoc


class Day10(aoc.Day):
    def __init__(self):
        super().__init__()

        with open("data/aoc/10.txt", 'r') as file:
            self.lines = file.read().split("\n")
        print(self.lines)
        for i, line in enumerate(self.lines):
            print(line)
            for j, letter in enumerate(line):
                if "S" == letter:
                    self.xstart = i
                    self.ystart = j

        self.visited = [(self.xstart, self.ystart)]
        self.n = len(self.lines) - 1
        self.m = len(self.lines[0]) - 1
        cur, i, j = self.find_next_pipe(val="S", i=self.xstart, j=self.ystart)
        self.node = Node(i=self.xstart, j=self.ystart, val=self.lines[self.xstart][self.ystart],
                         next=Node(val=cur, i=i, j=j))
        self.build_loop(root_node=self.node)

    def run(self):
        print(f"The most distant pipe is {self.count_steps() / 2} steps away!")

    def find_next_pipe(self, val, i, j):
        if i > 0 and val in ["S", "|", "L", "J"] and (i - 1, j) not in self.visited:
            cur = self.lines[i - 1][j]
            if cur != '.':
                if cur in ["|", "7", "F"]:
                    return cur, i - 1, j
        if i < self.n and val in ["S", "|", "7", "F"] and (i + 1, j) not in self.visited:
            cur = self.lines[i + 1][j]
            if cur != '.':
                if cur in ["|", "L", "J"]:
                    return cur, i + 1, j
        if j > 0 and val in ["S", "-", "J", "7"] and (i, j - 1) not in self.visited:
            cur = self.lines[i][j - 1]
            if cur != '.':
                if cur in ["-", "L", "F"]:
                    return cur, i, j - 1
        if j < self.m and val in ["S", "-", "L", "F"] and (i, j + 1) not in self.visited:
            cur = self.lines[i][j + 1]
            if cur != '.':
                if cur in ["-", "J", "7"]:
                    return cur, i, j + 1
        return "S", self.xstart, self.ystart

    def build_loop(self, root_node):
        self.visited.append((root_node.i, root_node.j))
        node = root_node
        while True:
            cur, i, j = self.find_next_pipe(val=node.val, i=node.i, j=node.j)
            if cur == "S":
                break
            new_node = Node(val=cur, i=i, j=j, next=None)
            node.next = new_node
            self.visited.append((node.i, node.j))
            node = new_node

    def count_steps(self):
        node = self.node.next
        steps = 1
        while node.next:
            steps += 1
            node = node.next
        return steps + 1

class Node:
    def __init__(self, i=None, j=None, val=None, next=None):
        self.i = i
        self.j = j
        self.val = val
        self.next = next


if __name__ == '__main__':
    day10 = Day10()
    day10.run()