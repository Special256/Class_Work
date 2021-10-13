#npOpLogicOperators.py
#from numpy import array
import numpy as np 

a= np.array ( [ 1, 1, 0, 0 ], dtype = bool )

b= np.array ( [ 1, 0, 1, 0 ], dtype = bool )

print ( "a = ", a )
print ( "b = ", b )

c= np.logical_and ( a, b )
print ( "\nAND Result = ", c )

c= np.logical_or ( a, b )
print ( "\nOR Result = ", c )

c= np.logical_xor ( a, b )
print ( "\nXOR Result = ", c )
