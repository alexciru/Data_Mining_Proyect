# File: point.py
# Author: Alejandro Cirugeda
# Description:
#   The class Point will storage the information about the different transactions from the file read
#


class Point:

    __init__(self, x, y):
        self.x = x  
        self.y = y

        self.cluster = 0 #cluster associated with the point
        return

    print(self):
        print("(%d, %d) ", self.x , self.y)
        return