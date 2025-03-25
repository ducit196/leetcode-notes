from collections import deque
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(ingredients)
        ans = []
        supplies = set(supplies)
        q = deque(range(n))
        lastSupliesLen = 0
        while len(supplies) > lastSupliesLen:
            lastSupliesLen = len(supplies)
            visited = set()
            while q:
                if q[0] in visited:
                    break
                currentProcess = q.popleft()
                visited.add(currentProcess)
                canMade = True
                for ingre in ingredients[currentProcess]:
                    if ingre not in supplies:
                        canMade = False
                        break
                if canMade:
                    ans.append(recipes[currentProcess])
                    supplies.add(recipes[currentProcess])
                else:
                    q.append(currentProcess)
        return ans
recipes = ["bread"]
ingredients = [["yeast","flour"]]
supplies = ["yeast","flour","corn"]
print(Solution().findAllRecipes(recipes, ingredients, supplies))