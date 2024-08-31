import numpy as np

x = 2.57 * 10**3
f = 0.873

y = (np.sin((np.pi/8 - f)**2) + (3+x**2)**(1/4)) / 2

print("Ответ: y = ", y)


X1 = np.ones(12)
X2 = np.random.randint(16, 28, 12)
X3 = np.random.randint(60, 82, 12)
X = np.vstack((X1, X2, X3))
X = X.transpose()

Y = np.random.uniform(13.5, 18.6, 12)

A = np.dot(np.linalg.inv(np.dot(np.transpose(X), X)), np.dot(np.transpose(X), Y))
print("Вектор оценок равен: ", A)

Y2 = A[0] + A[1]*X2 + A[2]*X3
print("Y равен: ", Y)
print("Y найденный по формуле равен: ", Y2)
