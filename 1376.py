class Solution:
    def numOfMinutes(self, n: int, headID: int, a: List[int], b: List[int]) -> int:
        mp=defaultdict(list)
        for i in range(len(a)):
            mp[a[i]].append(i)
        v=deque()
        v+=[[headID,b[headID]]]
        ans=0
        while v:
            x=v[0]
            v.popleft()
            for i in mp[x[0]]:
                v+=[[i,x[1]+b[i]]]
                ans=max(ans,x[1]+b[i])
        return ans
    ###
1376
###
            
