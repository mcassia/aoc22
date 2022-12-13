from utils import BaseSolver


class Solver(BaseSolver):

    def getPairsOfPackets(self, lines):
        pairs = []
        for i, line in enumerate(lines):
            if i % 3 == 0:
                pairs.append([eval(line)])
            elif (i-1)%3==0:
                pairs[-1].append(eval(line))
        return pairs

    def getPackets(self, lines):
        packets = []
        for line in lines:
            if line:
                packets.append(eval(line))
        return packets

    def compare(self, a, b):
        
        if isinstance(a, int) and isinstance(b, int):
            if a < b: return 1
            elif a > b: return -1
            elif a == b: return 0
        elif isinstance(a, list) and isinstance(b, int):
            return self.compare(a, [b])
        elif isinstance(a, int) and isinstance(b, list):
            return self.compare([a], b)
        elif isinstance(a, list) and isinstance(b, list):
            for x, y in zip(a, b):
                c = self.compare(x, y)
                if c == 0:
                    continue
                return c
            if len(a) < len(b):
                return 1
            elif len(a) > len(b):
                return -1
            else:
                return 0
        else:
            raise RuntimeError()

    def run1(self, text, lines):

        pairs = self.getPairsOfPackets(lines)

        total = 0
        for i, (a, b) in enumerate(pairs):
            c = self.compare(a, b)
            if c == 1:
                total += i+1

        return total

    def run2(self, text, lines):

        from functools import cmp_to_key

        extraPackets = [[[2]], [[6]]]

        packets = self.getPackets(lines) + extraPackets
        packets = list(reversed(sorted(packets, key=cmp_to_key(self.compare))))
        
        product = 1
        for i, a in enumerate(packets):
            for b in extraPackets:
                if a == b:
                    product *= (i + 1)
                    break

        return product
        

        
        



Solver().solve2(sample=False)