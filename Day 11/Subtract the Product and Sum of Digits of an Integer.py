class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        dsum = 0
        dproduct = 1

        while n > 0:
            digit = n % 10
            dsum += digit
            dproduct *= digit
            n = n // 10
            
        return dproduct - dsum
