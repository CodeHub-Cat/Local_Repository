import numpy as np
import matplotlib.pyplot as plt 
def f(x): 
    return np.sin(x)
x_values=np.linspace(-2*np.pi,2*np.pi,1000)
y_values=f(x_values)
plt.plot(x_values,y_values,label='graph of sin(x)')
plt.grid()
plt.legend()
plt.show() 
