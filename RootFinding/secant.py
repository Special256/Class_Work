import numpy as np
import matplotlib.pyplot as plt

def SecantMethod( func, x0, x1, epsilon, nMax = 100 ):
	#initialization
	i = 0
	x2 = 0
	iterX, iterY, iterCount = np.empty(0), np.empty(0), np.empty(0)
	error = 100

	x2 = x1 - func(x1) * ( (x1 - x0) / ( func(x1) - func(x0) ) )

	while np.abs(error) > epsilon and i < nMax:
		i+ = 1
		iterX = np.append ( iterX, x2 )
		iterY = np.append ( iterY, funct(x2) )
		iterCount = np.append ( iterCount, i )

		x2 = x1 - func(x1) * ( (x1 - x0) / (func(x1) - func(x0) ) )
		error = x2 - x1
		x0 = x1
		x1 = x2

	return x2, iterX, iterY, iterCount

#======================================= plot Secant Method
root, iterX, iterY, iterCount = SecantMethod( f, -5, -2, 0.01 )
fig, ax = plt.subplots()
ax.set_xlabel('x')
ax.axhline(0)
ax.plot(x, y)
ax.scatter(	x	= iterX, y	= iterY )
ax.set_title(	'Secant Method: {} iterations'.format(	len(iterCount)	)	)

for i, txt in enumerate(iterCount):
	ax.annotate(	txt, (	iterX[i], iterY[i]	)	)

plt.show()
