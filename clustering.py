# File: clustering.py
# Author: Alejandro Cirugeda
# Description:
# In this file we will implement the K-means algorithm

# TODO implement concurrency
import random
import math
import threading
from point import Point

def k_means(n_klustering, points):

    write_results("initial_points", points)   # We wrote the values of the

    # create random centroids
    centroids = create_random_controids(n_klustering)
    
    iteration = 0
    # We start the algorithm
    while True:
        
        # Assign the points to the nearnest centroid
        points = assign_nearnest_centroid(points, centroids)   

        # We write values into the file
        filename = "klustering_" + str(iteration) + ".txt"
        write_results( filename, points)
        iteration += 1


        counter       = [0] * n_klustering
        avgx          = [0] * n_klustering
        avgy          = [0] * n_klustering
        new_centroids = []


        # Calculate new Centroids (sum everything and divided by number of points)
        for point in points:
            index = point.cluster - 1
            counter[index] += 1

            avgx[index] += float("%.3f" % point.x)
            avgy[index] += float("%.3f" %point.y)
    

        print("Results: ")
        print("Counters: ")
        print("    - Cluster1: " + str(counter[0]))
        print("    - Cluster2: " + str(counter[1]))
        print("    - Cluster3: " + str(counter[2]))
       
        # TODO sometimes error dividing by zero
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

        if centroids == new_centroids: #if centroids didn't change we stop the algorithm
            break
        
        centroids = new_centroids

    return



# funcion that return the eclaudian distance between 2 points
def eucladian_distance(x, y):
    distance =  ((x.x - y.x)**2) + (x.y - y.y)**2
    return distance

#TODO make the program with more functions

def create_random_controids(n_klustering):
    centroids = [None] * n_klustering
    for i in range(0, n_klustering):
        
        # TODO implement seed
        # TODO implement dinamic random number generator with min and max 
        random_x = float("%.3f" % random.uniform(4, 9))
        random_y = float("%.3f" % random.uniform(2, 5))
        
        centroids[i] = Point(random_x, random_y, i)

    return centroids




def assign_nearnest_centroid(points, centroids):
    # assign each point to the nearnest centroids
    for point in points:
        distances = []
        for centro in centroids:
            distances.append( eucladian_distance(point, centro))

        point.cluster = distances.index(min(distances)) + 1  #index start in 0 - cluster start in 1

    return points



def calculate_new_centroids(points, centroids):
    return



# We will write the results in the output folder
def write_results(filename, points):
    path = "output/" + str(filename)
    f = open(path, 'w')
    for point in points:
        f.write("%.3f , %.3f , %d \n" % (point.x , point.y , point.cluster))

    f.close
    return
