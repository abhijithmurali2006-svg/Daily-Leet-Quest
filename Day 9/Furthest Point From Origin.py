class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        x = moves.count("L")
        y = moves.count("R")
        z = moves.count("_")
        return abs(x-y) + z
