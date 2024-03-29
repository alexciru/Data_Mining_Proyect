# File: main.py
# Author: Alejandro Cirugeda
# Description:
#   The main function will read the points from a file and will call the k-means algorith to assing a cluster 
#   for each point. We will also calculate the execution time for further analissys

import time
from point import Point
from clustering import k_means
from point import Point

N_KLUSTERS = 3
N_THREADS = 10

#FILENAME = "iris.data"
#FILENAME = "cluster_1500.txt"
#FILENAME = "cluster_2500.txt"
FILENAME = "cluster_8000.txt"

def main():
 
    points = read_points_from_file( FILENAME )
    start_time = time.time()
    # TODO - remove all files in output folder (can be in makefile)  
      
    k_means(N_KLUSTERS, points, N_THREADS )

    end_time = time.time()
    print("Execution time: %.3f" % (end_time - start_time))
    return


def read_points_from_file(filename):
    """
    Read information from file and create a Point for each entry.
    """
    path = "../input/" + filename
    f = open(path, 'r')
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


# set datafile sep ','
# set palette model RGB defined (0 "black",1 "blue", 2 "green",3 "red", 4 "yellow")
# plot 'iris.data' using 1:2:3 notitle with points pt 7 palette

# plot "./initial_points.txt" u 1:2:3 with points pt 7 ps 0.5 palette
# plot "./klustering_1.txt" u 1:2:3 with points pt 7 ps 0.5 palette