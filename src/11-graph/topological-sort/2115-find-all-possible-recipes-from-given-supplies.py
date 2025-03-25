from collections import deque, defaultdict
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        supplies = set(supplies)
        recipesToIndex = {recipe: i for i, recipe in enumerate(recipes)}
        indegre = [0] * n
        dependencyMap = defaultdict(list)
        #Build dependency
        for i, ingredientList in enumerate(ingredients):
            for ingre in ingredientList:
                if ingre not in supplies:
                    dependencyMap[ingre].append(recipes[i])
                    indegre[i] += 1
        q = deque()
        for i in range(n):
            if indegre[i] == 0:
                q.append(i)
        ans = []
        while q:
            currentProcess = q.popleft()
            #Remove depenency
            for dependant in dependencyMap[recipes[currentProcess]]:
                indegre[recipesToIndex[dependant]] -= 1
                if indegre[recipesToIndex[dependant]] == 0:
                    q.append(recipesToIndex[dependant])
            supplies.add(recipes[currentProcess])
            ans.append(recipes[currentProcess])
        return ans
recipes = ["bread","sandwich","burger"]
ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
supplies = ["yeast","flour","meat"]
print(Solution().findAllRecipes(recipes, ingredients, supplies))