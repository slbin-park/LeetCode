class Solution:
    def numTilings(self, n: int) -> int:
        arr = [0 for i in range(1001)]
        arr[0] = 0
        arr[1] = 1
        arr[2] = 2
        arr[3] = 5
        arr[4] = 11
        for i in range(4,n+1):
            arr[i] = (arr[i-1] * 2 +arr[i-3]) % (10**9 + 7)
        return arr[n]