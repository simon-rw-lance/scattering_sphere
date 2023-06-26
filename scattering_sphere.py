import numpy as np
import matplotlib.pyplot as plt
import csv
import time
import argparse

# Parse command line arguments.
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--iter", type=float, default=1e4, help='Number of photons.')
parser.add_argument("-tau", "--opacity", type=float, default=1, help='Optical depth.')
parser.add_argument("-p", "--plot", type=bool, default=False, help='Plot the results.')
args = parser.parse_args()

# Set up input variables.
iter = int(args.iter)
OPACITY = args.opacity

# Create save suffix to allow floating point opacity values.
if OPACITY.is_integer():
    save_suffix = f'{int(OPACITY)}'
else:
    save_suffix = f'{OPACITY}'.replace(".", "p")

# Define photon class.
class Photon():
    def __init__(self):
        '''
        Initialises the photon at the centre of the sphere. 
        '''
        self.x = 0 # position
        self.y = 0
        self.z = 0
        self.dir_x = 0  # direction of travel
        self.dir_y = 0
        self.dir_z = 0
        
        # Initial scattering of the photon
        self.scatter()
        self.travel()

    def radiusCalc(self):
        '''
        Calculates the radius of the photon from the centre of the sphere
        '''
        r = np.sqrt(self.x**2 + self.y**2 + self.z**2)
        return r

    def scatter(self):
        '''
        Scattering angle - Alters direction of travel
        '''
        phi = np.random.random()*np.pi
        theta = np.random.random()*2*np.pi
        self.dir_x = np.sin(phi)*np.cos(theta)
        self.dir_y = np.sin(phi)*np.sin(theta)
        self.dir_z = np.cos(phi)
        assert np.isclose(self.dir_x**2 + self.dir_y**2 + self.dir_z**2, 1) # Check direction is a unit vector.

    def travel(self):
        '''
        Travel distance - Alters position of photon
        '''
        eta = np.random.random() # I / I_0
        d = -np.log(eta)/OPACITY
        self.x += d*self.dir_x
        self.y += d*self.dir_y
        self.z += d*self.dir_z

# Initialse an array of zeros to store the total number of scatterings for each photon.
scatters = np.zeros(iter,dtype=int)

t_phot_start = time.time() # Start main loop timer

# Main loop over all photons.
for i in range(iter): 
    photon = Photon()
    while photon.radiusCalc() < 1: # Loop until photon leaves the sphere
        photon.scatter()
        photon.travel()
        scatters[i] += 1
    if (i/iter)*100 % 10 == 0: # Print progress
        print(f"{i/iter*100:.0f}% of photons completed.")
print(f"100% of photons completed.") 

t_phot_end = time.time() # End main loop timer
print(f"{t_phot_end-t_phot_start:.2f} seconds for {iter} photons.")

# Plot the results and save as a .pdf file.
if args.plot: 
    for i in range(np.min(scatters), np.max(scatters)):
        plt.plot(i, np.count_nonzero(scatters==i), 'x', c='k')
    plt.title(rf"Mean scatterings: {np.sum(scatters)/iter:.3f} $~~~~~~$ $\tau + \frac{{\tau^2}}{{2}} = ${OPACITY+(OPACITY**2)/2}")
    plt.annotate(rf"$\tau = $ {OPACITY}", (0.82,0.9), xycoords='axes fraction')
    plt.annotate(rf"$N = $ {iter:.0e}", (0.82,0.95), xycoords='axes fraction')
    plt.ylabel("Number of photons")
    plt.xlabel("Number of scatterings")
    plt.savefig(f"scatters_tau_{save_suffix}.pdf")

# Save the results to a .csv file.
with open(f'scatters_tau_{save_suffix}.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(zip(scatters))