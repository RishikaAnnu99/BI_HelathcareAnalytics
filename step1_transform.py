import pandas as pd
from datetime import timedelta
from dateutil.relativedelta import relativedelta

# Load the monthly enrollment data CSV file, then convert the month_year column into actual datetime objects
df = pd.read_csv("patient_id_month_year.csv", parse_dates=["month_year"])
#sort data
df = df.sort_values(['patient_id','month_year'])

#Generate spans, which holds each patient's continuous enrollment Interval
enrollment_spans = []

#Process one patient at a time
for patient_id, group in df.groupby('patient_id'):
    group = group.sort_values('month_year').reset_index(drop=True) # Make sure the data is sorter and indexed from 0

    start_date = group.iloc[0]['month_year'] # start the span with first month
    end_date = start_date

    #Loop through rest of the months for this patient
    for i in range(1, len(group)):
        current_date = group.iloc[i]['month_year']
    #If the month is less than or equal to 31 days after the last month, continue the span
        if (current_date - end_date).days <= 31:
            end_date = current_date
        else:
            #if there's a gap, end the current span and start a new one
            span_end = end_date + relativedelta(months=1) - timedelta(days=1)
            enrollment_spans.append([patient_id, start_date, span_end])

            #start a new span
            start_date = current_date
            end_date = current_date

    #After finishing all months for this patient, Add the final span
    span_end = end_date + relativedelta(months=1) - timedelta(days=1)
    enrollment_spans.append([patient_id, start_date, span_end])

#Convert the list of spans into a dataframe
result_df = pd.DataFrame(enrollment_spans, columns=["patient_id", "enrollment_start_date", "enrollment_end_date"])
#Save the result as CSV
result_df.to_csv("patient_enrollment_span.csv", index = False)

print("Answer 1:", len(result_df)) #Prints the number of rows in patient_enrollment_span.csv as Answer 1: 3105