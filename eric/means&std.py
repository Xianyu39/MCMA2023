import pandas as pd
file_path = 'Problem_C_Data_Wordle.xlsx'
df = pd.read_excel('Problem_C_Data_Wordle.xlsx')

means = []

for i in range(355):
    row_data = df.iloc[i, 6:13]
    sum = row_data[0]*1 + row_data[1]*2 + row_data[2]*3 + row_data[3]*4 + row_data[4]*5 + row_data[5]*6 + row_data[6]*7
    ave = sum/100
    means.append(ave)

results_column = 'Means'
df[results_column] = means
with pd.ExcelWriter(file_path) as writer:
    df.to_excel(writer, index=False)