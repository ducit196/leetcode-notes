
class Solution:
    #Idea: find the best solution between skip or take
    def knapSack(self, W, wt, val):
        mem = {}
        def dp(w, i):
            #Base case:
            if i == -1:
                return 0
            skip = dp(w, i -1)
            take = 0
            if w >= wt[i]:
                take = dp(w - wt[i], i - 1) + val[i]
            return max(skip, take)
        return dp(W, len(val) - 1)

        #bottom up solution
        dp = []



W = 4
wt = [4,5,1]
val = [1,2,3]
print(Solution().knapSack(W, wt, val))