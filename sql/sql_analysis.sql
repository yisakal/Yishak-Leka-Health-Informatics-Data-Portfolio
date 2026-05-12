-- Load and analyze the healthcare dataset.
-- The CSV is tab-separated and uses these columns:
-- patient_id, age, gender, diagnosis, length_of_stay, readmitted

DROP TABLE IF EXISTS patients;

CREATE TABLE patients (
	patient_id INTEGER PRIMARY KEY,
	age INTEGER,
	gender TEXT,
	diagnosis TEXT,
	length_of_stay INTEGER,
	readmitted INTEGER
);

-- MySQL
-- Adjust the file path if healthcare_dataset.csv is not in the server's import directory.
-- LOAD DATA LOCAL INFILE 'healthcare_dataset.csv'
-- INTO TABLE patients
-- FIELDS TERMINATED BY '\t'
-- LINES TERMINATED BY '\n'
-- IGNORE 1 LINES
-- (patient_id, age, gender, diagnosis, length_of_stay, readmitted);

-- PostgreSQL
-- COPY patients (patient_id, age, gender, diagnosis, length_of_stay, readmitted)
-- FROM '/absolute/path/to/healthcare_dataset.csv'
-- WITH (FORMAT csv, HEADER true, DELIMITER E'\t');

-- SQLite
-- .mode tabs
-- .import healthcare_dataset.csv patients

-- Top diagnoses
SELECT diagnosis, COUNT(*) AS total_cases
FROM patients
GROUP BY diagnosis
ORDER BY total_cases DESC, diagnosis;

-- Average hospital stay
SELECT ROUND(AVG(length_of_stay), 2) AS average_hospital_stay
FROM patients;

-- Readmission rate
SELECT ROUND(AVG(readmitted) * 100, 2) AS readmission_rate_percent
FROM patients;
