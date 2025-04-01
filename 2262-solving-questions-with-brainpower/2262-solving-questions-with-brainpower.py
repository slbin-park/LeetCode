class Solution:

    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        arr = [0 for i in range(N + 1)]
        if questions[0][1] + 1 < N:
            arr[questions[0][1] + 1] = questions[0][0]
        for i in range(1, N):
            plus = i + questions[i][1] + 1
            arr[i] = max(arr[i - 1], arr[i])
            if plus < N:
                arr[plus] = max(arr[plus], arr[i] + questions[i][0])
        answer = 0
        for i in range(N):
            answer = max(answer, arr[i] + questions[i][0])
        return answer
