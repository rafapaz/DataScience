import numpy as np


A = np.random.rand(5, 5)
print(A)
A[A >= 0.5] = 1
A[A < 0.5] = 0
print(A)