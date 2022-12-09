from utils import BaseSolver


class Solver(BaseSolver):

    LEGEND = {
        'A': 0,
        'B': 1,
        'C': 2,
        'X': 0,
        'Y': 1,
        'Z': 2,
    }

    OUTCOMES = (
        (3, 6, 0),
        (0, 3, 6),
        (6, 0, 3)
    )

    def run1(self, text, lines):

        total = 0
        
        for line in lines:

            a, b = line[0], line[-1]
            a, b = self.LEGEND[a], self.LEGEND[b]
            
            score = 0
            score += b + 1 # 1 for rock, 2 for paper, 3 for scissors
            score += self.OUTCOMES[a][b]
            total += score
            

        return total

    def run2(self, text, lines):

        total = 0
        
        for line in lines:
            opponent, outcome = line[0], line[-1]
            score = self.LEGEND[outcome] * 3
            score += self.OUTCOMES[self.LEGEND[opponent]].index(score) + 1
            total += score

        return total


Solver().solve2(sample=False)

            

            