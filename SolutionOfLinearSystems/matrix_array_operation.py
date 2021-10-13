#npOp1.py
from numpy import array

A = array ( [ 1.0, 2.0, 3.0, 4.0 ] )
B = array ( [ 5.0, 6.0, 7.0, 8.0 ] )

print( "A = ", A )
print( "B = ", B )

C= A + B
print( "\n+ Result = ", C )

C= B - A
print( "\n- Result = ", C )

C= A * B
print( "\n* Result = ", C )

C= A / B
print( "\n/ Result = ", C )

C= A % B
print( "\n% Result = ", C )

C= A** B
print( "\n** Result = ", C )
