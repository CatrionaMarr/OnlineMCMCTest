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

  if log(1) < m < log(1):
    lp = 0.
  else:
    return -np.inf

  lp -= 0.5*(c - 1)**2/0.65**2

  return lp


# define log likelihood function
def lnlike(theta, x, sigma_gauss, data):
  m,c = theta
  m = exp(m)
  md = mymodel(m,c,x)
  return -0.5*np.sum(((md - data)/sigma_gauss)**2)


# set number of MCMC points
Nmcmc = 1000
Nburnin = 1000
Nens = 100
ndim = 2

# initialise the start ensemble points
try:
  mini = log(1) + np.random.rand(Nens)*(log(1) - log(1))
  cini = 1 + np.random.randn(Nens)*0.65
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
if errval == 0:
  try:
    sigma_data = np.loadtxt("sigma_file.txt")
    if len(sigma_data) != len(data):
      errval = DATA_LENGTH_ERR
  except:
    try:
      sigma_data = np.loadtxt("sigma_file.txt", delimiter=",")
      if len(sigma_data) != len(data):
        errval = DATA_LENGTH_ERR
    except:
      errval = SIGMA_READ_ERR


# run the MCMC
if errval == 0:
  if len(data) != len(x):
    errval = DATA_LENGTH_ERR

  argslist = (x, sigma_data, data)

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
    samples[:,0] = exp(samples[:,0])
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
    postprocessing(samples, "m,c", x, "x", data, "fanatapan@yahoo.co.uk", "http://localhost/results/f6006e955a859812f37d62462121b224")
  except:
    errval = POST_PROCESS_ERR

success = True
if errval != 0:
  # run different script in case error codes are encountered
  errorpage(errval, "fanatapan@yahoo.co.uk", "http://localhost/results/f6006e955a859812f37d62462121b224")
  success = False

  # run post-processing script
  try:
    MCMCWrapper(1 2 3 4, "m,c", m,x,c, "emcee")
database_add_row("f6006e955a859812f37d62462121b224", "m*x+c", "m,c", 2, success)

