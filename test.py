import numpy as np

def simulateAnts(n=100):
    steps = []
    a = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for i in range(n):
        step = 0
        (x, y) = (0, 0)
        while abs(x) < 2 and abs(y) < 2:
            tup = np.random.randint(0, 3)
            x += a[tup][0]
            y += a[tup][1]
            step += 1
        steps.append(step)
    return sum(steps) / len(steps)

if __name__ == "__main__":
    measn = []
    print(simulateAnts(1000000))
