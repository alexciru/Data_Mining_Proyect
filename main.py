# File: main.py
# Author: Alejandro Cirugeda
# Description:
#
#

#import numpy as np   # Library for linear algebra
#import pandas as pd  # library for data procesing
from point import Point
from clustering import k_means
# from clustering import k_means

def main():
    # read file
    f = open("iris.data", 'r')
    points = [] #create a list of points

    
    for line in f:
        if line is not None:
            split = line.split(',')

            new_point = Point(float(split[0]), float(split[1])) #extract the information about lenght and width of the sepal
            new_point.print()
            points.append( new_point )
        

    # start clustering
    k_means(3,points)
    # show results

    #TODO plot the results
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