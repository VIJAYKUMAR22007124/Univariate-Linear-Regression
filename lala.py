import numpy as np
import matplotlib.pyplot as plt
X = np.array(eval(input()))
Y = np.array(eval(input()))
Xmean = np.mean(X)
Ymean = np.mean(Y)
num, dem = 0,0
for in range len(X):
    num += (X[i]-Xmean)-(Y[i]-Ymean)
    dem = (X[i]-Xmean)**2
m = num/dem
c=  Ymean-m*Xmean
print(m,c)
Y_pred = m*x+c
print(Y_pred)
plt.scatter(X,Y)
plt.plot(X,Y_pred, color="orange")
plt.show()
