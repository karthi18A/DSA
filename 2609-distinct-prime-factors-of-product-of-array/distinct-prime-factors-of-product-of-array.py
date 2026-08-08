class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primes=set()
        for n in nums:
            i=2
            while i*i<=n:
                while n%i==0:
                    primes.add(i)
                    n//=i
                i+=1
            if n>1:
                primes.add(n)
        return len(primes)        