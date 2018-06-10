def negLogLikelihood(params, data):
    """ the negative log-Likelohood-Function"""
    lamb = params[0]
    lnl = - poisson.logpmf(data, lamb).sum()
    return lnl


# minimize the negative log-Likelihood
result = optimize.minimize(negLogLikelihood,  x0=[1], args=(data,))

print(result)

# plot poisson-deviation with fitted parameter
x_plot = np.linspace(0, 12, 1500)

plt.hist(data.ravel(), bins=np.arange(12) - 0.5, density=True,)
plt.plot(x_plot, poisson.pmf(x_plot, result.x), 'r-', lw=2)
