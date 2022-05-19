# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

#두 수중에 더 큰 값을 반환하는 함수
def get_max(a, b):
    if a > b:
        return a;
    elif a == b:
        return a;
    else:
        return b;
    
if __name__ == '__main__':
    a, b = [ int(w) for w in input().split() ]
    answer = get_max(a, b)
    print(answer)
