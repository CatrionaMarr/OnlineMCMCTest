# import functions that can be used by the model
from numpy import pi, sin, cos, tan, exp, log, log10, log2, arccos, arcsin, arctan, arctan2, sinh, cosh, tanh, arccosh, arcsinh, arctanh
from scipy.special import erf, gamma
from scipy.misc import factorial

# define the model to fit to the data
def mymodel(m,c, x):
  
  
  return m*x+c

