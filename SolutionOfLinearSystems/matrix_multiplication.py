#npOpArray.py
import numpy as np
from numpy import array, dot
from numpy.linalg import inv, solve

A = array ( [ [1, 2, 3], [4, 5, 6] ] )
B = array ( [ [1,2], [3, 4], [5,6] ] )

result1 = dot ( A, B )
result2 = dot ( B, A )

print ( "\nResult of AB = \n", result1 )
print ( "\nResult of BA = \n", result2 )

#using np.dot

result1 = np.dot ( A, B )
result2 = np.dot ( B, A )
print ( "\nResult of AB = \n", result1 )
print ( "\nResult of BA = \n", result2 )

#dotMultiplication1.py

a= np.array ( [ [1, 2, 3], [4, 5, 6] ] )
b= np.array ( [ [1, 2], [3, 4], [5, 6] ] )

result1 = np.dot ( a, b )
result2 = np.dot ( b, a )

print ( '\nresult {0}{1}= \n{2}'.format ( 'a', 'b', result1 ) )
print ( '\nresult {0}{1}= \n{2}'.format ( 'b', 'a', result2 ) )


