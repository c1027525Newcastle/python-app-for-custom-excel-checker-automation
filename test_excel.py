import pandas as pd

df = pd.read_excel('Audit_Checker.xlsx')

print("All data:")
print(df)

print("\nFilter by role == Engineer:\n")
print(df[df['Roles'] == 'Engineer, Cool_Kids'])