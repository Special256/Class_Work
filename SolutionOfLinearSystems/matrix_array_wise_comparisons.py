#npOpLogicArrayWise.py
#from numpy import array
import numpy as np

A = np.array ( [ 1.0, 2.0, 3.0, 4.0 ] )
B = np.array ( [ 5.0, 2.0, 3.0, 8.0 ] )

print ( "A = ", A )
print ( "B = ", B )

C = A.copy()
print ( "\nC = ", C )

D = np.array_equal ( A, C )
print ( "\nResult = ", D )
