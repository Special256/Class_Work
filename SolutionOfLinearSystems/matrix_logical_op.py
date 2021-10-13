#npOpLogic.py
#from numpy import array
import numpy as np

A = np.array ( [ 1.0, 2.0, 3.0, 4.0 ] )
B = np.array ( [ 5.0, 2.0, 3.0, 8.0 ] )

print( "A = ", A )
print( "B = ", B )

C = np.equal ( A, B )
print( "\n A==B Result = ", C )

C = np.not_equal ( A, B )
print( "\n A!=B Result = ", C )

C = np.greater ( A, B )
print( "\n A>B Result = ", C )

C = np.greater_equal ( A, B )
print( "\n A>=B Result = ", C )

C = np.less ( A, B )
print( "\n A<B Result = ", C )

C = np.less_equal ( A, B )
print( "\n A<=B Result = ", C )

C = np.array_equal ( A, B )
print( "\n Array comparison Result = ", C )
