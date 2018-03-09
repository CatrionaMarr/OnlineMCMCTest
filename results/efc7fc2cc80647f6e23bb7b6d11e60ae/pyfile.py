#!/usr/bin/env python

# import required packages
import emcee
import numpy as np
from numpy import exp, log

# import model function from separate file
from mymodel import mymodel

# import post-processing function from theonlinemcmc package
from theonlinemcmc import *

#run the mcmc
runitem = MCMCWrapper({sampler_type}, {theta}, {abscissastring}, {gauss_like_sigma}, {fitarray}, {Nmcmc}, {Nburnin}, {Nens}, {ndim}, {errval}, {emailaddress}, {outdir}, {modelStrings}, {argslist})
runitem.run_mcmc()
runitem.run_postproc()

