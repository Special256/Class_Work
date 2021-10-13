import numpy as np
import matplotlib.pyplot as plt

def BisectionSearch(func, a, b, epsilon, nMax= 1000):
	# initialization variable, iterX, iterX are used to plot results
	i=0
	iterX, iterY, iterCount= np.empty(0), np.empty(0), np.empty(0)
	
	# Looping condition to ensure that loop is not infinite
	while i< nMax:
		i = i+1
		c = (a + b)/2.0 								# c= a + (b-a)/2
		iterX = np.append(iterX, c)
		iterY = np.append(iterY, func(c))

		iterCount = np.append(iterCount, i)
		if np.abs(func(c)) < epsilon:
			return c, iterX, iterY, iterCount
		elif np.sign(func(c)) == np.sign(func(a)):
			a = c
		elif np.sign(func(c)) == np.sign(func(b)):
			b = c

# def BisectionSearch(func, a, b, epsilon, nMax= 1000):
root, iterX, iterY, iterCount= BisectionSearch(f, -5, -2, 0.01) # call function
fig, ax= plt.subplots()
ax.set_xlabel('x')
ax.axhline(0)
ax.plot(x, y)
ax.scatter( x = iterX, y = iterY )
ax.set_title( 'Bisection Method: {} iterations'.format( len(iterCount) ) )

# Loop to add text annotations to the iteration points
for i, txt in enumerate(iterCount):
	ax.annotate( txt, ( iterX[i], iterY[i] ) )
plt.show()
