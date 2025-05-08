import heapq


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        N = len(moveTime)
        M = len(moveTime[0])
        arr = [[[1e9 * 2, 1e9 * 2, 1e9 * 2] for i in range(M)] for i in range(N)]
        arr[0][0] = [0, 0, 0]
        heap = []
        # n, m, t, (1,2)
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        heapq.heappush(heap, [0, 2, 0, 0])
        while heap:
            t, turn, n, m = heapq.heappop(heap)
            # print(n,m,t,turn)
            nextTurn = 1 if turn == 2 else 2
            for i in range(4):
                nx = n + dx[i]
                ny = m + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    nextTime = t + nextTurn
                    if moveTime[nx][ny] > t:
                        nextTime = moveTime[nx][ny] + nextTurn
                    if arr[nx][ny][nextTurn] > nextTime:
                        if nx == n - 1 and ny == m - 1:
                            return nextTime
                        arr[nx][ny][nextTurn] = nextTime
                        heapq.heappush(heap, [nextTime, nextTurn, nx, ny])
        # for i in range(N):
        # print(arr[i])
        # print(arr[N-1][M-1])
        return min(arr[N - 1][-1])
