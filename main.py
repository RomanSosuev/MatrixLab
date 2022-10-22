import numpy as np
from numpy import linalg

inpSize = int(input("Введите размерность матрицы: "))
A = np.random.randint(10, size=(inpSize, inpSize))
rg = np.linalg.matrix_rank(A)
print("Матрица А\n", A)
print("Ранг матрицы: ", rg)
accuracy = int(input('Введите количество знаков после запятой: '))
n = 1
summa = 0
currFact = 2
difference = 1
buff = 0
det = np.linalg.det(A)
while abs(difference) > (0.1 ** accuracy):
    fact = 3*n - 1
    buff += summa
    n += 1
    currDet = det * fact ** inpSize
    summa = currDet / currFact * (-1) ** n
    currFact = currFact * (3 * n - 3) * (3 * n - 2) * fact
    difference = abs(summa - buff)
    buff = 0
    print(n - 1, ' :  Сумма: ', summa, ' Разность: ' , difference)
print("\nСумма знакопеременного ряда: " , summa)
