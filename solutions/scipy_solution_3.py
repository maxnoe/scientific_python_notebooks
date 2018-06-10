# The clock speed gives us the points in time we need to sample the signal.
clock = np.arange(clock_speed, len(alien_signal), sample_length)

plt.figure()
plt.plot(alien_signal)
plt.plot(clock, alien_signal[clock], 'ro')


#Now cross correlate the signal with the pulse shape. We know the pulse shape and its length.

corr = signal.correlate(alien_signal, signal.boxcar(sample_length), mode='same') /sample_length
plt.figure()
plt.plot(corr)
plt.plot(clock, corr[clock], 'ro')
plt.axhline(0.5, ls='--', color='gray')


# decode the aline message
a = np.where(corr[clock] > 0.5, 1, 0)
s = bytearray(np.packbits(a)).decode('ascii')

print(f'Decoded Alien Message is:  "{s}" ')
