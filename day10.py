from utils import BaseSolver


class Solver(BaseSolver):

    def getInstructions(self, lines):
        for line in lines:
            if 'noop' in line:
                yield line
            elif 'addx' in line:
                yield '_' + line
                yield line
            else:
                raise RuntimeError()

    def run1(self, text, lines):
        x = 1
        strenghts = []
        for i, instruction in enumerate(self.getInstructions(lines)):

            clock = i + 1
            if clock in (20, 60, 100, 140, 180, 220):
                strength = clock * x
                strenghts.append(strength)

            if instruction == 'noop':
                pass
            elif instruction.startswith('_addx'):
                pass
            elif instruction.startswith('addx'):
                x += int(instruction.split()[-1])
            
        return sum(strenghts)

    def run2(self, text, lines):
        x = 1
        CRT = list(' ' * 40)
        for i, instruction in enumerate(self.getInstructions(lines)):

            j = i % 40
            CRT[j] = '#' if j in (x-1,x,x+1) else ' '
            if i and (i % 40 == 0):
                print(''.join(CRT))

            clock = i + 1

            if instruction == 'noop':
                pass
            elif instruction.startswith('_addx'):
                pass
            elif instruction.startswith('addx'):
                x += int(instruction.split()[-1])
        print(''.join(CRT))

Solver().solve2(sample=False)