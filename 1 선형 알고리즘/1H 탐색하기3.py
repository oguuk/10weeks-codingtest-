# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def find_index(data, n):
    average = sum(data)/n
    gap = abs(data[0] - average)
    ans = 0
    for n in range(len(data)):
        if abs(data[n] - average) < gap:
            gap = abs(data[n] - average)
            ans = n
    return ans


if __name__ == "__main__":
    n = int(input())
    data = [ int(w) for w in input().split() ]
    answer = find_index(data, n)
    print(answer+1, data[answer])
