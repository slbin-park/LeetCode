class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        prev = dominoes
        N = len(prev)
        if N == 1:
            return dominoes
        while True:
            curPrev = ""
            if prev[1] == 'L' and prev[0] == '.':
                curPrev += 'L'
            else:
                curPrev += prev[0]
            for i in range(1, len(prev)-1):
                if prev[i] == ".":
                    if i - 1 >= 0 and i + 1 < N:
                        if prev[i-1] == 'R'and (prev[i+1] == 'R' or prev[i+1] == '.'):
                            curPrev += 'R'
                        elif prev[i+1] == 'L' and (prev[i-1] == 'L' or prev[i-1] == '.'):
                            curPrev += 'L'
                        else:
                            curPrev += prev[i]
                    else:
                        curPrev += prev[i]
                else:
                    curPrev += prev[i]
            if prev[N-1] == '.' and prev[N-2] == 'R':
                curPrev += 'R'
            else:
                curPrev += prev[N-1]
            if curPrev == prev:
                break
            print(prev)
            print(curPrev)
            print("======")
            prev = curPrev
            
        return prev
                    

        