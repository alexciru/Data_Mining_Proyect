# Implementation of K-means Algorithm with application of parallel execution

```
Add k-means Gif
```

###### This project was done in the course of Data Mining in the University Politechnika Warszawa.
![Alt text](http://www.mini.pw.edu.pl/~gagolews/mini_studia_II_stopnia_matematyka/logopw.png)
___


### Main task
The objective of this project it’s to implement the clustering algorithm: K-means. This algorithm is used in data mining for finding patterns in the dataset. The objective of this project is to present a design and implementation of the algorithm with parallel implementation in python.

### Algorithm
The K-means algorithm is a simple algorithm that works as follows:
1.	We generate one centroid random point for each cluster we want to classify.
2.	We assign each point to the nearest centroid. For this project we will use the Euclidean distance.
3.	Calculate the new position of the Centroid with the average position of the points assig to that centroid
4.	With the new position of the centroid we assign the nearest point and repeat the process until the position of the centroid not vary

### input and output
This project will receive the input for a .txt file. In this file we will read the x and y position.
Once we have the output in the file, we will use Gnuplot, an open source plotting tool, in order to plot the results in a graphic and make a further analysis.

### Experiments
In order test the efficiency of the algorithm we have 3 different experiments with different datasets:
+ Iris Data (around 130 entries)
+ artificial database (8000 entries)
+ Household power consumption database (2 million entries)

1. Iris datasets
The objective of this experiment is to test if the k-means algorithm work properly with small numbers of entries. With this database there is have been a lot of experiments for classification and we can check if we obtain good results.  The iris database is formed with 150 instances of flower belonging to 3 different classes.
This was one of the first experiments and was mainly used to check the algorith while was writing.

![Alt text](https://media.giphy.com/media/XIqCQx02E1U9W/giphy.gif)


2. artificial dataset
This dataset is formed of 8000 instances and was created by a tool called: MlDemos, a tool used for education and learning of IA techniques
The main objective is to see how the algorithm behave with some notorious number of instances with some clear cluster in order to check both the assignment of the clusters and the execution time.

![Alt text](https://media.giphy.com/media/13HgwGsXF0aiGY/giphy.gif)

3. power consumption dataset
This dataset has 2075259 instances and the point of the experiment is to take the implementation to the limit and, specially, to study how the algorithm performs with such high numbers.
The household power consumption has information about the electric measurements in a house between 2007 and 2010. In order to use this dataset, it needed to be cleaned, removing the empty instances. This dataset is not mean to be used for clustering, therefore we will not be able to take conclusion about the dataset.

![Alt text](http://giphygifs.s3.amazonaws.com/media/MIY4jpusckRmU/giphy.gif)

### Issue with the project
One issue that is worth mentioning is the problem with the selection of the random centroids, for this test we used a seed in order to prevent any problems. The issue comes when one random centroid is situated in a position where no points are assigning to it. In order to fix we select another random point and hope it selected a better position. This case is very rare but, in this case, select another random position worked.

Another problem was the stop criteria, in the first version the stop criteria was once the centroids didn’t change between iterations but with higher databases could never stop because it enters a loop of position where a centroid oscillated between to values. It was once tried to be fixed it, adding a marginal error for the position of centroids. But at the end the best option was to add a limited number of the algorithm just in case the execution of the algorithm prolongates too much.
