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


files = ["1.csv", "5.csv", "11.csv",   "22.csv", "28.csv", "32_LETTER.csv", "34.csv", "35.csv", "36.csv", "47.csv",
         "49.csv", "50.csv", "51.csv", "53.csv", "54.csv"]
df2 = None
first = True

for file in files:
    data = pd.read_csv(f"Data/{file}", na_values=['-', 'ND'], header=[0])
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
        #print(message)

        df1.columns = ['Element', 'Frequency']
    df1['Percentage'] = df1['Frequency'] / sum(df1['Frequency']) * 100
    if first:
        df2 = df1[['Element', 'Percentage']].copy()
        df2.rename(columns={'Percentage': file}, inplace=True)
        first = False
    else:
        df2[file] = df1['Frequency'] / sum(df1['Frequency']) * 100


transposed = df2.transpose()[1:].copy()
plt.boxplot(transposed, sym="r.", medianprops=dict(color="black"))
plt.xticks([1,2,3,4,5,6,7,8,9, 10], [0,1,2,3,4,5,6,7,8,9])
plt.ylabel("Frequency (percentage)")
plt.xlabel("Digit")
plt.title("Digit frequency of first number after decimal")
plt.show()