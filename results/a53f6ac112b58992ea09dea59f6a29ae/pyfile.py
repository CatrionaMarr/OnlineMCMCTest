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
runitem = MCMCWrapper({fitarraystring}, emcee, m,c, x, , sigma_gauss, [object Object], 1000, 1000, 100, 2, {errval}, fanatapan@yahoo.co.uk, a53f6ac112b58992ea09dea59f6a29ae, {modelStrings},   argslist = (x, 0.65, data)
)
runitem.run_mcmc()
runitem.run_postproc()

