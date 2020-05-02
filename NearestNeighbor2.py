#NAME: Group 9 
#September 23 
#CPSC-51100, Fall 2018
#PROGRAMMING ASSIGNMENT #3

import numpy as np

def main():
    """ Main function """

    print("CPSC-51100, Fall 1, 2018")
    print("NAME: GROUP 9")
    print("PROGRAMMING ASSIGNMENT #3")
    print ""
    
          
    #import training and testing attributes from csv   
    trainingAttributes = np.genfromtxt(fname = 'iris-training-data.csv', dtype=float, delimiter=',', usecols=(0,1,2,3))
    testingAttributes = np.genfromtxt(fname = 'iris-testing-data.csv', dtype=float, delimiter=',', usecols=(0,1,2,3))
    
    #import classes from csv
    trainingClass = np.genfromtxt(fname = 'iris-training-data.csv', delimiter=",", dtype=("|S20"), usecols=(4))
    testingClass = np.genfromtxt(fname = 'iris-testing-data.csv', delimiter=",", dtype=("|S20"), usecols=(4))
    
    #ndarray of predicted classifications
    predictedClassification = classification(testingClass, testingAttributes, trainingAttributes)
    
    i = 1
    for true in predictedClassification:
        print i, " ", true
        i = i + 1
     
def classification(trainingClass, testingAttributes, trainingAttributes):
    """ Creates true classification on testingAttributes """

    #Variables used in classification
    returnClass = []
    smallest = 100000
    index = 0
    labelIndex = 0

    for test in testingAttributes:
        for train in trainingAttributes:
            dist = distance(test, train) 
            if dist < smallest:
                smallest = dist
                labelIndex = index
            index = index + 1
        returnClass.append(trainingClass[labelIndex])
        index = 0
        smallest = 100000
        labelIndex = 0
    return np.array(returnClass) #convert to numPy array

def distance(pointA, pointB, _norm=np.linalg.norm):
    """ Calculates the distance between testing and training attributes """
    return _norm(pointA - pointB)

def comparison(onedarray):
    #recall the 1D testing class array
    testingClass = np.genfromtxt(fname = 'iris-testing-data.csv', delimiter=",", dtype=("|S20"), usecols=(4))
    #count the number of matches
    n=np.sum(onedarray==testingClass)
    #count the number of testing examples
    p=np.size(testingClass)
    #compute and print the accuracy
    n=float(n)
    p=float(p)
    print"Accuracy: ", "%.2f" %  float(100*n/p), "%"
    return
        
comparison(np.array(returnClass))
if __name__ == "__main__":
    main()



