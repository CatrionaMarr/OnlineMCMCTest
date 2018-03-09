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
runitem = MCMCWrapper('emcee', 'm,c', 'x', '{"m":{"priortype":"Uniform","minval":"-10","maxval":"10","meanval":0,"sigmaval":0},"c":{"priortype":"Uniform","minval":"-1","maxval":"1","meanval":0,"sigmaval":0}}', 1000, 1000, 100, 2, 'fanatapan@yahoo.co.uk', 'a8a9b7e06e288ac7e24d565974b8f3f1', 'm*x+c', 'x, 0.65,')
runitem.run_mcmc()
runitem.run_postproc()

