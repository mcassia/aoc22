from utils import BaseSolver


class Solver(BaseSolver):

    def run1(self, text, lines):
        
        chars = []

        for i, c in enumerate(text):
            if len(chars) < 4:
                chars.append(c)
            else:
                chars = chars[1:] + [c]

            if len(set(chars)) == 4:
                return i + 1

        raise RuntimeError()

    def run2(self, text, lines):
        
        chars = []

        for i, c in enumerate(text):
            if len(chars) < 14:
                chars.append(c)
            else:
                chars = chars[1:] + [c]

            if len(set(chars)) == 14:
                return i + 1

        raise RuntimeError()


Solver().solve2(sample=True)