# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solve(data, n, p, q):
    addedAllPeopleWeight = 0
    people = 0
    for weight in data:
        if weight <= p:
            people +=1
            addedAllPeopleWeight += weight
    
    if addedAllPeopleWeight <= q:
        print(people,addedAllPeopleWeight,"\nYES")
    else:
        print(people,addedAllPeopleWeight,"\nNO")
    pass


if __name__ == "__main__":
    n, p, q = [ int(w) for w in input().split() ]
    data = [ int(w) for w in input().split() ]
    solve(data, n, p, q)
