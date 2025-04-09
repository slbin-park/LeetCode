class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arr = []
        sumCur = 0
        nums.sort()
        for i in range(len(nums)):
            sumCur += nums[i]
        arr = [0 for i in range(sumCur+1)]
        arr[0] = 1
        for i in range(len(nums)):
            for j in range(sumCur, -1, -1):
                if arr[j - nums[i]] >= 1:
                    arr[j] += 1
        #     print(arr)
        # print(arr)
        if sumCur %2 == 1:
            return False
        if arr[sumCur//2] >= 2:
            return True
        return False

        