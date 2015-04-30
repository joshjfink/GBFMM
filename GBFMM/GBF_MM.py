import numpy as np

class MM(object):
    def __init__(ngroups, betas, resp, sig2, goup_wts):
        resp.best = None
        resp.ngroups = ngroups
        resp.betas = betas
        resp.sig2 = sig2
        resp.goup_wts = goup_wts
        resp.its = []
        resp.loglike = []
        resp.ngroups = ngroups
        resp.loglike = np.array(resp.loglike)
        resp.best = resp.its[np.argmax(resp.loglike)]
        resp.its.append(MM(ngroups, goup_wts, betas, sig2))
        resp.loglike.append(loglike_null)

def mod_fit(dat, ngroups , set, max_its):
    loglike_new = 0.0
    it_new = 0.0
    loglike_old = 2.0 aspects_ = dat.values()[0][0].shape[1]
    # Initialize
    results = Output_GBF_MM(ngroups) # Function still to be coded
    group_wts = np.random.uniform(ngroups, size=(len(dat)))
    group_wts /= group_wts.sum(axis=1)[:,np.newaxis]
    ngroups = np.argmax(group_wts, axis=1)
    goup_wts, betas, sig2 = maximum_likelihood_parameters(dat, set, ngroups, aspects_, ngroups, group_wts)
    # Run Model Iterations
    while np.abs(loglike_old - loglike_new)>.01**3 and it_new < max_its:
		# Optimize coefficients
     	group_wts = calculate_group_wts(dat, set, goup_wts, betas, sig2)	
        goup_wts, betas, sig2 = maximum_likelihood_parameters(dat, set, ngroups, aspects_, ngroups, group_wts)
        # Logarithm of null likelihood
        loglike_old = loglike_new
        loglike_new = loglike_null(dat, set, ngroups, goup_wts, betas, sig2)
        # Progress Bar
        print '\t\t\t\t\t\t\t Hill Climbing...'
        # Complete Loop
        it_new += 1
    results.stop_alg()
    return results

def groups_alg(group_wts):
 	return np.argmax(group_wts, axis=1)

def regress_wghted(Y, X, wghts):
    # Linear Regression
    return np.linalg.pinv((wghts[:,np.newaxis]*X).T.dot(X)).dot((wghts[:,np.newaxis]*X).T.dot(Y))
    
def var_regress_wghted(Y,X, betas, wghts):
    result = 0.
    # Run weighted regression 
    for i in xrange(len(Y)):
        result += wghts[i]*(Y[i]-X[i].T.dot(betas))**2
    return result/wghts.sum()

def stop_alg(resp):
	# Halt EM model estimation
    resp.loglike = np.array(resp.loglike)
    resp.best = resp.its[np.argmax(resp.loglike)]

