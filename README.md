# **GitHub Repositories**

**Most-Starred GitHub Repositories by Language written in [Python](https://www.python.org).**

Using GitHub API to request information about specific language repositories on the site, and then generate an interactive visualization of the relative popularity of these projects using Plotly.

----
## **Requirements**

- [Python 3.10.5](https://www.python.org/downloads/release/python-3105/)
- [Plotly 5.9.0](https://plotly.com/python/getting-started/)
- [Requests 2.28.1](https://requests.readthedocs.io/en/latest/)
----
## **Installation**

GitHub Repositories can be installed via [Pip](https://pypi.org/project/pip/). To start, clone the repository to your local computer and change into the proper directory.

* **Clone Repository**
```bash
  $ git clone https://github.com/niel-conradie/github-repositories.git
  $ cd github-repositories
```
### **Pip Install**

* **Create Environment**
```bash
  $ python -m venv .venv
```
* **Activate Environment**
```bash
  # Bash
  $ source .venv/Scripts/activate

  # Command Prompt
  C:> .venv\Scripts\activate.bat

  # macOS
  $ .venv/bin/activate

  # PowerShell
  PS C:> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  PS C:> .venv\Scripts\Activate.ps1
```
* **Install Requirements**
```bash
  (.venv) $ python -m pip install -r requirements.txt
```
----
## **Usage**

To launch GitHub Repositories use thus file.
```bash
  run.py
```
----
## **License**

[MIT License](https://github.com/niel-conradie/GitHub-Repositories/blob/master/LICENSE)

----