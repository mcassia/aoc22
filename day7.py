from utils import BaseSolver
from pprint import pprint


class Solver(BaseSolver):

    def run1(self, text, lines):

        assert lines[0] == '$ cd /'

        current = []
        files = []

        i = 0

        while i < len(lines):
            line = lines[i]
            if line.startswith('$ cd '):
                directory = line[5:]
                if directory == '/':
                    current = []
                elif directory == '..':
                    current = current[:-1]
                else:
                    current = current + [directory]
                i += 1
            elif line == '$ ls':
                j = i + 1
                while j < len(lines) and not lines[j].startswith('$'):
                    a, b = lines[j].split()
                    if a == 'dir':
                        pass
                    else:
                        files.append((tuple(current), int(a), b))
                    j += 1
                i = j
            else:
                raise RuntimeError()


        grandTotal = 0
        directories = sorted(
            {
                directory[:i]
                for directory, _, _ in files
                for i in range(len(directory)+1)
            }
        )
        for directory in directories:
            total = 0
            for d, size, _ in files:
                if '/'.join(d).startswith('/'.join(directory)):
                    total += size
            if total <= 100000:
                grandTotal += total

        return grandTotal


    def run1(self, text, lines):

        assert lines[0] == '$ cd /'

        current = []
        files = []

        i = 0

        while i < len(lines):
            line = lines[i]
            if line.startswith('$ cd '):
                directory = line[5:]
                if directory == '/':
                    current = []
                elif directory == '..':
                    current = current[:-1]
                else:
                    current = current + [directory]
                i += 1
            elif line == '$ ls':
                j = i + 1
                while j < len(lines) and not lines[j].startswith('$'):
                    a, b = lines[j].split()
                    if a == 'dir':
                        pass
                    else:
                        files.append((tuple(current), int(a), b))
                    j += 1
                i = j
            else:
                raise RuntimeError()


        directories = sorted(
            {
                directory[:i]
                for directory, _, _ in files
                for i in range(len(directory)+1)
            }
        )
        directoryToSize = {}
        for directory in directories:
            total = 0
            for d, size, _ in files:
                if '/'.join(d).startswith('/'.join(directory)):
                    total += size
            directoryToSize[tuple(directory)] = total

        available = 70000000 - directoryToSize[()]
        needed = 30000000 - available

        smallest = None

        for d, s in directoryToSize.items():
            if s >= needed:
                if smallest is None:
                    smallest = s
                smallest = min(smallest, s)

        return smallest



                    

        

Solver().solve1(sample=True)
