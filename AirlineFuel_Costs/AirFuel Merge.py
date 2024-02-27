import os
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
csv_directory = os.path.join(desktop_path, 'AirlineFuel_Costs')
print(csv_directory)


import os
import pandas as pd

# Construct the path to the directory containing CSV files
csv_directory = '/Users/shivanibhasin/Desktop/AirlineFuel_Costs'

# List CSV files in the directory
dfs = []
for i in range(1, 27):
    filename = f'T_F41SCHEDULE_P12A-{i}.csv'
    file_path = os.path.join(csv_directory, filename)
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        dfs.append(df)
    else:
        print(f"File '{filename}' not found.")

# Concatenate DataFrames
if dfs:
    merged_df = pd.concat(dfs, ignore_index=True)

    # Write merged DataFrame to CSV
    merged_df.to_csv(os.path.join(csv_directory, 'merged_output.csv'), index=False)
else:
    print("No files found to merge.")
