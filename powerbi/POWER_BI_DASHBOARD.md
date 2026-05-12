# Power BI Dashboard Guide

Use `healthcare_dataset.csv` as the source file and load it into Power BI as a table named `patients`.

## Data Columns

- `patient_id`
- `age`
- `gender`
- `diagnosis`
- `length_of_stay`
- `readmitted`

## Recommended Measures

```DAX
Diagnosis Count = COUNT(patients[patient_id])

Average Length of Stay = AVERAGE(patients[length_of_stay])

Readmission Count = CALCULATE(COUNT(patients[patient_id]), patients[readmitted] = 1)

Not Readmitted Count = CALCULATE(COUNT(patients[patient_id]), patients[readmitted] = 0)

Readmission Rate % = DIVIDE([Readmission Count], COUNT(patients[patient_id]))

Readmission Status = IF(patients[readmitted] = 1, "Readmitted", "Not Readmitted")
```

## Visual Setup

### Bar Chart

- Visual: clustered bar chart
- Axis: `diagnosis`
- Values: `Diagnosis Count`
- Sort: descending by `Diagnosis Count`

### KPI

- Visual: KPI or card
- Indicator: `Average Length of Stay`
- Display units: none
- Format: 1 or 2 decimal places

### Pie Chart

- Visual: pie chart
- Legend: `Readmission Status`
- Values: count of `patient_id`
- If you want the share of readmitted vs not readmitted patients, use the `Readmission Status` field as the legend and count of `patient_id` as values.

### Filter

- Visual: slicer
- Field: `diagnosis`
- Optional: enable single-select if you want to analyze one diagnosis at a time.

## Build Steps

1. Open Power BI Desktop.
2. Select Get Data and import `healthcare_dataset.csv`.
3. Confirm the table name is `patients`.
4. Create the measures above.
5. Add the bar chart, KPI, pie chart, and slicer to the report canvas.
6. Format the KPI and pie chart labels for readability.
7. Save the report and publish if needed.

## Notes

- `readmitted` is stored as `1` for readmitted and `0` for not readmitted.
- If Power BI imports the file with a different table name, update the DAX formulas to match that table name.
- The dataset is small enough that all visuals should refresh quickly.