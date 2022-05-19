# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean



def range_sum_from_one(n):
    return n*(n+1)//2

def getAnswer(n):
    answer = 0
    for i in range(1,n+1):
        answer += range_sum_from_one(i)
        
    return answer

if __name__ == "__main__":
    n = int(input())
    answer = getAnswer(n)
    print(answer)
