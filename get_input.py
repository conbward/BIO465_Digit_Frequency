import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#returns the first digit after the decimal point
def first_after_decimal(num):
    # if (abs(num) < 1):
    #     return int((abs(num) * 10) % 10)
    if pd.isna(num):
        return
    return int((abs(float(num)) * 10) % 10)

def first_digit(num):
    if pd.isna(num):
        return
    return int(str(num)[0])


file = "Data/54.csv"
data = pd.read_csv(file, na_values=['-', 'ND'], header=[0])


last_digits = [] #
last_digit_dict = {}
last_digit_freq = {}

for column in data:
    nums = data[column]
    last_digit = [first_after_decimal(num) for num in nums]
    #last_digit = [first_digit(num) for num in nums]
    last_digits += last_digit
    last_digit_dict[column] = last_digit


df1 = pd.Series(last_digits).value_counts().sort_index().reset_index().reset_index(drop=True)


for key in last_digit_dict.keys():
    frequencies = pd.Series(last_digit_dict[key]).value_counts().sort_index().reset_index().reset_index(drop=True)
    frequencies.columns = ['Element', 'Frequency']
    frequencies['Percentage'] = frequencies['Frequency'] / sum(frequencies['Frequency']) * 100
    last_digit_freq[key] = frequencies
    message = (f"{key}"
    f"{frequencies}"
    f"")
    print(message)


df1.columns = ['Element', 'Frequency']
df1['Percentage'] = df1['Frequency'] / sum(df1['Frequency']) * 100

plt.bar(x = df1['Element'], height = df1['Percentage'])
plt.yticks(np.arange(0, 11, 1))
plt.show()

