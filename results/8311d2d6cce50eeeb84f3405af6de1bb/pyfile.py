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
runitem = MCMCWrapper(try:
  mini = -1 + np.random.rand(Nens)*2
  cini = -10 + np.random.rand(Nens)*20
  pos = np.array([mini, cini]).T
except:
  errval = PRIOR_INIT_ERR
, emcee, m,c, x, , sigma_gauss, [object Object], 1000, 1000, 100, 2, {errval}, fanatapan@yahoo.co.uk, 8311d2d6cce50eeeb84f3405af6de1bb, {modelStrings},   argslist = (x, 0.65, data)
)
runitem.run_mcmc()
runitem.run_postproc()

