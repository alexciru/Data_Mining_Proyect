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
    

    
    # We repeat the loop until the 
    while True:

    # assign each point to the nearnest centroids
        for point in points:
            distances = []
            for centro in centroids:
                distances.append( eucladian_distance(point, centro))

            point.cluster = distances.index(min(distances)) + 1  #index start in 0 - cluster start in 1
        

        counter       = [0] * n_klustering
        avgx          = [0] * n_klustering
        avgy          = [0] * n_klustering
        new_centroids = []


        for point in points:

            # Calculate new Centroids (sum everything and divided by number of points)
            index = point.cluster - 1
            counter[index] += 1

            avgx[index] += float("%.3f" % point.x)
            avgy[index] += float("%.3f" %point.y)
            #TODO test if work



        print("Results: ")
        print("Counters: ")
        print("    - Cluster1: " + str(counter[0]))
        print("    - Cluster2: " + str(counter[1]))
        print("    - Cluster3: " + str(counter[2]))
       
        
        avgx[0] = float("%.3f" % (avgx[0]/ counter[0]))
        avgy[0] = float("%.3f" % (avgy[0]/ counter[0]))
        avgx[1] = float("%.3f" % (avgx[1]/ counter[1]))
        avgy[1] = float("%.3f" % (avgy[1]/ counter[1]))
        avgx[2] = float("%.3f" % (avgx[2]/ counter[2]))
        avgy[2] = float("%.3f" % (avgy[2]/ counter[2]))
        
    
        new_centroids.append(Point(avgx[0], avgy[0]))
        new_centroids.append(Point(avgx[1], avgy[1]))
        new_centroids.append(Point(avgx[2], avgy[2]))

        print("Old centroids: " + str(centroids[0]) + " - " + str(centroids[1]) + " - " + str(centroids[2]))
        print("New centroids: " + str(new_centroids[0]) + " - " + str(new_centroids[1]) + " - " + str(new_centroids[2]))

        if centroids == new_centroids:
            break
        
        centroids = new_centroids
    
    return



# funcion that return the eclaudian distance between 2 points
def eucladian_distance(x, y):
    distance =  ((x.x - y.x)**2) + (x.y - y.y)**2
    return distance

#TODO make the program with more functions

def create_random_controids(centroids):
    return

def assign_nearnest_centroid(points, centroids):
    return

def calculate_new_centroids(points, centroids):
    return