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
        # TODO implement dinamic random number generator
        # TODO implement seed
        random_x = random.uniform(4, 9)
        random_y = random.uniform(2, 5)
        
        centroids[i] = Point(random_x, random_y, i)
    

    # assign each point to the nearnest centroids
    for point in points:
        distances = []
        for centro in centroids:
            distances.append( eucladian_distance(point, centro))

        point.cluster = distances.index(min(distances)) + 1  #index start in 0 - cluster start in 1
        
    #loop until centroids dont change
    # TODO change to until centroid are the same
    # while centroids not change
    for point in points:

        # Calculate new Centroids (sum everything and divided by number of points )
        counter = [0] * n_klustering
        avg      = [] * n_klustering

        index = point.id - 1
        counter[index] += 1

        avg[index][0] += point.x
        avg[index][1] += point.y
        #TODO test if work

    print("Results: ")
    print("Counters: ")
    print("    - Cluster1: " + counter[0])
    print("    - Cluster2: " + counter[1])
    print("    - Cluster3: " + counter[2])
    print("Old centroids: " + str(centroids[0]) + " - " + str(centroids[1]) + " - " + str(centroids[2]))
    
    avg[0] = avg[0]/ counter[0]
    avg[1] = avg[1]/ counter[1]
    avg[2] = avg[2]/ counter[2]
    print("New centroids: " + str(avg[0]) + " - " + str(avg[1]) + " - " + str(avg[2]))
    return



# funcion that return the eclaudian distance between 2 points
def eucladian_distance(x, y):
    distance =  ((x.x - y.x)**2) + (x.y - y.y)**2
    return distance