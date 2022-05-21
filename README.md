# GUT_MultiagentModel
Gdańsk University of Technology Project for modeling economic processes 

## Initialization

Create a new python virtual environmen (*venv* from now on)

`python -m venv <path>`

where `<path>` is the path where the environment will be created (I'd recommend to create it in the repos root directory as it is ignored - `.venv` or `venv`)

Next make sure to run the application using the venv by creating a shell that runs in it:

**PowerShell**

`.\.venv\Scripts\Activate.ps1` or `.\.venv\Scripts\activate`

**CMD**

`.\.venv\Scripts\activate.bat`

**VS Code** (requires the Python extension from Microsoft)

**View**->**Command Palette** (or Ctrl+Shift+P), **Python: Select interpreter** and select the one in `<path>`

### Install requirements

As venvs may not contain the necessary scripts and packages, they need to be installed using:

`pip install -r requirements.txt`

## Project details

The topic of PRNG (Pseudo Random Number Generator) seems to be a side-topic for non-security/non-cryptography and non-simulation people - the first PRNG i stumpled upon is the **Mersenne Twister** which has a **period of *2^19937 - 1***
