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
runitem = MCMCWrapper(emcee, 'm,c', 'x', '{"m":{"priortype":"Uniform","minval":"-1","maxval":"1","meanval":0,"sigmaval":0},"c":{"priortype":"Uniform","minval":"-10","maxval":"10","meanval":0,"sigmaval":0}}', 1000, 1000, 100, 2, 'fanatapan@yahoo.co.uk', '3e667ca4312513c833a6c0e8c8231c2c', 'm*x+c', 'x, 0.65,')
runitem.run_mcmc()
runitem.run_postproc()

