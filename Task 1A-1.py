import pandas as pd
import numpy as np
data = {
    'A': [1, 2, np.nan, 4, 5, np.nan, 7],
    'B': [np.nan, 2, 3, 4, np.nan, 6, 7],
    'C': ['foo', 'bar', 'baz', np.nan, 'qux', 'quux', 'corge'],
    'D': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
missing_data = df.isna()
print("\nMissing Data in DataFrame:")
print(missing_data)
df_dropna_rows = df.dropna()
print("\nDataFrame after dropping rows with any missing data:")
print(df_dropna_rows)
df_dropna_cols = df.dropna(axis=1)
print("\nDataFrame after dropping columns with any missing data:")
print(df_dropna_cols)
df_fillna = df.fillna(value={'A': df['A'].mean(), 'B': df['B'].mean(), 'C': 'missing', 'D': 0})
print("\nDataFrame after filling missing data:")
print(df_fillna)
df_with_duplicates = df.append(df.iloc[2], ignore_index=True)
print("\nDataFrame with Duplicates:")
print(df_with_duplicates)
duplicates = df_with_duplicates.duplicated()
print("\nDuplicates in DataFrame:")
print(duplicates)
df_no_duplicates = df_with_duplicates.drop_duplicates()
print("\nDataFrame after removing duplicates:")
print(df_no_duplicates)
