import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Department': ['Marketing', 'Finance', 'Marketing']}
df = pd.DataFrame(data)

# Filter rows where Department is 'Marketing'
filtered_df = df[df['Department'] == 'Marketing']
display(filtered_df)

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 32,45],
        'Score': [85, 90, 78]}
df = pd.DataFrame(data)

# Filter rows where Age > 30 and select only 'Name' and 'Score' columns
filtered_df = df.loc[df['Age'] > 30, ['Name', 'Score']]
print(filtered_df)

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 32,45],
        'Score': [85, 90, 78]}
df = pd.DataFrame(data)

# Filter rows where Age is either 25 or 45
filtered_df = df[df['Age'].isin([25, 45])]
print(filtered_df)

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 32,45],
        'Score': [85, 90, 78]}
df = pd.DataFrame(data)

# Filter using query method where Age > 30 and Score < 90
filtered_df = df.query('Age > 30 and Score < 90')
print(filtered_df)
