# Parse OSCARS website

A script to parse the OSCARS website to see which institutions have received funding from them.

## Inputs

- pages: saved html from the 3 pages of the OSCARS website listing projects

## Outputs

- project_institutions.csv: csv with the institutions and the projects they are involved in
- projects: saved html from the projects

How to run:

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Get projects (creates projects/ folder with html files)
python get_projects.py

# Get institutions (creates project_institutions.csv)
python get_institutions.py
```
