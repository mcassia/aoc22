from utils import BaseSolver


class Solver(BaseSolver):

    # maps level to displacement in both directions
    DIRECTIONS = {
        'D': (0, 1),
        'U': (0, -1),
        'R': (1, 0),
        'L': (-1, 0),
    }

    def _run(self, lines, length):

        rope = [(0, 0) for _ in range(length)]
        visited = {(0, 0)}

        # for every instruction
        for line in lines:

            # parse the instruction and determine the head displacement in both directions
            direction, distance = line.split()
            distance = int(distance)
            dx, dy = self.DIRECTIONS[direction]

            # at each step, review the position of each knot
            for step in range(distance):
                for i, (kx, ky) in enumerate(rope):

                    # if it's the head of the rope, just mpve
                    if i == 0:
                        nkx, nky = kx + dx, ky + dy
                        rope[i] = (nkx, nky)

                    # otherwise, check if moving is necessary
                    else:

                        pkx, pky = rope[i-1]
                        if abs(pkx - kx) > 1 or abs(pky - ky) > 1:
                            kdx, kdy = pkx - kx, pky - ky
                            kdx = int(kdx / abs(kdx)) if kdx else kdx
                            kdy = int(kdy / abs(kdy)) if kdy else kdy
                            rope[i] = (kx + kdx, ky + kdy)
                visited.add(rope[-1])

        return len(visited)

    def run1(self, text, lines):
        return self._run(lines, 2)

    def run2(self, text, lines):
        return self._run(lines, 10)



Solver().solve1(sample=False)
