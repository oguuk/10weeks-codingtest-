# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
size = int(input())
apt = []
asc = []
estate = 0
count = 0


def dfs(x,y):
    global count
    
    if x < 0 or y < 0 or x >= size or y >= size:
        return False
    
    if apt[y][x]:
        apt[y][x] = 0
        count += 1
        
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    
    return False
    

for i in range(size):
    line = list(map(int,input().split()))
    apt.append(line)
    
for r in range(size):
    for c in range(size):
        if dfs(r,c):
            estate += 1
            asc.append(count)
            count = 0

print(estate)
for i in sorted(asc):
    print(i)
    
