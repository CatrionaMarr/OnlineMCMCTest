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
three = '{"m":{"priortype":"LogUniform","minval":"1","maxval":"100","meanval":0,"sigmaval":0},"c":{"priortype":"Uniform","minval":"-2","maxval":"2","meanval":0,"sigmaval":0}}'
runitem = MCMCWrapper({fitarraystring}, emcee, m,c, x, , sigma_gauss, [object Object], 1000, 1000, 100, 2, {errval}, fanatapan@yahoo.co.uk, f1faa15224db3dee19dddbb27d8cbd52, {modelStrings},   argslist = (x, 0.65, data)
)
runitem.run_mcmc()
runitem.run_postproc()

