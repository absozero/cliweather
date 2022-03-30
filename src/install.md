# Installation
First [install the python interpreter](https://docs.python.org/3/using/index.html)(*required*)

## Easy way
```bash
pip install git+https://github.com/absozero/cliweather.git
```
This installs the latest version of cliweather from the github repo, and requires setuptools to be installed, which can be done with
```bash
pip install setuptools
```
This method **could** mess up system libraries, mostly likely on linux, so if that is a worry, stick to the harder way.

## Harder way
1. Clone the repository
```bash,editable
gh repo clone absozero/cliweather
 or
git clone https://github.com/absozero/cliweather.git
```
2. Get into the folder:
```bash,editable
cd cliweather
```

3. Then, create a virtual environment(Basically, it isolates packages from the rest of the system) by using
```bash,editable
python3 -m venv venv
 or
python -m venv venv
```
4. Then initialize the environment with the scripts given in the venv/Scripts or the venv/bin folder. You may have to use on mac and linux
```bash,editable
venv/Scripts/(activate.cmd)/(activate.ps1)
 or
. venv/bin/activate
```
5. Setuptools is required to install the bot[^note], and it is generally given with every distribution of python, but if it isn't, use the following to see how to install setuptools before the bot to install this tool
```bash,editable
pip install setuptools
pip install .
```

Then, you run the actual program, inside your virtual environment.
```bash,editable
cliw
```

**Now, you are finished with the installation of cliweather**

[^note]: Setuptools not being installed will render the setup.py file used with pip to not work at all, and packages have to be installed manually and the code has to be changed to accomodate for this.
