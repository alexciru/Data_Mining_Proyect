# Case study of machine learning and datamining techniques



### Using the Breast Cancer datasets
```
Add photos
```

###### This project was done in the course of Introduction of artificial intelligence in the University Politechnika Warszawa.
![Alt text](http://www.mini.pw.edu.pl/~gagolews/mini_studia_II_stopnia_matematyka/logopw.png)
___

### Main task
The task of this project is to make a case study of the different classifiers, In order to do that we will using a Breast Cancer Dataset.

## Description of the dataset

 This [Breast Cancer Database](https://archive.ics.uci.edu/ml/datasets/breast+cancer+wisconsin+%28original%29). Features were computed from a digitized image of a breast mass. They describe characteristics of the cell nuclei present in the image. This dataset is formed by 10 attributes and each instance has one of possible classes: **benign** or **malignant**.

attribute | value
:------------ | -------------
Sample code number| id number
Clump Thickness| 1 - 10
Uniformity of Cell Size| 1 - 10
Uniformity of Cell Shape| 1 - 10
Marginal Adhesion| 1 - 10
Single Epithelial Cell Size| 1 - 10
Bare Nuclei| 1 - 10
Bland Chromatin| 1 - 10
Normal Nucleoli| 1 - 10
Mitoses| 1 - 10
Class| B or M

In this dataset we have this class distribution:

+ **Benign**:    458  65.5%
+ **Malignant**: 241  34.5%




### training set and test set


Splitting the data is one of the most important steps and concepts in Machine Learning. we need to split the dataset into training set and testing set.
+ **TRAINING SET:** used to build and train the model.
+ **TESTING SET:** this is the data used to check the model previously created from the training set. We will generate ROC curse to measure the performance of the different classifiers.

For this case study we will separate the data into 75% training set and 25% testing set. Also we need to make sure that both sets contains data that belong to both class.

### conclusion
Model | Accuracy
------------ | -------------
ctrees | 96,28
rpart trees | 96,27
random Forest| 94,68
SVM | 96,28
Bayer| 92,02

```
Add photos
```
