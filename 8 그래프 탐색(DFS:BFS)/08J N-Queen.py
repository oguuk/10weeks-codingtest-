# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import deque

def dfs(graph,idx,route,visit):
    for i, value in enumerate(graph[idx]):
        if value and not visit[i]:
            route += "-%d"%i
            visit[idx] = 1
            return dfs(graph,i,route,visit)
    return print(route)
    
def bfs(graph,node,answer,visit):
    q = deque([1])
    while q:
        idx = q.popleft()
        visit[idx] = 1
        
        for i,value in enumerate(graph[idx]):
            if value and not visit[i]:
                answer += "-%d"%i
                visit[i] = 1

                q.append(i)
    
    return answer
    
node, edge = map(int,input().split())

graph = [[0 for _ in range(node+1)] for _ in range(node+1)]

for _ in range(edge):
    right, left = map(int,input().split())
    graph[right][left] = 1
    graph[left][right] = 1
    
answer = bfs(graph,1,"1",[0]*(node+1))

dfs(graph,1,"1",[0]*(node+1))
print(answer)
