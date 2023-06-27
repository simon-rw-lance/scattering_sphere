import numpy as np
import matplotlib.pyplot as plt
import csv
import time
import argparse

from .photon import Photon

def _parse_args():
    # Parse command line arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--iter", type=float, default=1e4, help='Number of photons.')
    parser.add_argument("-tau", "--opacity", type=float, default=1.0, help='Optical depth.')
    parser.add_argument("-p", "--plot", type=bool, default=False, help='Plot the results.')
    args = parser.parse_args()
    return args

def main():
    args = _parse_args()

    # Set up input variables.
    iter = int(args.iter)
    OPACITY = args.opacity

    # Create save suffix to allow floating point opacity values.
    if OPACITY.is_integer():
        save_suffix = f'{int(OPACITY)}'
    else:
        save_suffix = f'{OPACITY}'.replace(".", "p")

    # Initialse an array of zeros to store the total number of scatterings for each photon.
    scatters = np.zeros(iter,dtype=int)

    t_phot_start = time.time() # Start main loop timer

    # Main loop over all photons.
    for i in range(iter): 
        photon = Photon(OPACITY)
        while photon.radiusCalc() < 1: # Loop until photon leaves the sphere
            photon.scatter()
            photon.travel(OPACITY)
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

if __name__ == "__main__":
    main()
