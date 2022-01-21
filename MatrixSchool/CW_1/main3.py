n = 4
m = 4
a = [0] * n
b = [0] * n


def printer(a):
    for i in range(n):
        for j in range(m):
            print("{:4d}".format(a[i][j]), end="")
        print()

def create(a):
    h = 1
    for i in range(n):
        a[i] = [0] * m
        for j in range(m):
            a[i][j] = h
            h+=1

create(a)
create(b)
for i in range(n):
     for j in range(m):
         b[i][j]=a[j][i]
printer(b)
