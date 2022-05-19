# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
acron = int(input())
height = map(int, input().split())
birth = map(int, input().split())
answer = {i:[] for i in range(1,13)}
month = int(input())
for b,h in zip(birth,height):
    answer[b].append(h)
    

print(max(answer[month]) if answer.get(month) else -1)
