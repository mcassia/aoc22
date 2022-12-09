from utils import BaseSolver


class Solver(BaseSolver):

    def run1(self, text, lines):

        grid = [
            [int(height) for height in line]
            for line in lines
        ]

        def getSegments(i, j):
            return [
                grid[i][:j], # left
                grid[i][j+1:], # right
                [row[j] for row in grid[:i]], # top
                [row[j] for row in grid[i+1:]], # bottom
            ]

        visibleCount = 0
        for i, row in enumerate(grid):
            for j, height in enumerate(row):
                for segment in getSegments(i, j):
                    if all(height > otherHeight for otherHeight in segment):
                        visibleCount += 1
                        break

        return visibleCount

    def run2(self, text, lines):

        grid = [
            [int(height) for height in line]
            for line in lines
        ]

        def getSegments(i, j):
            return [
                list(reversed(grid[i][:j])), # left
                grid[i][j+1:], # right
                list(reversed([row[j] for row in grid[:i]])), # top
                [row[j] for row in grid[i+1:]], # bottom
            ]

        maximumScore = 0
        for i, row in enumerate(grid):
            for j, height in enumerate(row):
                score = 1
                for segment in getSegments(i, j):
                    distance = 0
                    for otherHeight in segment:
                        distance += 1
                        if otherHeight >= height:
                            break
                    score *= distance
                maximumScore = max(maximumScore, score)

        return maximumScore


Solver().solve2(sample=False)