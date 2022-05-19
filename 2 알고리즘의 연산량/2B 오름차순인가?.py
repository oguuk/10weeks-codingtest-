# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def is_ordered(data, n):
    temp = data[0]
    for i in range(n):
        if temp > data[i]:
            return False
        temp = data[i]
    return True


if __name__ == "__main__":
    n = int(input())
    data = [ int(w) for w in input().split() ]
    result = is_ordered(data, n)
    if result :
        print("YES")
    else:
        print("NO")
