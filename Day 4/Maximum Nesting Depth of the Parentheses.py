class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_num = 0
        for i in s:
            if i == "(":
                count += 1
                max_num = max(max_num, count)
            elif i == ")":
                count -= 1
        return max_num
