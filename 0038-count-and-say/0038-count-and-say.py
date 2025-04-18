class Solution:
    N = 1

    def countAndSay(self, n: int) -> str:
        self.N = n

        def createStr(str1, n):
            # print(str1, n)
            if self.N == n:
                return str1
            curStr = ""
            lastIndex = 0
            for i in range(1, len(str1)):
                if str1[i] != str1[i - 1]:
                    c = str(i - lastIndex)
                    d = str1[i - 1]
                    curStr += c + d
                    lastIndex = i
            # if len(str1) == 1:
            #     return createStr("1" + str(str1[0]), n + 1)
            c = str(len(str1) - lastIndex)
            # print("len = ", len(str1))
            # print("s1 = ", str1)
            d = str1[len(str1) - 1]
            curStr += c + d

            # print("curStr =", curStr)
            return createStr(curStr, n + 1)

        result = createStr("1", 1)
        return result
