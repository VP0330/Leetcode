class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeroCount=0
        while n:
            n//=5
            zeroCount+=n
        return zeroCount