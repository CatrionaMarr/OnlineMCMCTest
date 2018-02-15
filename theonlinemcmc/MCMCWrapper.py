class MCMCWrapper(object):
	def __init__(self, data, prior, parameters, sampler):
		self.data = data
		self.prior = prior
		self.parameters = parameters
		self.sampler = sampler

		self.run_mcmc()
		self.run_postproc()

	def run_mcmc(self):
		if self.sampler == "emcee":
			self.run_postproc(data, prior, parameters) #in mcmc form


		#elif self.sampler == "pymc3":
			#run postproc in pymc3 form

		#elif self.sampler == "cpnest":
			#run postproc in cpnest form

	def run_postproc(self, data, prior, parameters):
		#run
