# import libraries
import numpy as np

def driver():

# use routines    
# Exercise (1): f(x) = (x ** 2) * (x - 1)
  # interval (a = 0.5, b = 2) is a valid interval, with root at 0.9999999701976776
  # interval (a = -1, b = 0.5) returns an error because f(a) and f(b) are both negative
  # interal (a = -1, b = 2) is a valid interval, with root also at 0.9999999701976776
  
#Exercise (2): 
  # f(x) = (x - 1) * (x - 3) * (x - 5), (a = 0, b = 2.4) returns root at 0.999999976158142
  # f(x) = (x - 1) ** 2 * (x - 3), (a = 0, b = 2) returns an error because f(a) and f(b) have same sign
  # f(x) = sin(x), (a = 0, b = 0.1) returns exact root at 0 because f(a) is one of the roots
  # f(x) = sin(x), (a = 0.5, b = 3pi/4) returns an error because f(a) and f(b) have same sign
  # this seems like what we expect, as it gets very close to all the roots we want, and gave us the proper errors as well
    f = lambda x: np.sin(x)
    a = 0.5
    b = 3 * np.pi / 4

#    f = lambda x: np.sin(x)
#    a = 0.1
#    b = np.pi+0.1

    tol = 1e-7

    [astar,ier] = bisection(f,a,b,tol)
    print('the approximate root is',astar)
    print('the error message reads:',ier)
    print('f(astar) =', f(astar))




# define routines
def bisection(f,a,b,tol):
    
#    Inputs:
#     f,a,b       - function and endpoints of initial interval
#      tol  - bisection stops when interval length < tol

#    Returns:
#      astar - approximation of root
#      ier   - error message
#            - ier = 1 => Failed
#            - ier = 0 == success

#     first verify there is a root we can find in the interval 

    fa = f(a)
    fb = f(b);
    print(f"a point : {fa}, b point : {fb}")
    if (fa*fb > 0):
       ier = 1
       astar = a
       return [astar, ier]

#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier]

    count = 0
    d = 0.5*(a+b)
    while (abs(d-a)> tol):
      fd = f(d)
      if (fd ==0):
        astar = d
        ier = 0
        return [astar, ier]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1
#      print('abs(d-a) = ', abs(d-a))
      
    astar = d
    ier = 0
    return [astar, ier]
      
driver()               

