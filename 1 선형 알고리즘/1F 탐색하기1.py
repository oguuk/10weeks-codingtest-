# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def find_value(value, arr):
    return arr.index(value) if value in arr else -1

n, m = map(int, input().split())
data = [int(i) for i in input().split()]
print(data.index(m) if m in data else -1)

