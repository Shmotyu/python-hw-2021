n = 4
m = 5
a = [[0,1,1,0,1],
     [0,0,0,1,0],
     [1,0,1,1,0],
     [1,1,1,0,0]]
q = 0

for i in range(n):
    for j in range(m):
        try:
            if a[i][j-1] != a[i][j] and j!= m-1 and j != 0:
                q+=1
        except:
            pass

print(q)
