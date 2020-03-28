# Chapter 2 - End-to-End Machine Learning Project

Code related to chapter 2

## Create workspace

### Install pip
Check if pip is installed:
```bash
$ python3 -m pip --version
```
Update pip:
```bash
$ python3 -m pip install --user -U pip
```

### Create an Isolated Environment

Install virtualenv
```bash
$ python3 -m pip install --user -U virtualenv
```

Create isolated Python Environment
```bash
$ python3 -m virtualenv venv
```

Activate virtual environment
```bash
$ cd <PROJECT DIR>
$ source venv/bin/activate  # Linux
$ .\env\Scripts\activate    # Windows
```

Type `deactivate` to deactivate this environment.

While the environment is active, any package installed using pip will be
installed in this isolated environment, and Python will only have access to
these packages (if access to the system’s packages is desired, create the
environment using virtualenv’s --system-site-packages option)
