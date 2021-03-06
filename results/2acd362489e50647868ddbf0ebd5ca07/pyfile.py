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
three = "[object Object]"
runitem = MCMCWrapper({fitarraystring}, emcee, m,C, x, , sigma_gauss, [object Object], 1000, 1000, 100, 2, {errval}, fanatapan@yahoo.co.uk, 2acd362489e50647868ddbf0ebd5ca07, {modelStrings},   argslist = (x, 0.65, data)
)
runitem.run_mcmc()
runitem.run_postproc()

