# File: main.py
# Author: Alejandro Cirugeda
# Description:
#   The main function will read the points from a file and will call the k-means algorith to assing a cluster 
#   for each point. We will also calculate the execution time for further analissys

import time
from point import Point
from clustering import k_means

def main():
    points = read_points_from_file("iris.data")
    start_time = time.time()
    # TODO - remove all files in output folder (can be in makefile)    
    k_means(3, points)

    end_time = time.time()
    print("Execution time: %.3f" % (end_time - start_time))
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
# set palette model RGB defined (0 "black",1 "blue", 2 "green",3 "red", 4 "yellow")
# plot 'iris.data' using 1:2:3 notitle with points pt 7 palette

# plot "./initial_points.txt" u 1:2:3 with points pt 7 ps 0.5 palette