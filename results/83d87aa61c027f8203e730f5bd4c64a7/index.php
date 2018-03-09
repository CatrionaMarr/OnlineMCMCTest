
<!DOCTYPE HTML>
<html>
<head>
  <!-- Theme Made By www.w3schools.com - No Copyright -->
<meta name="author" content="Matthew Pitkin">
<meta name="description" content="The Online MCMC">
<meta name="keywords" content="MCMC, Markov chain Monte Carlo, Bayesian, emcee, python, data analysis, probability">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.css">

<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

<!-- Include theme font -->
<link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">

<!-- Include jQuery -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

<!-- custom CSS file -->
<link rel="stylesheet" type="text/css" href="../../simple.css"/>

<!-- include MathJax -->
<script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

<title>The Online MCMC: Results page</title>
</head>

<body>

<!-- Navbar -->
<nav class="navbar navbar-default">
  <div class="container">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>                        
      </button>
      <a class="navbar-brand">THE ONLINE MCMC</a>
    </div>
    <div class="collapse navbar-collapse" id="myNavbar">
      <ul class="nav navbar-nav navbar-right">
        <li><a href="#margpos">MARGINALISED POSTERIORS</a></li>
        <li><a href="#bestfit">BEST FIT VALUES & DISTRIBUTION</a></li>        
        <li><a href="#links">LINKS</a></li>
      </ul>
    </div>
  </div>
</nav>

<div class="container-top bg-1 text-center">
  <h2 class="title">RESULTS</h2>
  <h3>Your results have been generated and are displayed below.</h3>
</div>

<div id="margpos" class="container-fluid bg-2 text-left">
  <h3 class="text-center" id="instructions">MARGINALISED POSTERIORS</h3>
  <p>
    The diagonal plots show the <a style="color: #BD5D38" href="https://en.wikipedia.org/wiki/Marginal_distribution">marginal</a> <a style="color: #BD5D38" href="https://en.wikipedia.org/wiki/Posterior_probability">posterior probability</a> distributions for each of your fitted parameters. The off-diagonal plots show 1 and 2&sigma; probability contours for the <a style="color: #BD5D38" href="https://en.wikipedia.org/wiki/Joint_probability_distribution">joint</a> marginal posterior probability distributions of pairs of parameters. This has been produced with <a style="color: #BD5D38" href="https://github.com/dfm/corner.py">corner.py</a>.
  </p>
  <img class="center-block bg-3" src="posterior_plots.png" >
</div>

<div id="bestfit" class="container-fluid bg-3 text-left">
  <h3 class="text-center" id="functions">BEST FIT VALUES</h3>
  
  The <a href="https://en.wikipedia.org/wiki/Mean">mean</a>, <a href="https://en.wikipedia.org/wiki/Median">median</a> and <a href="https://en.wikipedia.org/wiki/Mode_(statistics)">mode</a> of the probability distributions for each parameter. Also give are the <a href="https://en.wikipedia.org/wiki/Standard_deviation">standard deviation</a> of the distributions and minimal 68% and 95% <a href="https://en.wikipedia.org/wiki/Credible_interval">credible intervals</a> (CI).
  <div>
    <table class="table table-striped table-hover">
<tr><th>Variable</th><th>Mean</th><th>Median</th><th>Mode</th><th>&sigma;</th><th>68% CI</th><th>95% CI</th></tr>
<tr><td>\(m\)</td><td>1.0</td><td>1.0</td><td>1.0</td><td>0.3</td><td>[0.7, 1.3]</td><td>[0.4, 1.6]</td></tr><tr><td>\(c\)</td><td>-0.0</td><td>-0.0</td><td>-8.7&times;10<sup>-4</sup></td><td>0.8</td><td>[-0.9, 0.7]</td><td>[-1.6, 1.5]</td></tr></table>

  </div>

  <h3>Correlation coefficient matrix</h3>

  The <a href="https://en.wikipedia.org/wiki/Covariance_matrix#Correlation_matrix">correlation coefficients</a> between each of the fitted parameters.
  <div>
    <table class="table table-striped table-hover"><th></th><td>\(m\)</td><td>\(c\)</td></tr>
<tr><td>\(m\)</td><td>1.00</td><td>-0.91</td></tr>
<tr><td>\(c\)</td><td>-0.91</td><td>1.00</td></tr>
</table>

  </div>
</div>

<div class="container-fluid bg-1 text-left">
  <h3 class="text-center" id="instructions">BEST FIT MODEL DISTRIBUTION</h3>
  <p>
    This plot shows the distribution of 100 models drawn randomly from the posterior distribution. The best fitting models will be clustered over each other.
  </p>
  <img class="center-block bg-3" src="model_plot.png" width="60%">
</div>

<div id="links" class="container-fluid bg-3 text-left">
  <h2 class="text-center">LINKS</h2>
  <h3>Code links</h3>
  The <a href="https://www.python.org/">python</a> files for running the MCMC are provided below. These use the <a href="http://dan.iel.fm/emcee/current/">emcee</a> python module.
  <ul>
    <li><a href="pyfile.py"><code>pyfile.py</code></a> - the python file used to run the MCMC</li>
    <li><a href="mymodel.py"><code>mymodel.py</code></a> - the python model function</li>
  </ul>

  <h3>Data links</h3>
  <ul>
    <li><a href="posterior_samples.txt.gz"><code>posterior_samples.txt.gz</code></a> - a gzipped tarball containing the posterior samples</li>
    <li><a href="variables.txt"><code>variables.txt</code></a> - the variables in the order of the posterior file</li>
  </ul>
</div>

 <footer class="container-fluid bg-2 text-center">
  <p class="footer"> &copy; Matthew Pitkin (2015), Catriona Marr (2018). The code for this site is licensed under the <a style="color: #BD5D38" href="http://opensource.org/licenses/MIT">MIT license</a>. It is available on <a style="color: #BD5D38" href="https://github.com/mattpitkin/theonlinemcmc">github</a> and <a style="color: #BD5D38" href="https://bitbucket.org/mattpitkin/theonlinemcmc">bitbucket</a>.<br>This site is kindly hosted by the <a style="color: #BD5D38" href="http://www.gla.ac.uk/schools/physics/">School of Physics & Astronomy</a> at the <a style="color: #BD5D38" href="http://www.gla.ac.uk/">University of Glasgow</a>. They bear no reponsibility for the content of this site or the results that are produced.
  </p>

<!-- include social media sharing -->
<?php
$shareurl = "http://localhost/results/83d87aa61c027f8203e730f5bd4c64a7";
include('../../social.inc');
?>
</div>
</body>
