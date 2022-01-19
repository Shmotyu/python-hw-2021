import random
from random import randint

n = 7
m = 7
a = [0] * n

def printer(a):
     for i in range(n):
          for j in range(m):
               print("{:4d}".format(a[i][j]), end = "")
          print()

def create(a):
    for i in range(n):
        a[i] = [0] * m
        for j in range(m):
            a[i][j] = 0


create(a)
diag = m
for i in range(n):
     diag -= 1
     for j in range(m):
          if j >= diag:# РИСУНОК 1
               a[i][j] = 99
printer(a)
print()

create(a)
diag = m
for i in range(n):
     diag -= 1
     for j in range(m):
          if j <= diag:# РИСУНОК 2
               a[i][j] = 99
printer(a)
print()

create(a)
point = (m // 2)
h = -1
current = 0
for i in range(n):
     h += 1
     if (i <= point):
        current = i
     else:
         current-=1
     for j in range(m):
          if j >= point-current and j <= point+current: #РИСУНОК 3
              a[i][j] = 99
printer(a)


