import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Load the data first method

def mcol(v):
    return v.reshape((v.size, 1))

def mrow(v):
    return v.reshape((1, v.size))

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

# Load the data second method
def load_iris_data(filename):

    # Load numerical features
    d = np.loadtxt(filename, delimiter=",", usecols=(0, 1, 2, 3)).reshape(4, 150)

    # Load and convert class labels
    labels = np.loadtxt(filename, delimiter=",", usecols=(4), dtype=str).reshape(1, 150)
    l = np.where(labels == "Iris-setosa", 0, 
        np.where(labels == "Iris-versicolor", 1, 2))

    return d, l

if __name__ == "__main__":
    # Load the data
    d, l = load("iris.csv")

    # Create masks for each class
    M0 = (l == 0)  # Mask for Iris-setosa
    M1 = (l == 1)  # Mask for Iris-versicolor
    M2 = (l == 2)  # Mask for Iris-virginica

    # Extract data corresponding to each class
    D0 = d[:, M0]  # Data for Iris-setosa
    D1 = d[:, M1]  # Data for Iris-versicolor
    D2 = d[:, M2]  # Data for Iris-virginica

    hFea = {
        0: 'Sepal length',
        1: 'Sepal width',
        2: 'Petal length',
        3: 'Petal width'
        }
    
    for dIdx in range(4):
        plt.figure()
        plt.xlabel(hFea[dIdx])
        plt.ylabel('Density')        
        plt.hist(D0[dIdx, :], bins = 10, density = True, alpha = 0.4, label = 'Setosa')
        plt.hist(D1[dIdx, :], bins = 10, density = True, alpha = 0.4, label = 'Versicolor')
        plt.hist(D2[dIdx, :], bins = 10, density = True, alpha = 0.4, label = 'Virginica')
        
        plt.legend()
        plt.tight_layout() # Use with non-default font size to keep axis label inside the figure
        plt.savefig('hist_%d.pdf' % dIdx)
    plt.show()

    for dIdx1 in range(4):
        for dIdx2 in range(4):
            if dIdx1 == dIdx2:
                continue
            plt.figure()
            plt.xlabel(hFea[dIdx1])
            plt.ylabel(hFea[dIdx2])
            plt.scatter(D0[dIdx1, :], D0[dIdx2, :], label = 'Setosa')
            plt.scatter(D1[dIdx1, :], D1[dIdx2, :], label = 'Versicolor')
            plt.scatter(D2[dIdx1, :], D2[dIdx2, :], label = 'Virginica')
        
            plt.legend()
            plt.tight_layout() # Use with non-default font size to keep axis label inside the figure
            plt.savefig('scatter_%d_%d.pdf' % (dIdx1, dIdx2))
        plt.show()

    mu = d.mean(1).reshape((d.shape[0], 1))
    print('Mean:')
    print(mu)
    DC = d - mu
    C = ((d - mu) @ (d - mu).T) / float(d.shape[1])
    print('Covariance matrix:')
    print(C)
    print()
    var = d.var(1)
    std = d.std(1)
    print('Variance:', var)
    print('Std. dev.:', std)
    print()
    
    for cls in [0,1,2]:
        print('Class', cls)
        DCls = d[:, l==cls]
        mu = DCls.mean(1).reshape(DCls.shape[0], 1)
        print('Mean:')
        print(mu)
        C = ((DCls - mu) @ (DCls - mu).T) / float(DCls.shape[1])
        print('Covariance:')
        print(C)
        var = DCls.var(1)
        std = DCls.std(1)
        print('Variance:', var)
        print('Std. dev.:', std)
        print()
        
    