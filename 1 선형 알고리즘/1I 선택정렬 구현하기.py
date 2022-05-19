# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def find_min_index(data, begin, end):
    min_index = begin
    for idx in range(begin,end):
        if data[idx] < data[min_index]:
            min_index = idx
    return min_index

def selection_sort(data, n):
    for i in range(n):
        min_index = find_min_index(data,i,n)
        temp = data[i]
        data[i] = data[min_index]
        data[min_index] = temp

if __name__ == "__main__":
    n = int(input())
    data = [ int(w) for w in input().split() ]
    selection_sort(data, n)
    print(" ".join([str(w) for w in data]))

    
