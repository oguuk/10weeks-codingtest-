# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
m, n = map(int,input().split())
box = []
whole_day = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(y,x,day):
    global whole_day
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or ny < 0 or ny >= len(box) or nx >= len(box[0]):
            if day > whole_day:
                whole_day = day
            continue
        
        if not box[ny][nx]:
            box[ny][nx] = 1
            dfs(ny,nx,day+1)
            
    return
    
ripe_tomato = []

for r in range(n):
    line = list(map(int,input().split()))
    box.append(line)
    
    for c,v in enumerate(line):
        if v == 1:
            ripe_tomato.append((r,c))

for start in ripe_tomato:
    y,x = start
    dfs(y,x,0)

flag = 1
for line in box:
    if 0 in line:
        flag = 0
        break
        
print(whole_day) if flag else print(-1)
