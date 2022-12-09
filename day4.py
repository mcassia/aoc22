from utils import BaseSolver


class Solver(BaseSolver):

    def run1(self, text, lines):

        total = 0

        for line in lines:
            left, right = line.split(',')
            left = set(range(int(left.split('-')[0]), int(left.split('-')[1])+1))
            right = set(range(int(right.split('-')[0]), int(right.split('-')[1])+1))
            if left & right:
                total += 1

        return total


Solver().solve1(sample=False)