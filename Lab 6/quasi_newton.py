import numpy as np
import math
import time
from numpy.linalg import inv 
from numpy.linalg import norm 

# Class code
def evalF(x): 

    F = np.zeros(2)
    
    F[0] = 4 * x[0] ** 2 + x[1] ** 2 - 4
    F[1] = x[0] + x[1] - np.sin(x[0] - x[1])
    
    return F


def evalJ(x): 

    
    # J = np.array([[8 * x[0], 2 * x[1]],
    #              [1 - np.cos(x[0] - x[1]), 1 + np.cos(x[0] - x[1])]])
    J = np.array([[8 * x[0], 2 * x[1]],
                  [1 - np.cos(x[0] - x[1]), 1 + np.cos(x[0] - x[1])]])
    return J


# slacker newton
def slacker_newton(x0, tol, Nmax, update_iter):
    
    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    for its in range(Nmax):
        
        if its % update_iter == 0:
            J = evalJ(x0)
            Jinv = inv(J)
        
        F = evalF(x0)

        x1 = x0 - Jinv.dot(F)

        if (norm(x1-x0) < tol):
            xstar = x1
            ier =0
            return[xstar, ier, its]
            
        x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its]


# running code

x0 = np.array([1, 0])

Nmax = 100
tol = 1e-10
update_iter = 3

for j in range(20):
    [xstar,ier,its] =  slacker_newton(x0,tol,Nmax, update_iter)

print(xstar)
print('Newton: the error message reads:',ier)
print('Netwon: number of iterations is:',its)