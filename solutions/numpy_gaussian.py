import numpy as np

numbers = np.random.normal(2, 3, 10000)

mu = np.mean(numbers)
sigma = np.std(numbers)

print('mean:', mu)
print('std:', sigma)

mask = np.logical_or(numbers < (mu - sigma), numbers > (mu + sigma))

print('Outside 1 sigma:', len(numbers[mask]) / len(numbers))

mask = numbers >= 0

print('n>0:', len(numbers[mask]))
print('std, where x > 0:', np.std(numbers[mask]))
