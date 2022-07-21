from collections import defaultdict
class Solution:
    def calcEquation(self, eqns: List[List[str]], val: List[float], q: List[List[str]]) -> List[float]:
        n = len(eqns)
        g = [[] for i in range(21)]
        d = defaultdict(list)
        for i in range(n):
            u,v = eqns[i]
            d[u].append([v,  val[i]])
            d[v].append([u,1/val[i]])
        def dfs(x,y):
            st = set()
            q = deque()
            q.append([x,1])
            if not d[x]:
                return -1.0
            if x == y:
                return 1.0       
            st.add(x)
            ans = None
            while q:
                node, cur = q.popleft()
                # vis[node] = 1
                for child, value in d[node]:
                    if child in st:
                        continue
                    if child == y:
                        if ans != None and ans == cur*value:
                            return -1.0
                        ans = cur*value
                    q.append([child, cur*value])
                    st.add(child)
            return ans if ans else -1.0
        
        res = []
        for x,y in q:
            # if not d[x] or d[y]:
            #     res.append(-1.0)
            #     continue
            res.append(dfs(x,y))
        return res
        
        
            
