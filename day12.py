from utils import BaseSolver
from time import sleep


class Solver(BaseSolver):

    def run1(self, text, lines):

        # build the grid and detect start and end
        _grid = list(lines)
        grid, start, end = [], None, None
        for i, line in enumerate(lines):
            grid.append([])
            for j, c in enumerate(line):
                if c == 'S':
                    start = (i, j)
                    n = ord('a')
                elif c == 'E':
                    end = (i, j)
                    n = ord('z')
                else:
                    n = ord(c)
                grid[-1].append(n)
        h, w = len(grid), len(grid[0])

        # search (naive dijkstra)
        nodes = {
            (i, j): 0 if (i, j) == start else None
            for i, row in enumerate(grid)
            for j, value in enumerate(row)
        }
        unvisited = set(nodes)
        node = start
        while end in unvisited:
            i, j = node
            distance = nodes[node]
            for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                ni, nj = i + di, j + dj
                if (ni, nj) in unvisited:
                    if grid[i][j] - grid[ni][nj] >= -1:                                
                        currentDistance = nodes[(ni,nj)]
                        nextDistance = distance + 1
                        nodes[(ni,nj)] = min(currentDistance, nextDistance) if (currentDistance is not None) else nextDistance
            unvisited.remove(node)
            possible = sorted([n for n in unvisited if nodes[n] is not None], key=nodes.get)
            if possible:
                node = possible[0]
            else:
                break

        return nodes[end]

    def run2(self, text, lines):

        # build the grid and detect start and end
        grid, starts, end = [], [], None
        for i, line in enumerate(lines):
            grid.append([])
            for j, c in enumerate(line):
                c = c.replace('S', 'a')
                if c == 'E':
                    end = (i, j)
                    n = ord('z')
                else:
                    n = ord(c)
                    if c == 'a':
                        starts.append((i,j))
                grid[-1].append(n)
        h, w = len(grid), len(grid[0])

        # search (naive dijkstra)
        shortest = None
        for start in starts:
            nodes = {
                (i, j): 0 if (i, j) == start else None
                for i, row in enumerate(grid)
                for j, value in enumerate(row)
            }
            unvisited = set(nodes)
            node = start
            while end in unvisited:
                i, j = node
                distance = nodes[node]
                for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                    ni, nj = i + di, j + dj
                    if (ni, nj) in unvisited:
                        if grid[i][j] - grid[ni][nj] >= -1:                                
                            currentDistance = nodes[(ni,nj)]
                            nextDistance = distance + 1
                            nodes[(ni,nj)] = min(currentDistance, nextDistance) if (currentDistance is not None) else nextDistance
                unvisited.remove(node)
                possible = sorted([n for n in unvisited if nodes[n] is not None], key=nodes.get)
                if possible:
                    node = possible[0]
                else:
                    break
            if nodes[end] is not None:
                shortest = min(shortest, nodes[end]) if (shortest is not None) else nodes[end]

        return shortest


Solver().solve2(sample=True)
Solver().solve2(sample=False)