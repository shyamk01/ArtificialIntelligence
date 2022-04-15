#!/usr/bin/python

def displayPathtoPrincess(n, grid):
    m = -1
    p = -1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':
                m = i, j
            if grid[i][j] == 'p':
                p = i, j
    up = ""
    left = ""
    if m[0] >= p[0] and m[1] >= p[1]:
        x = abs(m[0] - p[0])
        y = abs(m[1] - p[1])
        if x == 0: x += 1
        if y == 0: y += 1
        up = "UP " * x
        left = "LEFT " * (y)
    if m[0] >= p[0] and m[1] <= p[1]:
        x = abs(m[0] - p[0])
        y = abs(m[1] - p[1])
        if x == 0: x += 1
        if y == 0: y += 1
        up = "UP " * (x)
        left = "RIGHT " * (y)
    if m[0] <= p[0] and m[1] >= p[1]:
        x = abs(m[0] - p[0])
        y = abs(m[1] - p[1])
        if x == 0: x += 1
        if y == 0: y += 1
        up = "DOWN " * (x)
        left = "LEFT " * (y)
    if m[0] <= p[0] and m[1] <= p[1]:
        x = abs(m[0] - p[0])
        y = abs(m[1] - p[1])
        if x == 0: x += 1
        if y == 0: y += 1
        up = "DOWN " * (x)
        left = "RIGHT " * (y)
    str=up+left
    str1 = str.split(" ")
    print((len(str1)))
    for i in range(len(str1)-1):
        print(str1[i].replace(' ', '\n'))


m = 3

grid = [[chr(45), chr(45), chr(45)], [chr(45), 'm', chr(45)], ['p', chr(45), chr(45)]]
print(grid)
displayPathtoPrincess(m, grid)
