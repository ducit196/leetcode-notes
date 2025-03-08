

class Solution:
    def solution(self, songs, animation):
        n = len(songs)
        m = len(animation)
        ans = []
        for i in range(n):
            for j in range(m):
                name,lenght = songs[i].s