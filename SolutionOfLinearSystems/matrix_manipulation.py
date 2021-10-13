#npOpArrayNp.py
from numpy import array

A = array ( [ 1.0, 2.0, 3.0, 4.0 ] )
B = array ( [ 5.0, 6.0, 7.0, 8.0 ] )

print ( "A = ", A )
print ( "B = ", B )

C = A + 1
print ( "\n+ Result = ", C )

C = A - 1
print ( "\n- Result = ", C )

C = A * 2
print ( "\n* Result = ", C )

C = A / 2
print ( "\n/ Result = ", C )

C = A % 4
print ( "\nModulus Result = ", C )

C = A ** 2
print ( "\nSquare Result = ", C )

C = 2 ** A
print ( "\nBase 2 Result = ", C )
