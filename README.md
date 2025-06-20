#📊 Healthcare BI Project – Patient Enrollment & Visit Analytics

This project simulates a real-world healthcare analytics workflow to clean, transform, and analyze patient data. It focuses on generating continuous enrollment spans and aggregating outpatient visit statistics using Python and Pandas.

 📁 Project Structure

| File                          | Description                                                        |
|-------------------------------|--------------------------------------------------------------------|
| `step1_transform.py`          | Transforms monthly enrollment data into continuous date spans     |
| `step2_aggregate.py`          | Aggregates outpatient visit data across enrollment spans          |
| `patient_id_month_year.csv`   | Input file for Step 1 – patient enrollment by month               |
| `outpatient_visits_file.csv`  | Input file for Step 2 – daily patient visit records               |
| `patient_enrollment_span.csv` | Output of Step 1 – continuous enrollment spans                    |
| `result.csv`                  | Output of Step 2 – visit count and distinct visit days per span   |


🛠️ Tech Stack

- Python 3.12
- Pandas
- Dateutil
- CSV

🧪 How to Run

Ensure Python and Pandas are installed, and place all CSV files in the project root directory

▶️ Step 1: Transform Monthly Enrollment Data
```bash
python step1_transform.py
Output: patient_enrollment_span.csv file


▶️ Step 2:Aggregate Visit Statistics
```bash
python step2_aggregate.py
Output: result.csv file
