# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def bubble(data,num):
    for i in range(num):
        for j in range(num-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    
num = int(input())
data = [int(i) for i in input().split()]
bubble(data,num)
for i in data:
    print(i,end=' ')
