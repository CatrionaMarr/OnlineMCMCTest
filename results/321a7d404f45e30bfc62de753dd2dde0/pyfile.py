#!/usr/bin/env python

# import required packages
import emcee
import numpy as np
from numpy import exp, log

# import model function from separate file
from mymodel import mymodel

# import post-processing function from theonlinemcmc package
from theonlinemcmc import *

#import the wrapper class
from theonlinemcmc import MCMCWrapper

#run the mcmc
runitem = MCMCWrapper(emcee, m,c,d, x, , sigma_gauss, [object Object], 1000, 1000, 100, 3, {errval}, fanatapan@yahoo.co.uk, 321a7d404f45e30bfc62de753dd2dde0, {modelStrings},   argslist = (x, 0.65, data)
)
runitem.run_mcmc()
runitem.run_postproc()

