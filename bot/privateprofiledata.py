import pandas as pd

# Read the XLSX file
df = pd.read_excel('privateprofile.xlsx')

# Extract data from columns 1 and 2
column1_data = df.iloc[:, 0].tolist()
column2_data = df.iloc[:, 1].tolist()

# Find values present in column 1 but not in column 2
values_only_in_column1 = set(column1_data) - set(column2_data)

# Create a DataFrame with the values
result_df = pd.DataFrame({'Values': list(values_only_in_column1)})

# Save the DataFrame to a CSV file
result_df.to_csv('result.csv', index=False)
