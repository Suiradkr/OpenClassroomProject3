# OpenClassroom Project 3: Python ETL Pipeline
github repo: https://github.com/Suiradkr/OpenClassroomProject3.git
## Purpose
This ETL can be used to identify all running clusters, help determine if the cluster is being utilized, and can provide a list clusters that can be deleted which will ultimately free up resources and decrease the amount of cluster deployment times and failures.

### Navigate to the Project Folder

First, ensure you are in the `ETLClusterProject` directory:

```bash
cd ETLClusterProject
```

Create and activate virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the requirements in virtual environment
```bash
pip install -r requirements.txt 
```
### Run ETL:
```bash
python cluster_manager.py
```
**you will see transformed data in the terminal and in cluster_report.csv

### Create Flake8-html report:
```bash
flake8 --exclude .venv --format=html --htmldir=lint_report .
```
### Open Flake8-html report:
```bash
open lint_report/index.html 
```
