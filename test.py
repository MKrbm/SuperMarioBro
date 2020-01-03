import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

class area:
	def __init__(self,r):
		self.r = r

	def area(self):
		return np.pi**2*self.r
