# Scattering sphere
Python code for simple scattering sphere calculations.

```shell
usage: scattering_sphere.py [-h] [-n ITER] [-tau OPACITY] [-p PLOT]

optional arguments:
  -h, --help                        show this help message and exit
  -n ITER, --iter ITER              Number of photons.
  -tau OPACITY, --opacity OPACITY   Optical depth.
  -p PLOT, --plot PLOT              Plot the results.
```

E.g. (output as seen in ```examples/```):
```shell
python3 scattering_sphere.py -n 1e6 -tau 2 -p True
```
