import numpy as np

x = np.array([[51, 55], [14, 19], [0, 4]])
print(x)

print(x[0])
print(x[0][1])


for row in x:
    print(row)

y = x.flatten()
print(y)

print(y[np.array([0, 2, 4])])

print(y > 15)
print(y[y > 15])
