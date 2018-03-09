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
runitem = MCMCWrapper(emcee, 'm,c', 'x', '{"m":{"priortype":"Uniform","minval":"-10","maxval":"10","meanval":0,"sigmaval":0},"c":{"priortype":"Uniform","minval":"-10","maxval":"10","meanval":0,"sigmaval":0}}', 1000, 1000, 100, 2, 'fanatapan@yahoo.co.uk', 'e36ff5c44a9e2b4c519aa20eca5b7cc1', 'm*x+c', 'x, 0.65,')
runitem.run_mcmc()
runitem.run_postproc()

