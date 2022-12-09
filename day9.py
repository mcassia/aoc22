from utils import BaseSolver


class Solver(BaseSolver):

    # maps level to displacement in both directions
    DIRECTIONS = {
        'D': (0, 1),
        'U': (0, -1),
        'R': (1, 0),
        'L': (-1, 0),
    }

    def run2(self, text, lines):

        rope = [(0, 0) for _ in range(10)]
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

        head = (0, 0)
        tail = (0, 0)

        tailHistory = {(0, 0)}

        for line in lines:
            direction, distance = line.split()
            distance = int(distance)
            dx, dy = self.DIRECTIONS[direction]

            # move head one step at a time
            for i in range(distance):

                # move the head
                hx, hy = head
                nhx, nhy = hx + dx, hy + dy
                head = (nhx, nhy)
                hx, hy = head
                print('HEAD', head)

                # move the tail if needed
                tx, ty = tail
                if abs(nhx - tx) > 1 or abs(nhy - ty) > 1:
                    ndx, ndy = nhx - tx, nhy - ty
                    ndx = int(ndx / abs(ndx)) if ndx else ndx
                    ndy = int(ndy / abs(ndy)) if ndy else ndy
                    ntx, nty = tx + ndx, ty + ndy
                    tail = (ntx, nty)
                    tailHistory.add(tail)

        return len(tailHistory)



Solver().solve2(sample=False)