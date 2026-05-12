# Project Overview

This repository contains a small healthcare dataset and accompanying analysis assets: a SQL analysis script, a Python notebook, and Power BI dashboard notes.

## Purpose

Provide reproducible analysis of patient diagnosis frequency, average hospital stay, and readmission rate using the provided dataset.

## Key files

- Data: `Data/healthcare_dataset.csv`
- Notebook: `python/python_analysis.ipynb`
- SQL script: `sql/sql_analysis.sql`
- Power BI guide: `powerbi/POWER_BI_DASHBOARD.md`
- README: `README.md`

## Dataset schema

- `patient_id` (int)
- `age` (int)
- `gender` (string)
- `diagnosis` (string)
- `length_of_stay` (int)
- `readmitted` (0/1)

## How to run the Python analysis locally

1. Create and activate a Python environment (optional but recommended).

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies.

```bash
python -m pip install --upgrade pip
python -m pip install pandas matplotlib
```

3. Execute the notebook (headless) to reproduce outputs.

```bash
jupyter nbconvert --to notebook --execute python/python_analysis.ipynb --output executed_notebook.ipynb
```

Or open the notebook in Jupyter/VS Code and run cells interactively.

## How to load the CSV into a database

SQLite (quick local test):

```bash
sqlite3 patients.db
-- inside sqlite3 shell
.mode csv
.import Data/healthcare_dataset.csv patients
```

PostgreSQL (server):

```sql
CREATE TABLE patients (...);
COPY patients (patient_id, age, gender, diagnosis, length_of_stay, readmitted)
FROM '/absolute/path/to/Data/healthcare_dataset.csv' WITH (FORMAT csv, HEADER true);
```

MySQL (server):

```sql
LOAD DATA LOCAL INFILE 'Data/healthcare_dataset.csv'
INTO TABLE patients
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;
```

See `sql/sql_analysis.sql` for a cross-dialect script with table schema and example load commands.

## Power BI

Open Power BI Desktop, import `Data/healthcare_dataset.csv`, and follow the guide in `powerbi/POWER_BI_DASHBOARD.md` to create the bar chart (diagnosis counts), KPI (average length of stay), pie chart (readmission split), and a diagnosis slicer.

## Notes

- The repository layout may be updated; check the `Data/`, `python/`, `sql/`, and `powerbi/` folders for the latest locations of files.

