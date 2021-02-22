import random
import numpy as np
#Необхідно інсталювати pip install numpy

print("""
Лабораторна робота 1 з МОПЕ
Варіант: 318 max(Y)
Виконав: Май Тієн Ноанг
Перевірив: Регіда П.Г
""")

a0 = int(input("Enter a0: "))
a1 = int(input("Enter a1: "))
a2 = int(input("Enter a2: "))
a3 = int(input("Enter a3: "))
a = [a0, a1, a2, a3]

#Сгенерируем параметри x1, x2, x3
x = [[random.randint(20, 50) for i in range(8)],
     [random.randint(20, 50) for i in range(8)],
     [random.randint(20, 50) for i in range(8)]]
x_matrix = np.array([x[0], x[1], x[2]])

Y = [a[0] + (a[1] * x[0][i]) + (a[2] * x[1][i]) + (a[3] * x[2][i]) for i in range(8)]

Y_max = max(Y)

#Розрахуємо X01, X02, X03
x0 = [(max(x[0]) + min(x[0])) / 2,
      (max(x[1]) + min(x[1])) / 2,
      (max(x[2]) + min(x[2])) / 2]

#Розрахуємо dX1, dX2, dX3
dx = [x0[0] - min(x[0]),
      x0[1] - min(x[1]),
      x0[2] - min(x[2])]

#Розрахуємо Xn1, Xn2, Xn3
xn = [[(x[0][i] - x0[0]) / dx[0] for i in range(8)],
      [(x[1][i] - x0[1]) / dx[1] for i in range(8)],
      [(x[2][i] - x0[2]) / dx[2] for i in range(8)]]

xn_matrix = np.array([xn[0], xn[1], xn[2]])

#Розрахуэмо Yet
Yet = a[0] + (a[1] * x0[0]) + (a[1] * x0[1]) + (a[2] * x0[2])

print("X1 X2 X3:" + "\n", x_matrix.transpose())
print("Y: ", Y)
print("x01, x02, x03: ", x0[0], x0[1], x0[2])
print("dx1, dx2, dx3: ", dx[0], dx[1], dx[2])
print("Xn1, Xn2, xn3:" + "\n", xn_matrix.transpose())
print("Yэт: %s"%Yet)
print("max(Y): ", Y_max)
