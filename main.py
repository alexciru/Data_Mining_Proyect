# File: main.py
# Author: Alejandro Cirugeda
# Description:
#
#

#import numpy as np   # Library for linear algebra
#import pandas as pd  # library for data procesing
import k_means
import Point

def main():
    # read file
    f = open('../iris.data', 'r')
    points = [] #create a list of points

    
    for line in f:
        line.split(",")
        points.append(Point(line[0],line[1]))
        

    # start clustering
    k_means(3,points)
    # show results
    return






if __name__ == "__main__":
    main()



"""
We will use the iris database:
And we will use the information about sepal length and width
1. sepal length in cm
   2. sepal width in cm
   3. petal length in cm
   4. petal width in cm
   5. class: 
      -- Iris Setosa
      -- Iris Versicolour
      -- Iris Virginica
"""