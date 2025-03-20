'''
'Project
The project task consists of a binary classification problem. The goal is to perform fingerprint spoofing
detection, i.e. to identify genuine vs counterfeit fingerprint images. The dataset consists of labeled
samples corresponding to the genuine (True, label 1) class and the fake (False, label 0) class. The
samples are computed by a feature extractor that summarizes high-level characteristics of a fingerprint
image. The data is 6-dimensional.
The training files for the project are stored in file Project/trainData.txt. The format of the file is
the same as for the Iris dataset, i.e. a csv file where each row represents a sample. The first 6 values of
each row are the features, whereas the last value of each row represents the class (1 or 0). The samples
are not ordered.
Load the dataset and plot normalized histograms and pair-wise scatter plots of the different features.
Analyze the plots.
1. Analyze the first two features. What do you observe? Do the classes overlap? If so, where? Do the
classes show similar mean for the first two features? Are the variances similar for the two classes?
How many modes are evident from the histograms (i.e., how many “peaks” can be observed)?
2. Analyze the third and fourth features. What do you observe? Do the classes overlap? If so, where?
Do the classes show similar mean for these two features? Are the variances similar for the two
classes? How many modes are evident from the histograms?
3. Analyze the last two features. What do you observe? Do the classes overlap? If so, where? How
many modes are evident from the histograms? How many clusters can you notice from the scatter
plots for each class?'
'''
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def load_data(file_path):
    data = np.loadtxt(file_path, delimiter=',')
    features = data[:, :-1]
    labels = data[:, -1]
    return features, labels

if __name__ == '__main__':
    data, label = load_data('trainData.txt')
    print(data.shape)
    print(label.shape)

    M0 = label == 0
    M1 = label == 1
    print(M0)
    D0 = data[M0, :]
    D1 = data[M1, :]
    for i in range(6):
        plt.figure()
        plt.hist(D0[:, i], density = True, alpha = 0.4, bins=10, label = 'False')
        plt.hist(D1[:, i], density = True, alpha = 0.4, bins=10, label = 'True')
        
        plt.title('Feature ' + str(i+1))
        plt.xlabel('Value')
        plt.ylabel('Density')
        plt.legend()
        plt.tight_layout() # Use with non-default font size to keep axis label inside the figure
        plt.savefig('hist_%d.pdf' % i)
    plt.show()

    for i in range(6):
        for j in range(6):
            if i == j:
                continue
            plt.figure()
            plt.xlabel(i)
            plt.ylabel(j)   
            plt.scatter(D0[:, i], D0[:, j], label = 'False')
            plt.scatter(D1[:, i], D1[:, j], label = 'True')
            plt.title('Feature ' + str(i+1))
            plt.xlabel('Value')
            plt.ylabel('Frequency')
            plt.legend()
            plt.tight_layout() # Use with non-default font size to keep axis label inside the figure
            plt.savefig('scatter_%d.pdf' % i)
    plt.show()
