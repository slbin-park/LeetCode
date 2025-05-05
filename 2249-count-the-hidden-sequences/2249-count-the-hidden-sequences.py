class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        if len(differences) == 1:
            if abs(upper - lower) < differences[0]:
                return 0
            return abs(upper - lower) - abs(differences[0]) + 1
        minV = 0
        maxV = 0
        curV = 0
        
        for i in range(len(differences)):
            curV += differences[i]
            minV = min(minV, curV)
            maxV = max(maxV, curV)
        print(minV,maxV)
        if minV > lower:
            diff = minV - lower
            minV -= diff
            maxV -= diff
        else:
            diff = lower - minV
            minV += diff
            maxV += diff
        print(minV,maxV)
        if minV < lower or maxV > upper:
            return 0
        else:
            return upper - maxV + 1
