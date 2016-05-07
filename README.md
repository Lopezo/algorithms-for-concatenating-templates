# Algorithms for concatenating templates

Python implementation of algorithms presented in the paper: [DOI 10.1063/1.4942799](http://dx.doi.org/10.1063/1.4942799). In this paper we present two algorithms for concatenating two branched manifolds described by a linking matrix. We also present algorithms we use to transform one mathematical description of a branched manifold $A$ using a matrix and an array ($TM(A)$ and $Ar(A)$) to another using a matrix ($T(A)$), and inversely.

## How to use it?

### Create an environment with dependencies

```sh
# Create a virtualenv
virtualenv -p python3 .concatenation_venv

# Activate it
source .concatenation_venv/bin/activate

# Install the dependencies
pip install numpy

# After the use of the program, deactivate the virtualenv
deactivate
```

### Run the application

```sh
python main.py
```
