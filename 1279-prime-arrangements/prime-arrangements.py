class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7

        def isPrime(x):
            if x < 2:
                return False

            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1

            return True

        primes = 0

        for i in range(1, n + 1):
            if isPrime(i):
                primes += 1

        def fact(x):
            ans = 1
            for i in range(2, x + 1):
                ans = (ans * i) % MOD
            return ans

        return (fact(primes) * fact(n - primes)) % MOD