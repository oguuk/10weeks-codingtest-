# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import deque

dx = [1,-1,0,0] #오른쪽, 왼쪽, 아래, 위
dy = [0,0,1,-1]

def dfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= len(map_[0]) or ny >= len(map_):
                continue
            
            if map_[ny][nx] == 0:
                continue
                
            if map_[ny][nx] == 1:
                map_[ny][nx] = map_[y][x] + 1
                queue.append((nx,ny))
    
    return map_[destination[0]][destination[1]]-1

row,col = map(int,input().split())
map_ = [[]for _ in range(row)]

start = [0,0]
destination = [row-1,col-1]
answer = []

for r in range(row):
    for c,char in enumerate(input()):
        if char == "S":
            start = [r,c]
            
        if char == "E":
            destination = [r,c]
            
        if char == "#":
            map_[r].append(0)
        else:
            map_[r].append(1)

print(dfs(start[0],start[1]))
