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


## Structuring Projects

### Creating a `tests` directory
Recommended approach for `import`ing a module/library in a project repository's test file(s): "Use a simple (but _explicit_) path modification to resolve the package properly."

1. Create `tests/context.py`:
```python
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import module_name_here
```

2. Inside a given test file, use `from .context import module_name_here

### Code Smells 👃
- Circular dependencies
- Hidden coupling
- Heavy use of global state/context
- Spaghetti code
- **Ravioli code**: "hundreds of similar little pieces of logic, often classes or objects, without proper structure"

### Modules
- Module names should be short and descriptive and should avoid use of special characters.
- Don't use periods (.), underscores, (_) or hyphens (-). ( - is the subtraction operator.)
#### Imports
- Explicit
`from module import func`
- General
`import module`
- Bad
`from modu import *`

### Packages
- If a directory has `__init__.py`, it's considered a Python package.
	- E.g., a directory `/case` with `wonkabar.py` => `import case.wonkabar`
		- Look for `__init__.py` in `case`, execute all of its top-level statements
		- Look for `case/wonkabar.py`, execute all of its top-level statements
		- Any variable, function, or class defined in `wonkabar.py` is given by the case.wonkabar namespace
- Ideally `__init__.py` should be empty.
- Aliasing for nested package: `import deeply.nested.module as mod`
