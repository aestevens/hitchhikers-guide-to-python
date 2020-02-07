# 🐍 Exploring *The Hitchhiker's Guide to Python* 
Below are my notes collected from the community-maintained [*The Hitchhiker’s Guide to Python*](https://docs.python-guide.org)

## Pipenv & Virtual Environments

### Pipenv - package management for Python
- Install packages with Pipenv
	- `$ pipenv install insert_package_name_here`

- Import syntax inside Python source code
	- `$ import insert_package_name_here`

- Run Python script with Pipenv
	- `$ pipenv run python file_name.py`
	
### virtualenv - create isolated 'virtual' environments
- Can be used standalone, in place of Pipenv
- Setting up a virtual environment gives you a specific version of the Python executable plus any dependencies
- Create a virtual environment with directory `venv`, a global naming convention
	- `$ virtualenv venv`
- Virtual environment requires activation to start using
	- macOS/Linux: `$ source venv/bin/activate`
	- Windows: `C:\Users\SomeUser\project_folder> venv\Scripts\activate`
- Install packages needed for a project with pip
- Virtual environment can be deactivated when needed. This will return to the system default Python interpreter and any installed packages.
	- `$ deactivate`
- Freeze the state of environment packages, allowing others to install the same packages with the same versions
	- `$ pip freeze > requirements.txt`
- Install packages
	- `$ pip install -r requirements.txt`
