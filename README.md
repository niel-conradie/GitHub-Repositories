# **GitHub Repositories**

**Most-Starred GitHub Repositories by Language written in [Python](https://www.python.org).**

Using GitHub API to request information about specific language repositories on the site, and then generate an interactive visualization of the relative popularity of these projects using Plotly.

---

## **Requirements**

- [Python 3.11.X](https://www.python.org/downloads/)
- [Plotly](https://plotly.com/python/getting-started/)
- [Requests](https://requests.readthedocs.io/en/latest/)

---

## **Installation**

GitHub Repositories can be installed via [Pip](https://pypi.org/project/pip/). To start, clone the repository to your local computer and change into the proper directory.

- **Clone Repository**

```bash
git clone https://github.com/niel-conradie/github-repositories.git
```

- **Change Directory**

```bash
cd github-repositories
```

### **Pip Install**

- **Create Environment**

```bash
python -m venv .venv
```

- **Activate Environment**

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

- **Install Requirements**

```bash
python -m pip install -r requirements.txt
```

---

## **Usage**

- To launch GitHub Repositories use the [run.py](https://github.com/niel-conradie/github-repositories/blob/master/github-repositories/run.py) file to start.

---

## **License**

[MIT License](https://github.com/niel-conradie/GitHub-Repositories/blob/master/LICENSE)

---
