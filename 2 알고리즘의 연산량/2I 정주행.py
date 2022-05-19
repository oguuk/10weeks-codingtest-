# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

dic = int(input())
array = sorted(map(int,input().split()))

def solution(array):
    for idx in range(len(array)-1):
        if array[idx+1] - array[idx] != 1:
            return print("NO")
    return print("YES")

solution(array)
