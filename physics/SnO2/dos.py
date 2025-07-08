import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d

energy, dos = np.loadtxt('SnO2.dos', unpack=True, usecols=(0,1))
sigma = 20.0
dos_smoothed = gaussian_filter1d(dos, sigma=sigma)
plt.figure(figsize=(10,6))
plt.plot(energy, dos_smoothed, 'b-', linewidth=2)
plt.xlabel('Energy (eV)')
plt.ylabel('DOS (states/eV)')
plt.title('Density of States')
plt.xlim(-10, 20)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()