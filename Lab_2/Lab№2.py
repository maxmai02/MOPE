import random
import numpy as np
import math
#Май Тієн Ноанг ІО-93 вар: 318

m=6
x1_min,x1_max = 20,70
x2_min,x2_max = -15,45
y_max = (30 - 11) * 10
y_min = (20 - 11) * 10

def Func(a, b):
    if a >= b:
        return a / b
    else:
        return b / a


y=[[random.randint(y_min, y_max) for j in range(m)] for i in range(3)]

y_srednie=[]

for i in range(len(y)):
    SrednieY1 = 0
    for j in y[i]:
        SrednieY1 +=j
    y_srednie.append(SrednieY1/m)



Dispersia = [(np.var(y[0])),
             (np.var(y[1])),
             (np.var(y[2]))]

sigma = math.sqrt((2 * (2 * m - 2)) / (m * (m - 4)))

Fuv = [(Func(Dispersia[0], Dispersia[1])),
      (Func(Dispersia[2], Dispersia[0])),
      (Func(Dispersia[2], Dispersia[1]))]


Ouv = [(((m - 2) / m) * Fuv[0]),
      (((m - 2) / m) * Fuv[1]),
      (((m - 2) / m) * Fuv[2])]


Ruv = [((abs(Ouv[0] - 1) / sigma)),
      ((abs(Ouv[1] - 1) / sigma)),
      ((abs(Ouv[2] - 1) / sigma))]

kr = 2
for i in Ruv:
    if i > kr:
        Proverka="Помилка, дисперсія неоднорідна"
    else:
        Proverka=("дисперсія однорідна")

xn = [[-1, -1], [-1,  1], [1,  -1]]

mx = [((xn[0][0] + xn[1][0] + xn[2][0]) / 3),
      ((xn[0][1] + xn[1][1] + xn[2][1]) / 3)]

my = (y_srednie[0] + y_srednie[1] + y_srednie[2]) / 3

a1 = (xn[0][0] ** 2 + xn[1][0] ** 2 + xn[2][0] ** 2) / 3
a2 = (xn[0][0] * xn[0][1] + xn[1][0] * xn[1][1] + xn[2][0] * xn[2][1]) / 3
a3 = (xn[0][1] ** 2 + xn[1][1] ** 2 + xn[2][1] ** 2) / 3
a11 = (xn[0][0] * y_srednie[0] + xn[1][0] * y_srednie[1] + xn[2][0] * y_srednie[2]) / 3
a22 = (xn[0][1] * y_srednie[0] + xn[1][1] * y_srednie[1] + xn[2][1] * y_srednie[2]) / 3

b0=(np.linalg.det([[my, mx[0], mx[1]],[a11, a1, a2],[a22, a2, a3]])/np.linalg.det([[1, mx[0], mx[1],],[mx[0], a1, a2],[mx[1], a2, a3]]))
b1=(np.linalg.det([[1, my, mx[1]],[mx[0], a11, a2],[mx[1], a22, a3]])/np.linalg.det([[1, mx[0], mx[1]],[mx[0], a1, a2],[mx[1], a2, a3]]))
b2=(np.linalg.det([[1, mx[0], my],[mx[0], a1, a11],[mx[1], a2, a22]])/np.linalg.det([[1, mx[0], mx[1]],[mx[0], a1, a2],[mx[1], a2, a3]]))

Tx1=abs(x1_max - x1_min) / 2
Tx2=abs(x2_max - x2_min) / 2
x10=(x1_max + x1_min) / 2
x20=(x2_max + x2_min) / 2
a0 = b0 - (b1 * x10 / Tx1) - (b2 * x20 / Tx2)
a1 = b1 / Tx1
a2 = b2 / Tx2


yn1 = a0 + a1 * x1_min + a2 * x2_min
yn2 = a0 + a1 * x1_max + a2 * x2_min
yn3 = a0 + a1 * x1_min + a2 * x2_max


print("y = ")
for row in y:
    print(' | '.join([str(elem) for elem in row]))


print("середнє значення функції відгуку в рядках {}\nдисперсії по рядках - {}\nосновне відхилення - {}\nFuv - {}\nOuv - {}\nRuv - {}\nПеревірка - {}\nb0 - {}\nb1 - {}\nb2 - {}\n ".format(y_srednie,Dispersia,sigma,Fuv,Ouv,Ruv,Proverka,b0,b1,b2))
print("Перевірка")
print(round((b0-b1-b2),1))
print(round((b0+b1-b2),1))
print(round((b0-b1+b2),1))
print("∆x1 = {} ∆x2 = {} x10 = {} x20= {} a0 = {} a1 = {} a2 = {}".format(Tx1,Tx2,x10,x20,a0,a1,a2))
print("Перевірка")
print(yn1,yn2,yn3)
