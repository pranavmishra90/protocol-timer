# Protocol Timer

A timer designed to follow along the steps of a laboratory protocol and provide notifications when it's time for the next step

[![Protocol Timer - Test](https://github.com/pranavmishra90/protocol-timer/actions/workflows/ffpe.yml/badge.svg)](https://github.com/pranavmishra90/protocol-timer/actions/workflows/ffpe.yml)

## Python Enviroment
The protocol timer (and this repository) works using python. To run the timer's notebook, you will need to have a python environment ready. For convenience, I have described the way to create an isolated python "environment" just for this timer. 

### Create it locally
Using `conda` / `mamba`, create a python environment locally to a folder `env/`

````sh
mamba env create --prefix ./env -f ./environment.yml
````

You can substitute other conda-like commands for `mamba`, including `conda`, `micromamba`, etc.


## Coming soon - launch in binder

Binder is an incredible free service that lets you launch this repository in your browser without having to install anything. At the moment, there appears to be a bug in how binder allows for the programmatic creation of new jupyter notebook cells - only the last step of the protocol is performed.

[![Binder - pranavmishra90/protocol-timer](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pranavmishra90/protocol-timer/HEAD?labpath=protocol-timer.ipynb)


## License

[MIT License](./license.md)

Copyright (c) 2023 Pranav Kumar Mishra
