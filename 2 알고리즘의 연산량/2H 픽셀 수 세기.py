# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

num = int(input())
circles = []

for circle in range(num):
    circles.append(int(input()))

def CountPixel(circles,num):

    for c in range(num):
        pixel = 0
        edge = circles[c]
        for y in range(0,circles[c]+1):
            for x in range(edge,-1,-1):
                if x*x + y*y <= circles[c]**2:
                    pixel += edge
                    break
                else:
                    edge -= 1

        print("#%d"%(c+1))
        print(pixel*4)

CountPixel(circles,num)
            
    
    
