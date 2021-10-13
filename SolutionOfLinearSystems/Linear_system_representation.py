#npSolver.py
from numpy import *
import numpy as np

#A= np.array([[10, 0, 40], [0, 20, 40], [10, -20, 0]])
A = np.array ( [ [10, 0, 40], [0, 20, 40], [1, 1, -1] ] )
B = np.array ( [ 10, 20, 0] )

print ( "A matrix = ", A )
print ( "B matrix = ", B )

A_det = np.linalg.det( A )
A_inv = np.linalg.inv( A )

print ( "\nA determinent =", A_det )
print ( "A inverse= ", A_inv )

S = np.linalg.solve ( A, B )
print( "\nSolution = ", S )
