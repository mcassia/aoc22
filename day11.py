from utils import BaseSolver
from pprint import pprint as pp



class Solver(BaseSolver):

    def getMonkeys(self, lines):
        monkeys = []
        i = 0
        while i < len(lines):
            monkeys.append(Monkey.fromLines(lines[i:i+7]))
            i += 7
        return monkeys


    def run2(self, text, lines):

        monkeys = self.getMonkeys(lines)     

        for m in monkeys:
            for l, h in m.levels:
                for m2 in monkeys:
                    h[m2.divisor] = l % m2.divisor

        for round in range(10000):
            print(round)
            for monkey in monkeys:
                
                for level, history in monkey.levels:
                    
                    if monkey.operation == '+':
                        x = monkey.term()
                        for divisor, r in history.items():
                            history[divisor] = (r + x) % divisor
                    elif monkey.operation == '*':
                        x = monkey.term()
                        for divisor, r in history.items():
                            history[divisor] = (r * x) % divisor
                    elif monkey.operation == '**':
                        for divisor, r in history.items():
                            history[divisor] = (r ** 2) % divisor
                    else:
                        raise RuntimeError()
                    
                    remainder = history[monkey.divisor]

                    monkeys[
                        monkey.left if (remainder == 0) else monkey.right
                    ].levels.append((level, history))
                    monkey.inspected += 1
                    

                monkey.levels = []    

            
        inspected = [monkey.inspected for monkey in monkeys]
        inspecteds = sorted(inspected)[-2:]
        business = inspecteds[0] * inspecteds[1]
        print(round, business, inspected, sum(inspected))

        return business



class Monkey(object):

    def __init__(self, name, levels, operation, term, divisor, left, right):
        self.name = name # int, unique id of monkey
        self.levels = [(level, {}) for level in levels] # list[int]
        self.operation = operation
        self.term = term
        self.divisor = divisor
        self.left = left
        self.right = right
        self.inspected = 0

    @staticmethod
    def fromLines(lines):
        name = int(lines[0].split()[-1][:-1])
        levels = list(map(int, lines[1].split(':')[-1].replace(' ', '').split(',')))

        # update = lambda old: eval(str(lines[2].split('=')[-1].replace(' ', '')))
        update = str(lines[2].split('=')[-1].replace(' ', ''))
        operation = '+' if '+' in update else ('**' if '*old' in update else '*')
        term = lambda: eval(update.split(operation)[-1])

        divisor = int(lines[3].split('divisible by ')[-1])
        left = int(lines[4].split('throw to monkey ')[-1])
        right = int(lines[5].split('throw to monkey ')[-1])

        return Monkey(
            name=name,
            levels=levels,
            operation=operation,
            term=term,
            divisor=divisor,
            left=left,
            right=right
        )


Solver().solve2(sample=False)
