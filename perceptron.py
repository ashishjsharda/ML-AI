'''
Created on Aug 8, 2019
Perceptron -Getting Started 
@author: asharda
'''
from sklearn import datasets

#Load the iris dataset
iris=datasets.load_iris()
#Create X and Y data
X=iris.data
Y=iris.target
print(X)
print(Y)
