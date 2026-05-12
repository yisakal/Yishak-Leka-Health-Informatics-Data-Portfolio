# Yishak-Leka-Health-Informatics-Data-Portfolio
This portfolio showcases my data analysis projects using healthcare datasets.

Skills demonstrated:
- Python (Pandas, Data Visualization)
- SQL (Data querying and aggregation)
- Power BI (Dashboard creation)

The projects focus on analyzing patient data to generate insights into healthcare trends such as diagnosis frequency, hospital stay duration, and readmissions.

## Power BI Dashboard

Use `healthcare_dataset.csv` as the source table for the dashboard.

See [POWER_BI_DASHBOARD.md](POWER_BI_DASHBOARD.md) for a step-by-step build guide.

### Visuals

- Bar chart: diagnosis counts
	- Axis: `diagnosis`
	- Values: count of `patient_id`
- KPI: average length of stay
	- Measure: average of `length_of_stay`
- Pie chart: readmission rate
	- Legend: readmission status
	- Values: count of `patient_id`
- Filter: diagnosis
	- Slicer field: `diagnosis`

### Suggested DAX Measures

```DAX
Diagnosis Count = COUNT(patients[patient_id])

Average Length of Stay = AVERAGE(patients[length_of_stay])

Readmission Count = CALCULATE(COUNT(patients[patient_id]), patients[readmitted] = 1)

Not Readmitted Count = CALCULATE(COUNT(patients[patient_id]), patients[readmitted] = 0)

Readmission Rate % = DIVIDE([Readmission Count], COUNT(patients[patient_id]))

Readmission Status = IF(patients[readmitted] = 1, "Readmitted", "Not Readmitted")
```

### Build Notes

- Load the CSV into Power BI as a table named `patients`.
- Use the `Readmission Status` field for the pie chart legend if you want to show the split between readmitted and not readmitted patients.
- Format `Average Length of Stay` as a whole number or decimal KPI, depending on the presentation style you want.
- Format `Readmission Rate %` as a percentage if you want the pie chart or KPI to display the rate directly.