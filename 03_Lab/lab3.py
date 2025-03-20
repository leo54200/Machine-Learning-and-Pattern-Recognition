import numpy as np
import matplotlib.pyplot as plt

def mrow (n):
    return n.reshape(1, n.size)

def mcol (n):
    return n.reshape(n.size, 1)

def load(fname):
    DList = []
    labelsList = []
    hLabels = {
        'Iris-setosa': 0,
        'Iris-versicolor': 1,
        'Iris-virginica': 2
        }

    with open(fname) as f:
        for line in f:
            try:
                attrs = line.split(',')[0:-1]
                attrs = mcol(np.array([float(i) for i in attrs]))
                name = line.split(',')[-1].strip()
                label = hLabels[name]
                DList.append(attrs)
                labelsList.append(label)
            except:
                pass

    return np.hstack(DList), np.array(labelsList, dtype=np.int32)




D, L = load("iris.csv")
mu = D.mean(axis=1)
DC = D - mcol(mu)
C = np.dot(DC, DC.T) / D.shape[1]
#print(mcol(mu))
#print(C)

s, U = np.linalg.eigh(C)
#print(s)
#print(U)
m = 2
P = U[:, ::-1][:, 0:m]
print(P)
U, s, Vh = np.linalg.svd(C)
P = U[:, 0:m]
#y = np.dot(P.T, x)
DP = np.dot(P.T, D)

plt.scatter(DP[0, L == 0], DP[1, L == 0], c='r', label='Iris-setosa')
plt.scatter(DP[0, L == 1], DP[1, L == 1], c='g', label='Iris-versicolor')
plt.scatter(DP[0, L == 2], DP[1, L == 2], c='b', label='Iris-virginica')
plt.legend()
plt.show()