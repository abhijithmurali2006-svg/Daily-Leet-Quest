class Solution:
    def judgeCircle(self, v: str) -> bool:
        x = 0
        y = 0
        
        for move in v:
            if move == 'R':
                x += 1
            elif move == 'L':
                x -= 1
            elif move == 'U':
                y += 1
            elif move == 'D':
                y -= 1

        return x == 0 and y == 0
