#these are the imports for python to give us access numpy and plotting libraries
import numpy as np
import numpy.linalg as la
import math

# this is the driver functiont that runs the code to be seen in terminal
def driver():
    n = 3
    # linspace creates an array to give a set of numbers for us to work with
    x = np.linspace(0,np.pi,n)
    # this is a function handle. You can use it to define
    # functions instead of using a subroutine like you
    # have to in a true low level language.
    f = lambda x: x**2 + 4*x + 2*np.exp(x)
    g = lambda x: 6*x**3 + 2*np.sin(x)
    y = [1,0,1]
    w = [0,1,0]
    # evaluate the dot product of y and w
    dp = dotProduct(y,w,n)
    # print the output
    print('the dot product is : ', dp)
    return
def dotProduct(x,y,n):
# Computes the dot product of the n x 1 vectors x and y
    dp = 0.
    # for loop that adds up the computations of the vector elements
    for j in range(n):
        dp = dp + x[j]*y[j]
    return dp
# incomplete function that uses the dot product to multiply matrices
def matrixMult(x,y,n):
    new_matrix = 0
    return new_matrix
driver()