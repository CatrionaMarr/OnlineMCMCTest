#!/usr/bin/env python

# import required packages
import emcee
import numpy as np
from numpy import exp, log

# import model function from separate file
from mymodel import mymodel

# import post-processing function from theonlinemcmc package
from theonlinemcmc import *

# initialise error code value
errval = 0

#MCMCWrapper
sample = MCMCWrapper({wrapper_data}, {theta}, {variables}, {sampler_type})

#MCMCWrapper args
wrapper_data = {wrapper_data}theta = {theta}variables = {variables}sampler_type = {sampler_type}
{sampler_type}{theta}{variables}{sampler_type}
# define the log posterior function
def lnprob(theta, x, sigma_gauss, data):
  lp = lnprior(theta)
  if not np.isfinite(lp):
    return -np.inf

  return lp + lnlike(theta, x, sigma_gauss, data)


# define the log prior function
def lnprior(theta):
  lp = 0.
  m,c = theta

  if -10 < m < 10:
    lp = 0.
  else:
    return -np.inf

  if -10 < c < 10:
    lp = 0.
  else:
    return -np.inf

  return lp


# define log likelihood function
def lnlike(theta, x, sigma_gauss, data):
  m,c = theta
  md = mymodel(m,c,x)
  return -0.5*np.sum(((md - data)/sigma_gauss)**2)


# set number of MCMC points
Nmcmc = 1000
Nburnin = 1000
Nens = 100
ndim = 2

# initialise the start ensemble points
try:
  mini = -10 + np.random.rand(Nens)*20
  cini = -10 + np.random.rand(Nens)*20
  pos = np.array([mini, cini]).T
except:
  errval = PRIOR_INIT_ERR

# read in the data
if errval == 0:
  try:
    data = np.loadtxt("data_file.txt")
  except:
    try:
      data = np.loadtxt("data_file.txt", delimiter=",")
    except:
      errval = DATA_READ_ERR


# read in the abscissa values
if errval == 0:
  try:
    x = np.loadtxt("abscissa_file.txt")
  except:
    try:
      x = np.loadtxt("abscissa_file.txt", delimiter=",")
    except:
      errval = ABSCISSA_READ_ERR


# read in sigma (standard deviation) values (there may be nothing here if it not applicable to your likelihood)

# run the MCMC
if errval == 0:
  if len(data) != len(x):
    errval = DATA_LENGTH_ERR

  argslist = (x, 0.65, data)

if errval == 0:
  # set up sampler
  try:
    sampler = emcee.EnsembleSampler(Nens, ndim, lnprob, args=argslist)
  except:
    errval = MCMC_INIT_ERR

  # run sampler
  try:
    sampler.run_mcmc(pos, Nmcmc+Nburnin)
    # remove burn-in and flatten
    samples = sampler.chain[:, Nburnin:, :].reshape((-1, ndim))
    lnp = np.reshape(sampler.lnprobability[:, Nburnin:].flatten(), (-1,1))
    samples = np.hstack((samples, lnp))
  except:
    errval = MCMC_RUN_ERR

  # output the posterior samples, likelihood and variables
  try:
    np.savetxt('posterior_samples.txt.gz', samples)
    fv = open('variables.txt', 'w')
    fv.write("m,c")
    fv.close()
  except:
    errval = POST_OUTPUT_ERR

  # run post-processing script
  try:
    postprocessing(samples, "m,c", x, "x", data, "fanatapan@yahoo.co.uk", "http://localhost/results/6f45520e0bf7e366b59e9fba3b80dcc8")
  except:
    errval = POST_PROCESS_ERR

success = True
if errval != 0:
  # run different script in case error codes are encountered
  errorpage(errval, "fanatapan@yahoo.co.uk", "http://localhost/results/6f45520e0bf7e366b59e9fba3b80dcc8")
  success = False

  # run post-processing script
  try:
    MCMCWrapper(1 2 3 4, "m,c", m,x,c, "emcee")
database_add_row("6f45520e0bf7e366b59e9fba3b80dcc8", "m*x+c", "m,c", 2, success)


