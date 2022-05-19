# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


class point2d:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def get_squared_dist(self, other):
        delta_x = self.x - other.x
        delta_y = self.y - other.y
        return delta_x**2 + delta_y**2
    
    def get_dist(other):
        return get_squared_dist(other)
    
def main():
    n = int(input())
    points = []
    min_dist = 10e10
    for i in range(n):
        x, y = [ int(w) for w in input().split() ]
        points.append(point2d(x,y))

    for star1 in range(len(points)-1):
        for star2 in range(star1+1,len(points)):
            dis = points[star1].get_squared_dist(points[star2])
            if dis < min_dist:
                min_dist = dis
                min_count = 1
            elif dis == min_dist:
                min_count += 1
    
    print("%.1f"%(min_dist**0.5))
    print("%d"%min_count)
    
if __name__ == "__main__":
    main()
