class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def check(a, b, start):
            if start == n:
                return True

            s = str(int(a) + int(b))

            if not num.startswith(s, start):
                return False

            return check(b, s, start + len(s))

        for i in range(1, n):
            for j in range(i + 1, n):

                first = num[:i]
                second = num[i:j]
                if (len(first) > 1 and first[0] == '0') or \
                   (len(second) > 1 and second[0] == '0'):
                    continue

                if check(first, second, j):
                    return True

        return False