class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        def dfs(i):
            isConnected[i][i] = 0
            for j in range(n):
                if isConnected[i][j] == 1 and isConnected[j][j] == 1:
                    dfs(j)
            
                        
        province = 0
        for i in range(n):
            if isConnected[i][i] == 1:
                province +=1
                dfs(i)

        return province 
        