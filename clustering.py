# File: clustering.py
# Author: Alejandro Cirugeda
# Description:
# In this file we will implement the K-means algorithm

# TODO implement concurrency
import random
import math
from point import Point

def k_means(n_klustering, points):

    # create random centroids
    centroids = [None] * n_klustering
    for i in range(0, n_klustering):
        # TODO implement seed

        # TODO implement dinamic random number generator
        random_x = float("%.3f" % random.uniform(4, 9))
        random_y = float("%.3f" % random.uniform(2, 5))
        
        centroids[i] = Point(random_x, random_y, i)
    

    # assign each point to the nearnest centroids
    for point in points:
        distances = []
        for centro in centroids:
            distances.append( eucladian_distance(point, centro))

        point.cluster = distances.index(min(distances)) + 1  #index start in 0 - cluster start in 1
        
    #loop until centroids dont change
    # TODO change to until centroid are the same
    counter = [0] * n_klustering
    avgx      = [0] * n_klustering
    avgy      = [0] * n_klustering

    # while centroids not change

    for point in points:

        # Calculate new Centroids (sum everything and divided by number of points)
        index = point.cluster - 1
        counter[index] += 1

        avgx[index] += point.x
        avgy[index] += point.y
        #TODO test if work

    print("Results: ")
    print("Counters: ")
    print("    - Cluster1: " + str(counter[0]))
    print("    - Cluster2: " + str(counter[1]))
    print("    - Cluster3: " + str(counter[2]))
    print("Old centroids: " + str(centroids[0]) + " - " + str(centroids[1]) + " - " + str(centroids[2]))
    
    avgx[0] = avgx[0]/ counter[0]
    avgy[0] = avgy[0]/ counter[0]
    avgx[1] = avgx[1]/ counter[1]
    avgy[1] = avgy[1]/ counter[1]
    avgx[2] = avgx[2]/ counter[2]
    avgy[2] = avgy[2]/ counter[2]
    
    
    print("New centroids: " + str(avgx[0]) + "," + str(avgy[0]))
    print("New centroids: " + str(avgx[1]) + "," + str(avgy[1]))
    print("New centroids: " + str(avgx[2]) + "," + str(avgy[2]))
    return



# funcion that return the eclaudian distance between 2 points
def eucladian_distance(x, y):
    distance =  ((x.x - y.x)**2) + (x.y - y.y)**2
    return distance