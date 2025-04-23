class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = {}
        setArr = set()
        for answer in answers:
            if answer in dic:
                dic[answer] += 1
            else:
                setArr.add(answer)
                dic[answer] = 1
        print(dic)
        setArr = list(setArr)
        print(setArr)
        answer = 0
        for i in range(len(setArr)):
            cnt = dic[setArr[i]]
            while cnt > 0:
                answer += setArr[i] + 1
                cnt -= setArr[i] + 1
        print(answer)
        return answer
            