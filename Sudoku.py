#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[53]:


grid = [[0,4,5,0,0,0,9,0,8],[0,2,7,0,5,1,0,0,3],[0,0,0,0,8,0,0,0,0],[0,0,3,0,0,8,7,0,0],[4,8,0,0,0,0,0,3,9],[0,0,9,0,4,3,5,0,0],[0,0,0,0,1,0,0,0,0],[9,0,0,3,2,0,4,1,0],[6,0,4,0,0,0,3,2,0]]
def possible(x,y,n):
    val = grid[y][x]
    rx = x - x%3
    ry = y - y%3
    if val != 0:
        return False
    if n in grid[y]:
        return False
    for row in grid:
        if n== row[x]:
            return False
    for i in range(rx,rx+3):
        for j in range(ry,ry+3):
            if n == grid[j][i]:
                return False
    return True
def presolve(x,y):
    poss = []
    for i in range(1,10):
        if possible(x,y,i):
            poss.append(i)
    return poss
def lookup(y):
    Itable = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    for x in range(9):
        p = presolve(x,y)
        for i in p:
            Itable[i] = Itable[i] + 1
    for i in range(1,10):
        if Itable[i]==1:
            for x in range(9):
                if possible(x,y,i):
                    print(x,y,i)
                    grid[y][x]=i
                    return True
    return False
def solve():
    for y in range(9):
        if lookup(y):
            solve()
solve()
g = np.array(grid)
print(g)


# 
