import random
import numpy as np
#Необхідно інсталювати pip install numpy

print("""
Лабораторна робота 1 з МОПЕ
Варіант: 318 max(Y)
Виконав: Май Тієн Ноанг
Перевірив: Регіда П.Г
""")

a0 = 1
a1 = 1
a2 = 3
a3 = 2

#Сгенерируем параметри x1, x2, x3
X1 = [random.randrange(1,21,1) for _ in range(8)]
X2 = [random.randrange(1,21,1) for _ in range(8)]
X3 = [random.randrange(1,21,1) for _ in range(8)]
x_matrix = np.array([X1, X2, X3])
Y = [a0 + a1*X1[i] + a2*X2[i] + a3*X3[i] for i in range(8)]
Y_max = max(Y)

#Розрахуємо X01, X02, X03
X01 = (max(X1)+min(X1))/2
X02 = (max(X2)+min(X2))/2
X03 = (max(X3)+min(X3))/2

#Розрахуємо dX1, dX2, dX3
dX1 = X01-min(X1)
dX2 = X02-min(X2)
dX3 = X03-min(X3)

#Розрахуємо Xn1, Xn2, Xn3
Xn1 = [(X1[i] - X01)/dX1 for i in range(8)]
Xn2 = [(X2[i] - X02)/dX2 for i in range(8)]
Xn3 = [(X3[i] - X03)/dX3 for i in range(8)]
Xn_matrix = np.array([Xn1, Xn2, Xn3])

#Розрахуэмо Yet
Yet = a0 + (a1 * X01) + (a2 * X02) + (a3 * X03)

def FindYet(yet, array):
    current = array[0]
    for i in range(len(array)):
        if abs(yet - array[i]) < abs(yet - current):
            current = array[i]
    return current

print("a0=%s a1=%s a2=%s a3=%s"%(a0, a1, a2, a3))
print("X1: %s"%X1)
print("X2: %s"%X2)
print("X3: %s"%X3)
print("Y: %s"%Y)
print("X01, X02, X03: %s %s %s"%(X01, X02, X03))
print("dx: %s %s %s"%(dX1, dX2, dX3))
print("Xn1: %s"%Xn1)
print("Xn2: %s"%Xn2)
print("Xn3: %s"%Xn3)
print(Xn_matrix.transpose())
print("Yэт: %s"%Yet)
print("max(Y): ", Y_max)
print("Найближче до Yet:", FindYet(Yet, Y))
