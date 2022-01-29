a = [[0, 1, 1, 0, 1],
     [1, 0, 0, 0, 0],
     [0, 1, 1, 1, 1],
     [0, 1, 0, 0, 1]]

b = [[],
     [],
     [],
     []]

c = []

def finder():
    global a, b
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 1:
                if j < 4 and a[i][j] == a[i][j + 1] == 1:
                    b[i].append(j)
                    if j < 3 and a[i][j + 2] == 0:
                        b[i].append(j + 1)
                    if j == len(a[0]) - 2:
                        b[i].append(j + 1)
                if j == 0 and a[i][j] != a[i][j + 1] and a[i][j] == 1:
                    b[i].append(j)  # if j = 0
                if j == len(a[0]) - 1 and a[i][j] != a[i][j - 1] and a[i][j] == 1:
                    b[i].append(j)  # if j = length of massive
                if j < 4 and a[i][j] != a[i][j + 1] and j > 0 and a[i][j] != a[i][j - 1] and a[i][j] == 1:
                    b[i].append(j)
            else:
                b[i].append(6)
                pass


finder()

h = 1

def ife(f):
    global h, c
    q = 0
    if h == len(b):
        return

    for i in range(len(f)):
        for j in range(len(b[h])):
            if f[i] == b[h][j] != 6:
                b[h-1][j] = 9
                q += 1
    if q > 0:
        c.append(h-1)
    h += 1

def delete():
    global b
    for i in range(len(b)):
        ife(b[i])

delete()
count=0


for i in range(len(b)):
    try:
        for j in range(len(b[i])):
            if b[i][j] != 6:
                # if j!=len(b[i])-1 and j!=0 and b[i][j-1]==6 and b[i][j+1] == 6 and i!=c[0]+1:
                #     count+=1
                if j==len(b[i])-1 and b[i][j-1]==6 and b[i+1][j]==6 and i!=c[0]+1:
                    count+=1

                # if j==0 and b[i][j+1]==6 and i!=c[0]+1:
                #     count+=1
    except:
        pass

for i in range(len(b)):
    try:
        if b[i] != 9:
            for j in range(len(b[i])):
                if b[i][j] == 9:
                    del b[i]
    except:
        pass

count+=len(b)

print("Кол-во островов: ", count)
