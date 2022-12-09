from utils import BaseSolver


class Solver(BaseSolver):

    def run1(self, text, lines):

        alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

        total = 0

        for line in lines:
            n = len(line)
            left, right = set(line[:n//2]), set(line[n//2:])
            common = left & right
            assert len(common) == 1
            item = list(common)[0]
            priority = alphabet.index(item) + 1
            total += priority

        return total

    def run2(self, text, lines):

        alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

        assert len(lines) % 3 == 0

        total = 0

        for i in range(len(lines) // 3):
            common = set(lines[i*3]) & set(lines[i*3+1]) & set(lines[i*3+2])
            assert len(common) == 1
            item = list(common)[0]
            priority = alphabet.index(item) + 1
            total += priority

        return total






Solver().solve2(sample=False)