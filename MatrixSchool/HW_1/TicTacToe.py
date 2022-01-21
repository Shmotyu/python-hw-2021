from random import randint

n = 0
m = 0
a = []
start = 1
coordi = []
x_player = 0
y_player = 0
xy_player = ""
currentGame = False
def setup():
     global  currentGame, m, n, a
     print("Введите размер поля. Пример ввода 3 3")
     g, h = input().split()
     n = int(g) + 1
     m = int(h) + 1
     a = [0] * n
     for i in range(n):
          a[i] = [0] * m
          for j in range(m):
               a[i][j] = "#"
     currentGame = True
     for i in range(1, n):
          for j in range(1, m):
               coordi.append(str(i) + str(j))

def graphic():
     global x_free, y_free, x_player, y_player, start,xy_player, currentGame
     num = 1
     num2 = 1
     if start != 1:
               try:
                    coordi.remove(xy_player)
               except:
                    pass
     if len(coordi) == 0:
          currentGame = False
          return 0
     b_c = randint(0, len(coordi) - 1)
     bot_coord = coordi[b_c]
     bot_y = int(bot_coord[1])
     bot_x = int(bot_coord[0])
     print("БОТ ПОШЕЛ НА (", bot_x, ";", bot_y, ")", sep= "")
     start = 0

     try:
          coordi.remove(coordi[b_c])
     except:
          pass

     for i in range(n):
          for j in range(m):
               if i == 0:
                    if j == 0:
                         a[i][j] = " "
                    else:
                         a[i][j] = str(num)
                         num+=1
               else:

                    if j == 0:
                         a[i][j] = str(num2)
                         num2+=1
                    if j == x_player and i == y_player:
                         a[i][j] = "X"
                    if j == bot_x and i == bot_y:
                         a[i][j] = "O"
               print(a[i][j], sep="", end = "   ")
          print()

def checkWinTieLose():
     global currentGame, x_player, y_player, xy_player, a, m, n

     for i in range(n):
          for j in range(m):
               try:
                    if a[i][j - 1] == a[i][j] == a[i][j + 1] != "#" or a[i-1][j] == a[i][j] == a[i+1][j] != "#":
                         print("Выиграл: ", a[i][j], sep="")
                         currentGame = False
                         return 0
               except:
                    pass

     for i in range(n):
          for j in range(m):
               try:
                    if a[i-1][j-1] == a[i][j] == a[i-2][j-2] != "#" or a[i+1][j-1] == a[i][j] == a[i-1][j+1] != "#":
                         print("Выиграл: ", a[i][j],sep="")
                         currentGame = False
                         return 0
               except:
                    pass

     if len(coordi) == 0:
          print("Ничья!")
          currentGame = False
          return 0

def logic():
     global currentGame, x_player, y_player, xy_player, a, m, n
     q = 0
     checkWinTieLose()
     print("Введите координаты крестика. Пример ввода 3 3:")
     while True:
          x_player, y_player = input().split()
          x_player = int(x_player)
          y_player = int(y_player)

          xy_player = str(x_player) + str(y_player)
          print()
          print("ВАШ ХОД НА ", "(", xy_player[0], ";", xy_player[1], ")", sep="")

          if (x_player > 0 and x_player <= m) and (y_player > 0 and y_player <= n):
               for i in range(len(coordi)):
                    if coordi[i] == xy_player:
                         q+=1
                         break
               if q == 1:
                    break
               else:
                    print("Координаты заняты")

          else:
               print("Координаты не соответствуют размеру сетки")


def update():
     global currentGame
     while currentGame != False:
          checkWinTieLose()
          graphic()
          checkWinTieLose()
          logic()
          checkWinTieLose()

setup()
update()


     
