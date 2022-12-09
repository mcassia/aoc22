from utils import BaseSolver


class Solver(BaseSolver):

    def run(self, text):

        current = 0
        stocks = []

        for line in text.splitlines():
            line = line.strip()
            if line:
                current += int(line)
            else:
                stocks.append(current)
                current = 0
        if current:
            stocks.append(current)

        print(stocks)

        stocks = sorted(stocks)

        return sum(stocks[-3:])


Solver().solve(sample=False)