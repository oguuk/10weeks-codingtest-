# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import deque

def bfs(target):
    que = deque([[1,0]])
    while que:
        virus,time = que.popleft()
        
        if virus == target:
            return time
        else:
            if virus < 500000:
                que.append([virus*2,time+1])
            if virus > 2:
                que.append([virus//3,time+1])
    
    
time = int(input())

for _ in range(time):
    target = int(input())
    print(bfs(target))
    
