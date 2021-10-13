import numpy as np
import matplotlib.pyplot as plt

def NewtonRaphson(func, deriv, x, epsilon, nMax= 100):
	# initialization variable, iterX, iterX are used to plot results
	i=0
	iterX, iterY, iterCount= np.empty(0), np.empty(0), np.empty(0)

	error= x- (x- func(x)/deriv(x))

	# Looping as long as error is greater than epsilon
	while np.abs(error) > epsilon and i < nMax:
		i += 1
		iterX= np.append(iterX, x)
		iterY= np.append(iterY, func(x))
		iterCount= np.append(iterCount, i)
		
		error = x- (x- func(x)/deriv(x))
		x= x - func(x)/deriv(x)
	
	return x, iterX, iterY, iterCount


#======================================= Netwon Raphson method
root, iterX, iterY, iterCount= NewtonRaphson(f, dfdx, -2, 0.01)
fig, ax= plt.subplots()
ax.set_xlabel('x')
ax.axhline(0)
ax.plot(x, y)
ax.scatter(x= iterX, y= iterY)
ax.set_title('Newton Raphson Method: {} iterations'.format(len(iterCount)))

# plotting the function and its derivative
for i, txt in enumerate(iterCount):
	ax.annotate(txt, (iterX[i], iterY[i]))

plt.show()
