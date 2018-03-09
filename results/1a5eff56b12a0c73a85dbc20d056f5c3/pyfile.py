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
runitem = MCMCWrapper(emcee, {theta}, x, , sigma_gauss, '{"m":{"priortype":"LogUniform","minval":"1","maxval":"2","meanval":0,"sigmaval":0},"c":{"priortype":"Uniform","minval":"-10","maxval":"10","meanval":0,"sigmaval":0}}', 1000, 1000, 100, 2, {errval}, fanatapan@yahoo.co.uk, 1a5eff56b12a0c73a85dbc20d056f5c3, {modelStrings}, 'x, 0.65,')
runitem.run_mcmc()
runitem.run_postproc()

