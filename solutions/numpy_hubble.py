import numpy as np

n = 100000
h0 = np.random.normal(67.74, 0.47, n)
distance = np.random.normal(500, 100, n)

velocities = h0 * distance

velocity_mean = np.mean(velocities)
velocity_unc = np.std(velocities)

print('({:.0f} ± {:.0f}) km/s'.format(velocity_mean, velocity_unc))
