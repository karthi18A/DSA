class Solution:
    def smallestValue(self, n: int) -> int:
        def primeFactorSum(num):
            total = 0
            d = 2
            while d * d <= num:
                while num % d == 0:
                    total += d
                    num //= d
                d += 1
            if num > 1:
                total += num
            return total
        while True:
            s = primeFactorSum(n)
            if s == n:
                return n
            n = s