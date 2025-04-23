class Solution:
    def countLargestGroup(self, n: int) -> int:
        dic = {}
        arr = [0 for i in range(37)]
        maxL = 0
        for i in range(1, n+1):
            curStr = str(i)
            curSum = 0
            for j in range(len(curStr)):
                curSum += int(curStr[j])
            arr[curSum] += 1
            maxL = max(maxL, arr[curSum])
        maxV = 0
        for i in range(len(arr)):
            if arr[i] == maxL:
                maxV += 1
        return maxV