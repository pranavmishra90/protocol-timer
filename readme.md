# Protocol Timer

A timer designed to follow along the steps of a laboratory protocol and provide notifications when it's time for the next step


## Python Enviroment
The protocol timer (and this repository) works using python. To run the timer's notebook, you will need to have a python environment ready. For convenience, I have described the way to create an isolated python "environment" just for this timer. 

### Create it locally
Using `conda` / `mamba`, create a python environment locally to a folder `env/`

````sh
mamba env create --prefix ./env -f ./environment.yaml
````

You can substitute other conda-like commands for `mamba`, including `conda`, `micromamba`, etc.


## License

[MIT License](./license.md)

Copyright (c) 2023 Pranav Kumar Mishra
