class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        cnt = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j+1,len(arr)):
                    aa = abs(arr[i] - arr[j])
                    bb = abs(arr[j] - arr[k])
                    cc = abs(arr[i] - arr[k])
                    if aa <= a and bb <= b and cc <=c:
                        cnt+=1
        return cnt