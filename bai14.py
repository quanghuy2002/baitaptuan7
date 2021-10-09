import numpy as np

x = np.array([[14, 96],
              [46, 82],
              [80, 67],
              [77, 91],
              [99, 87]])

print("X = ", x)

print("Giá trị lớn nhất: ", np.amax(x))
print("Giá trị bé nhất: ", np.amin(x))