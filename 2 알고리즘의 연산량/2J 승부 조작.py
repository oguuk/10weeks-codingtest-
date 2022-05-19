num, choice = map(int,input().split())
cups = [int(i) for i in input().split()]

def solution(choice, cups):
    temp = sum((cups[:choice]))
    idx = 0
    for a in range(choice,len(cups)):
        if temp % 2 == 0:
            return print("YES")
        temp += cups[a]
        temp -= cups[idx]
        idx +=1
    return print("NO") if temp % 2 != 0 else print("YES")

solution(choice, cups)
