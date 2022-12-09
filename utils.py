def _readInput(path):
    return open(path, 'rb').read().decode('utf8')


def readSampleInput():
    return _readInput('sample_input.txt')


def readInput():
    return _readInput('real_input.txt')


class BaseSolver:

    def solve1(self, sample=True):
        return self._solve(self.run1, sample=sample)

    def solve2(self, sample=True):
        return self._solve(self.run2, sample=sample)

    def _solve(self, f, sample=True):
        i = readSampleInput() if sample else readInput()
        solution = f(i, list(i.splitlines()))
        print(solution)
        return solution

    def run1(self, text, lines):
        raise NotImplementedError()

    def run2(self, text, lines):
        raise NotImplementedError()