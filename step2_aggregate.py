import pandas as pd
#Load generated Enrollment_span.csv file from step1 transformation and parse the data
enrollment = pd.read_csv('patient_enrollment_span.csv', parse_dates=['enrollment_start_date','enrollment_end_date'])
#Load outpatient visit data
no_of_visits = pd.read_csv("outpatient_visits_file.csv", parse_dates=['date'])

final_data = [] #list to accumulate final results

# Check for full row duplicates
duplicate_visits = no_of_visits.duplicated()

# Iterate over each enrollment span
for _, row in enrollment.iterrows():
    patient_id = row["patient_id"]
    start_date = row["enrollment_start_date"]
    end_date = row["enrollment_end_date"]
    
# Filter the visits for this patient within the enrollment window
    patient_visits = no_of_visits[
        (no_of_visits["patient_id"] == patient_id) &
        (no_of_visits["date"] >= start_date) &
        (no_of_visits["date"] <= end_date)
    ]
    
# Total visits and number of unique visit days
    total_visits = patient_visits["outpatient_visit_count"].sum()
    unique_days = patient_visits['date'].nunique()
    
    #Append the result for this enrollment period
    final_data.append([
    patient_id,
    start_date.date(),
    end_date.date(),
    total_visits,
    unique_days
])

#Transform the results to a Dataframe
result_df = pd.DataFrame(final_data, columns=[
    "patient_id", "enrollment_start_date", "enrollment_end_date", "ct_outpatient_visits", "ct_days_with_outpatient_visit"
])

#Save the result as CSV
result_df.to_csv("result.csv", index='False')

# Print the number of distinct values in days-with-visit column, here Answer: 33  
print("Answer2:", result_df["ct_days_with_outpatient_visit"].nunique()) 

