from utils import BaseSolver


class Solver(BaseSolver):

    def apply(self, lines, multiple):

        f = lambda lst: list(lst) if multiple else list(reversed(lst))

        stacks, ops = [], []

        inOps = False
        for line in lines:
            if not line.strip():
                inOps = True
            elif inOps:
                vs = [int(v) for v in line.split() if v.isdigit()]
                assert len(vs) == 3
                ops.append(vs)
            else:
                i, j = 1, 0
                while i < len(line):
                    v = line[i]
                    if len(stacks) <= j:
                        stacks.append([])
                    stacks[j].append(v)
                    i = i + 4
                    j = j + 1

        stacks = [[x for x in stack if x.strip() and x.isalpha()] for stack in stacks]
        
        for op in ops:
            q, a, b = op
            a, b = a - 1, b - 1
            stacks[b] = f(stacks[a][:q]) + stacks[b]
            stacks[a] = stacks[a][q:]
            
        return ''.join([stack[0] for stack in stacks if stack])

    def run1(self, text, lines):
        return self.apply(lines=lines, multiple=False)

    def run2(self, text, lines):
        return self.apply(lines=lines, multiple=True)
            
        
Solver().solve2(sample=False)

