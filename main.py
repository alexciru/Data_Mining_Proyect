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
    points = read_points_from_file("iris.data")

    # start clustering
    k_means(3,points)
    
    # show results
    print("writing results on file:")
    write_results("out.data", points)
    
    return


def read_points_from_file(filename):
    f = open("iris.data", 'r')
    points = [] #create a list of points

    for line in f:
        if line is not None:
            split = line.split(',')

            new_point = Point(float(split[0]), float(split[1]))
            points.append(new_point)
    
    f.close()
    return points


def write_results(filename, points):
    f = open(filename, 'w')
    for point in points:
        f.write("%.3f , %.3f , %d \n" % (point.x , point.y , point.cluster))

    f.close
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

# set datafile sep ','
# set palette model RGB defined (0 "red",1 "blue", 2 "green")
# plot 'iris.data' using 1:2:3 notitle with points pt 7 palette