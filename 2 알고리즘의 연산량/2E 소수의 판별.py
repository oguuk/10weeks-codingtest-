# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

import math
def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)):
        if (n % i) == 0:
            return False
    return True

if __name__ == "__main__":
    caseSize = int(input())
    for i in range(1,caseSize+1):
        print("Case #%d"%i)
        n = int(input())
        if is_prime(n):
            print("YES")
        else:
            print("NO")
