class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxNum = max(nums)
        arr = []
        for i in range(len(nums)):
            if nums[i] == maxNum:
                arr.append(i)
        answer = 0
        prevIndex = 0
        print(arr)
        for i in range(len(arr)):
            curI = i + k - 1
            # print(answer)
            # print(i,curI)
            if curI < len(arr):
                # print("??")
                answer += (arr[i] - prevIndex + 1) * (len(nums) - arr[curI])
                prevIndex = arr[i] + 1
            elif len(arr) - i == k:
                answer += (arr[i] - prevIndex) + (len(nums) - arr[-1])
        print(answer)
        return answer  

