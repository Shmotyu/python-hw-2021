import random
from random import randint

n = 5
m = 5
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
               a[i][j] = random.randint(20, 80)

create(a)
diag = m
for i in range(n):
     diag -= 1
     for j in range(m):
          if j < diag:
               a[i][j] = 0
printer(a)
print()

diag = 0
create(a)
for i in range(n):
     diag += 1
     for j in range(m):
          if j >= diag:
               a[i][j] = 0
printer(a)



