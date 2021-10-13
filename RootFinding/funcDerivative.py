# funcDerivative.py
import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return x**3 - 2*x**2 - 11*x +12 # function

def dfdx(x):
	return 3*x**2 -4*x -11 		# derivative

# initialize data
x = np.linspace ( -4, 6, 100 )
y = f(x)
ydf = dfdx ( x )
p = np.roots ( [ 1,-2,-11, 12 ] )

# plotting the function and its derivative
fig = plt.figure()
plt.xlabel( 'x' )
plt.axhline( 0 ) 			# horizontal
plt.axvline( p[ 0 ] )			# vertical
plt.axvline( p[ 1 ] )
plt.axvline( p[ 2 ] )
plt.plot( x, y, '-b', label= 'f(x)' )
plt.plot( x, ydf, '--r', label='df(x)/dx' )
plt.legend()
plt.show()
