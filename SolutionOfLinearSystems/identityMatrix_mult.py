#npOpIdentity.py
# from numpy import array, dot
import numpy as np

A = np.array ( [ [0, 7, 4, 9], [3, 7, -9, 2], [0, 1, -4, 7], [6, 0, 4, 1] ] )
I = np.array ( [ [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1] ] )

result1 = np.dot ( A, I )
result2 = np.dot ( I, A )

print ( "\nResult of AI = \n", result1 )
print ( "\nResult of IA = \n", result2 )

#npOpInvIdentity.py

A = np.array ( [ [2, 3], [3, 5] ] )
B = np.array ( [ [5, -3], [-3, 2] ] )

result1 = np.dot ( A, B )
result2 = np.dot ( B, A )

print ( "\nResult of AB = \n", result1 )
print ( "\nResult of BA = \n", result2 )


