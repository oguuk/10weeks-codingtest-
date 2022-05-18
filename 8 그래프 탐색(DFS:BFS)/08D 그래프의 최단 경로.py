# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import deque

vertex, edge = map(int,input().split())
start, target = map(int,input().split())
graph = {i:[] for i in range(1,vertex+1)}

for _ in range(edge):
    r, l = map(int,input().split())
    graph[r].append(l)
    graph[l].append(r)

que = [start]
memory = []
visit = [0]*(vertex+1)

answer = 0

while memory or que:
    if not que:
        answer += 1
        que = memory
        memory = []
        continue
    
    if target in que:
        print(answer)
        break
        
    for i in que:
        if not visit[i]:
            memory += graph[i]
    
    for i in que:
        visit[i] = 1
    
    que = []
    
    
    
