# Scattering sphere
Package for simple scattering sphere calculations.

## Installation

```scattering_sphere``` can be installed using ```pip```. 

First it is recommended you ensure ```pip``` is up to date:

```
$ python3 -m pip install -U --user pip
```

From the root directory (where the ```pyproject.toml``` file is located),  ```scattering_sphere``` can then be installed with the following command:

```
$ python3 -m pip install -U . 
```

## Running 

After installation ```scattering_sphere``` can be run from any location (note that outputs produced from the -p flag will be saved in current directory) 

```
usage: scattering_sphere [-h] [-n ITER] [-tau OPACITY] [-p PLOT]

optional arguments:
  -h, --help                        show this help message and exit
  -n ITER, --iter ITER              Number of photons (default: 1e4).
  -tau OPACITY, --opacity OPACITY   Optical depth (default: 1.0).
  -p PLOT, --plot PLOT              Plot the results in current directory (default: False).
```

E.g. (output as seen in ```examples/```):
```shell
scattering_sphere -n 1e6 -tau 2 -p True
```

