
#1 LOAD DATA FRAME
#2 NUMBER OF PATIENTS AND HEALTHY
#3 PERCENTAGE OF PATIENTS AMONG MAN / WOMAN
#4 COPIES (200<CHOLESTEROL) IN THE NEW DATA FRAME AND IDENTITY THE PERCENTAGE OF PATIENTS AMONG THEM
#5 COPIES (200<CHOLESTEROL AND 48<AGE) IN THE NEW DATA FRAME AND IDENTITY THE PERCENTAGE OF PATIENTS AMONG THEM
#6 VAR, MIN, MAX, AVG, Q1, Q2 & Q3 FOR HEART RATE ATTRIBUTE
#7 NUMBER OF NULLS IN EACH COLUMN

import pandas as pd
import os

current_dir = os.getcwd()
#df = pd.read_csv(f'{current_dir}/pandas/Individuals.csv')
df = pd.read_csv('Individuals.csv')

print("#1 LOAD DATA FRAME:")
print(df)

print("\n\n#2 SICK AND HEALTHY COUNT:")
patient = len(list(filter(lambda x: x == 1 ,df.C)))
healthy = len(df.C) - patient
print("SICK: %i\nHEALTHY: %i" % (patient, healthy))

print("\n\n#3 PERCENTAGE OF SICK'S AMONG MEN / WOMEN:")
mans_num = len(list(filter(lambda x: x == 1, df.Sex)))
womans_num = len(df.index) - mans_num
sick_mans = 0
sick_womans = 0
for i in range(len(df.index)):
    if df.Sex[i] == 1 and df.C[i] == 1:
        sick_mans += 1
    elif df.Sex[i] == 0 and df.C[i] == 1:
        sick_womans += 1

print("{:>5.2f} % OF MEN ARE SICK\n{:>5.2f} % OF WOMEN ARE SICK".format(sick_mans * 100 / mans_num, sick_womans * 100 / womans_num))

print("\n\n#4 NEW DF FOR (CHOLESTORAL > 200) AND PERCENTAGE OF SICK'S:")
dict1 = {'Colestoral': []}
a = 0
for i in range(len(df.index)):
    if df.Cholestoral[i] > 200:
        dict1["Colestoral"].append(df.Cholestoral[i])
    if df.Cholestoral[i] > 200 and df.C[i] == 1:
        a += 1

df1 = pd.DataFrame(dict1)
print("{}\n{:>5.2f} % OF PERSON'S ARE SICK".format(df1, a * 100 / len(df1.index)))

print("\n\n#5 NEW DF FOR (CHOLESTORAL > 200 & AGE > 48) AND PERCENTAGE OF SICK'S:")
dict2 = {'Colestoral': [], 'Age': []}
b = 0
for i in range(len(df.index)):
    if df.Cholestoral[i] > 200 and df.Age[i] > 48:
        dict2["Colestoral"].append(df.Cholestoral[i])
        dict2["Age"].append(df.Age[i])
    if df.Cholestoral[i] > 200 and df.Age[i] > 48 and df.C[i] == 1:
        b += 1

df2 = pd.DataFrame(dict2)
print("{}\n{:>5.2f} % OF PERSON'S ARE SICK".format(df2, b * 100 / len(df2.index)))

print("\n\n#6 VAR, MIN, MAX, AVG, Q1, Q2 & Q3 FOR HEART RATE COLUMN:")
print("var    {:>10.5f}\n{}".format(df.var()['Heart_rate'], df["Heart_rate"].describe()[["min","max","mean","25%","50%","75%"]]))

print("\n\n#7 NULL COUNT IN EACH COLUMNS:")
print(df.isnull().sum())
print(f'ALL NULL: {df.isna().sum().sum()}')
