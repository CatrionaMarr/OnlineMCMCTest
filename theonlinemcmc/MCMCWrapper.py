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
#errval = 0

class MCMCWrapper(object): # fix arg names before running idiot
	def __init__(self, sampler, theta, gauss_like_sigma, fitarray, Nmcmc, Nburnin, Nens, ndim, errval, emailaddress, outdir, modelStrings, argslist):
		self.sampler = sampler
    self.theta = theta
		self.gauss_like_sigma = gauss_like_sigma
		self.fitarray = fitarray
		self.Nmcmc = Nmcmc
    self.Nburnin = Nburnin
    self.Nens = Nens
    self.ndim = ndim
    self.errval = errval
    self.emailaddress = emailaddress
    self.outdir = outdir
    self.modelStrings = modelStrings
    self.argslist = argslist

		self.run_mcmc()
		self.run_postproc()

  for name in theta:
    thetajoin = self.thetajoin + ", " + name
  
	resultsaddress = "http://localhost/results/" + self.outdir
	thetajoinquotes = "'%s'"%thetajoin

	emailaddressquotes = "'%s'"%self.emailaddress
	resultsaddressquotes = "'%s'"%self.resultsaddress
	outdirquotes = "'%s'"%self.outdir
	modelStringsquotes = "'%s'"%self.modelStrings['outputstring']
	
	# read in the data
	if self.errval == 0:
  		try:
    		data = np.loadtxt("data_file.txt")
  		except:
    		try:
      			data = np.loadtxt("data_file.txt", delimiter=",")
    		except:
      			self.errval = DATA_READ_ERR


	# read in the abscissa values
	if self.errval == 0:
  		try:
    		abscissastring = np.loadtxt("abscissa_file.txt")
  		except:
    		try:
      			abscissastring = np.loadtxt("abscissa_file.txt", delimiter=",")
    		except:
      			self.errval = ABSCISSA_READ_ERR

  abscissastringquotes = "'%s'"abscissastring


	def run_mcmc():
		if self.sampler == "emcee":
			# define the log posterior function

			def lnprob(theta, abscissastring, gauss_like_sigma, data):
  				lp = lnprior(self.theta)
  				if not np.isfinite(lp):
    				return -np.inf

  				return lp + lnlike(theta, abscissastring, gauss_like_sigma, data)
			

			# define the log prior function -------FITARRAY
			def lnprior(theta):
  				lp = 0.
  				
  				for variable in self.theta:
  			   		if self.fitarray[variable][minval] < self.theta[variable] < self.fitarray[variable][maxval]:
  					#if -100 < m < 100:
    					lp = 0.
  					else:
    					return -np.inf
    				"""	
  					if -101 < c < 101:
    					lp = 0.
  					else:
    					return -np.inf
					"""
  					return lp

			# define log likelihood function
			def lnlike(theta, abscissastring, gauss_like_sigma, data):
  				#m,c = theta
  				md = mymodel(self.modelStrings[arguments])
  				return -0.5*np.sum(((md - self.data)/self.gauss_like_sigma)**2)
  				"""
				# set number of MCMC points
				Nmcmc = 1000
				Nburnin = 1000
				Nens = 100
				ndim = 2
				"""
			for variable in self.theta:
				# initialise the start ensemble points
				try:
					varini[variable] = self.fitarray[variable][minval] + np.random.rand(self.Nens) * (self.fitarray[variable][maxval] - self.fitarray[variable][minval])
					#mini = -100 + np.random.rand(Nens)*200
  					#cini = -101 + np.random.rand(Nens)*202
  					pos = np.array(varini).T
				except:
  					self.errval = PRIOR_INIT_ERR

			# read in the data
			if self.errval == 0:
  				try:
    				data = np.loadtxt("data_file.txt")
  				except:
    				try:
      					data = np.loadtxt("data_file.txt", delimiter=",")
    				except:
      					self.errval = DATA_READ_ERR

			# read in the abscissa values
			if self.errval == 0:
  				try:
    				abscissastring = np.loadtxt("abscissa_file.txt")
  				except:
    				try:
      					abscissastring = np.loadtxt("abscissa_file.txt", delimiter=",")
    				except:
      					self.errval = ABSCISSA_READ_ERR

			# read in sigma (standard deviation) values (there may be nothing here if it not applicable to your likelihood)
			#{readsigma}

			# run the MCMC
			if self.errval == 0:
  				if len(data) != len(abscissastring):
    				self.errval = DATA_LENGTH_ERR

  				#argslist = (abscissastring, 0.65, data)

			if self.errval == 0:
  				# set up sampler
  				try:
    				finalsampler = emcee.EnsembleSampler(Nens, ndim, lnprob, args=argslist)
  				except:
    				self.errval = MCMC_INIT_ERR

  				# run sampler
  				try:
    				finalsampler.run_mcmc(pos, Nmcmc+Nburnin)
    				# remove burn-in and flatten
    				samples = finalsampler.chain[:, self.Nburnin:, :].reshape((-1, self.ndim))
    				lnp = np.reshape(finalsampler.lnprobability[:, self.Nburnin:].flatten(), (-1,1))
    				samples = np.hstack((samples, lnp))
 	 			except:
    				self.errval = MCMC_RUN_ERR

  				# output the posterior samples, likelihood and variables
  				try:
    				np.savetxt('posterior_samples.txt.gz', samples)
    				fv = open('variables.txt', 'w')
    				fv.write(thetajoinquotes)
    				fv.close()
  				except:
    				self.errval = POST_OUTPUT_ERR
		


		#elif self.sampler == "pymc3":
			#run postproc in pymc3 form

		#elif self.sampler == "cpnest":
			#run postproc in cpnest form

	def run_postproc():

		try:
    		postprocessing(samples, thetajoinquotes, abscissastring, abscissastringquotes, data, emailaddressquotes, resultsaddressquotes)
  		except:
    		self.errval = POST_PROCESS_ERR

		success = True
		if self.errval != 0:
  			# run different script in case error codes are encountered
  			errorpage(self.errval, emailaddressquotes, resultsaddressquotes)
  			success = False

		database_add_row(outdirquotes, self.modelStrings, thetajoinquotes, len(theta), success)



#var sample = MCMCWrapper(data,prior,variables,sampler);
#sample.run_mcmc();
#sample.run_postproc();