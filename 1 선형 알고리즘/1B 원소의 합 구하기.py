# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def get_sum(data, n):
    return sum(data)


if __name__ == '__main__':
    n = int(input())
    data = [ int(w) for w in input().split() ]
    answer = get_sum(data, n)
    print(answer)
