# File: clustering.py
# Author: Alejandro Cirugeda
# Description:
#   The k-means function will take a list of Class points and will execute the K-means algorthm in order to assign
#   a cluster to each point.s. The execution of the algorith is in parallel
#   spliting the number of points between differents threads in order to calculate the eucladian distance and the assigment 
#   of the different clusters. The output of every iteration is witten in a file for further annalisys

# TODO implement concurrency
import random
import math
import threading
from point import Point

def k_means(n_klustering, points):

    write_results("initial_points.txt", points)   # We wrote the values of the
    centroids = create_random_controids(n_klustering)

    chunks = split_points(points, 4)
  

    iteration = 0
    while True:
        points = assign_nearnest_centroid(points, centroids)   

        # We write values into the file
        filename = "klustering_" + str(iteration) + ".txt"
        write_results( filename, points)

        new_centroids = calculate_new_centroids(n_klustering, points)

        print("Old centroids: " + str(centroids[0]) + " - " + str(centroids[1]) + " - " + str(centroids[2]))
        print("New centroids: " + str(new_centroids[0]) + " - " + str(new_centroids[1]) + " - " + str(new_centroids[2]))

        if centroids == new_centroids: #if centroids didn't change we stop the algorithm
            break
        
        centroids = new_centroids
        iteration += 1

    print("K-means execute correctly")
    return



# funcion that return the eclaudian distance between 2 points
def eucladian_distance(x, y):
    """
    Returns the distance between two different points
    """
    distance =  ((x.x - y.x)**2) + (x.y - y.y)**2
    return distance



def create_random_controids(n_klustering):
    """
    Create a new point that will work as centroid of a cluster. Will start with a 
    random position.
    """
    # TODO check if at least one point is assig to each centroid
    centroids = [None] * n_klustering
    for i in range(0, n_klustering):
        
        # FIXME seed generator dont work
        # TODO implement dinamic random number generator with min and max 
        random_x = float("%.3f" % random.uniform(4, 9))
        random_y = float("%.3f" % random.uniform(2, 5))
        
        centroids[i] = Point(random_x, random_y, i)

    return centroids




def assign_nearnest_centroid(points, centroids):
    """
    Goes thought the list of points and assign each one to the centroid which in more near
    """
    for point in points:
        distances = []
        for centro in centroids:
            distances.append( eucladian_distance(point, centro))

        point.cluster = distances.index(min(distances)) + 1  #index start in 0 - cluster start in 1

    return points


def calculate_new_centroids(n_clusters, points):
    """
    This method obtain the avg position of all the points that are assig in the same cluster in 
    order to return a list of the new position of the centroids
    """
    counter       = [0] * n_clusters
    avgx          = [0] * n_clusters
    avgy          = [0] * n_clusters
    new_centroids = []


    # Sum of position in same clusters
    for point in points:
        index = point.cluster - 1
        counter[index] += 1

        avgx[index] += float("%.3f" % point.x)
        avgy[index] += float("%.3f" %point.y)

    print("Counters: ")
    print("    - Cluster1: " + str(counter[0]))
    print("    - Cluster2: " + str(counter[1]))
    print("    - Cluster3: " + str(counter[2]))

    # Calculate avg position and add it to list
    for i in range(n_clusters):
        avgx[i] = float("%.3f" % (avgx[i]/ counter[i]))
        avgy[i] = float("%.3f" % (avgy[i]/ counter[i]))
        new_centroids.append(Point(avgx[i], avgy[i]))
   
    return new_centroids



# We will write the results in the output folder
def write_results(filename, points):
    """
    Write the state of the point into a fille. Write x, y and kluster_id
    """
    path = "output/" + str(filename)
    f = open(path, 'w')
    for point in points:
        f.write("%.3f , %.3f , %d \n" % (point.x , point.y , point.cluster))

    f.close
    return

def split_points(points, n_chunks):
    """
    Split the list of points into similar size chunks. Return the list of chucka
    """
    if n_chunks < 2: return points
    
    avg = len(points) / float(n_chunks)
    out = []
    last = 0.0

    while last < len(points):
        out.append(points[int(last):int(last + avg)])
        last += avg

    return out



