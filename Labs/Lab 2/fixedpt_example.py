# import libraries
import numpy as np
    
def driver():

     
     f1 = lambda x:  (10 / (x + 4)) ** (1/2)
# fixed point is alpha1 = 1.4987....

     f2 = lambda x:  x - (x ** 5 - 7) / (5 * x ** 4)
#fixed point is alpha2 = 3.09... 

     Nmax = 100
     tol = 1e-10
     p = 1.3652300134140976

# test f1 '''
     x0 = 1.5
     [xstar,ier, x_arr] = fixedpt(f1,x0,tol,Nmax)
     convergence(x_arr, p)
     print('the approximate fixed point is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)
    
# #test f2 '''
#      x0 = 1
#      [xstar,ier, x_arr] = fixedpt(f2,x0,tol,Nmax)
#      convergence(x_arr, p)
#      print('the approximate fixed point is:',xstar)
#      print('f2(xstar):',f2(xstar))
#      print('Error message reads:',ier)



# define routines
def fixedpt(f,x0,tol,Nmax):
    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''
    ''' x = vector for approximation'''
    x = np.zeros((Nmax, 1))
    count = 0
    x[count] = x0
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       x[count] = x1
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier, x]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier, x]
    
def convergence(x, p):
     residuals = np.abs(x - p)

# Compute ratios
     ratios = residuals[1:] / residuals[:-1]

     # Estimate the order of convergence
     order_of_convergence = np.log(ratios[1:]) / np.log(ratios[:-1])

     # Print results
     print("Order of Convergence:", order_of_convergence)
     return

def aitken_squared(x):
     x_a = []
     for i in range(len(x)):
          x_a.append((x[i] - (x[i+1] - x[i]) ** 2) / (x[i+2] - 2*x[i+1] + x[i]))
     return x_a

driver()