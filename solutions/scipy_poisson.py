def negLogLikelihood(params, data):
    """ the negative log-Likelohood-Function"""
    lnl = - np.sum(poisson.logpmf(data, params[0]))
    return lnl


# minimize the negative log-Likelihood
result = optimize.minimize(negLogLikelihood,  x0=[1], args=(data,))

print(result)

# plot poisson-deviation with fitted parameter
x_plot = np.arange(-1, 12)

plt.hist(data.ravel(), bins=np.arange(12) - 0.5, density=True,)
plt.step(x_plot, poisson.pmf(x_plot, result.x), 'r-', lw=2, where='mid')
