import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#
def get_frequencies(nums):
    freqs_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for num in nums:
        if not pd.isna(num):
            freqs_list[num] += 1
    freqs_df = pd.DataFrame(freqs_list, index=range(0, 10), columns=['freq'])

    return freqs_df


# returns the first digit after the decimal point
def first_after_decimal(num):
    # if (abs(num) < 1):
    #     return int((abs(num) * 10) % 10)
    if pd.isna(num):
        return
    return int((abs(float(num)) * 10) % 10)


def first_digit(num):
    if pd.isna(num):
        return
    if float(num) == 0:
        return
    num= num * 1000000
    return int(str(abs(num))[0])


files = ['74.csv', '73.csv', '65_protein_PMSI_normalized.csv', '65_peptide_PMSI_normalized.csv', '68.csv', '60_T4.csv',
         '22.csv', '59_raw.csv', '65_protein_water_normalized.csv', '14.csv', '28.csv', '36.csv', '1.csv', '48.csv',
         '65_peptide_water_raw.csv', '47.csv', '65_protein_PMSI_raw.csv', '51.csv', '35.csv', '72.csv', '53.csv',
         '65_protein_water_raw.csv', '54.csv', '34.csv', '32_LETTER.csv', '63.csv', '50.csv', '60_T3.csv',
         '43.csv', '65_peptide_PMSI_raw.csv', '49.csv', '70.csv', '66.csv', '11.csv', '58.csv', '56_raw.csv', '25.csv',
         '71.csv', '67.csv', '5.csv', '65_peptide_water_normalized.csv']

df2 = pd.DataFrame(index=range(0, 10))
first = True

for file in files:
    data = pd.read_csv(f"Data/{file}", na_values=['-', 'ND'], header=[0])
    last_digits = []  #
    last_digit_dict = {}
    last_digit_freq = {}

    for column in data:
        nums = data[column]
        # last_digit = [first_after_decimal(num) for num in nums]
        last_digit = [first_digit(num) for num in nums]
        last_digits += last_digit
        last_digit_dict[column] = last_digit

    df1 = get_frequencies(last_digits)

    for key in last_digit_dict.keys():
        frequencies = get_frequencies(last_digit_dict[key])
        frequencies['Percentage'] = frequencies['freq'] / sum(frequencies['freq']) * 100
        last_digit_freq[key] = frequencies
        message = (f"{key}"
                   f"{frequencies}"
                   f"")
        print(message)

    df1['Percentage'] = df1['freq'] / sum(df1['freq']) * 100

    df2[file] = df1['freq'] / sum(df1['freq']) * 100

transposed = df2.transpose()[1:].copy()
plt.boxplot(transposed, sym="r.", medianprops=dict(color="black"))
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
plt.ylabel("Frequency (percentage)")
plt.xlabel("Digit")
plt.title("Digit frequency of first number")
plt.show()
