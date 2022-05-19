# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def get_indexes(schools, n):
    first_index = -1
    last_index = -1
    for index, front in enumerate(schools):
        if front == "AJOU":
            first_index = index+1
            break
    for index, back in enumerate(schools[::-1]):
        if back == "AJOU":
            last_index = len(schools) - index
            break
    return first_index,    last_index
    
    

if __name__ == '__main__':
    n = int(input())
    schools = [ input() for i in range(n) ]
    indexes = get_indexes(schools, n);
    print( "{0} {1}".format( indexes[0], indexes[1]) )
