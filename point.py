# File: point.py
# Author: Alejandro Cirugeda
# Description:
#   The class Point will storage the information about the different transactions from the file read
#

class Point:
    def __init__(self, x, y, identifier = -1):
        self.x = x  
        self.y = y
        self.cluster = -1 #cluster associated with the point
        self.id = identifier
        return



    def print(self):
        string = "(" + str(self.x) + ", " +  str(self.y) + ")"
        if(self.cluster != -1):
            string += string + " cluster =" + str(self.cluster)
        
        print(string)
        return