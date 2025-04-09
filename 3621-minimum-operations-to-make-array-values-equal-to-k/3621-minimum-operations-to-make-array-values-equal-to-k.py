class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        arr = set()
        for i in range(len(nums)):
            if nums[i] < k:
                return -1
            if nums[i] > k:
                arr.add(nums[i])
        return len(arr)
        