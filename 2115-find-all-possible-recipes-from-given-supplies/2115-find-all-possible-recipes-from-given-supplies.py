class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        dic = {}
        answer = []

        for supply in supplies:
            dic[supply] = 1
        tmp = []
        for i in range(len(recipes)):
            tmp.append([i,recipes[i]])
        while True:
            curTmp = []
            for i, recipe in tmp:
                flag = 1
                for j in range(len(ingredients[i])):
                    if ingredients[i][j] not in dic:
                        flag = 0
                        break
                if flag:
                    dic[recipe] = 1
                    answer.append(recipe)
                else:
                    curTmp.append([i, recipe])
            if len(tmp) == len(curTmp):
                return answer
            tmp = curTmp
        