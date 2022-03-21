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
    if float(num) == 0:
        return
    num = num * 10000
    return int(str(abs(num))[0])


file = "Data/72.csv"
data = pd.read_csv(file, na_values=['-', 'ND'], header=[0])


last_digits = [] #
last_digit_dict = {}
last_digit_freq = {}

for column in data:
    nums = data[column]
    #last_digit = [first_after_decimal(num) for num in nums]
    last_digit = [first_digit(num) for num in nums]
    last_digits += last_digit
    last_digit_dict[column] = last_digit


df1 = get_frequencies(last_digits)


col_freq = pd.DataFrame(index=range(0, 10))


for key in last_digit_dict.keys():
    frequencies = get_frequencies(last_digit_dict[key])
    frequencies['Percentage'] = frequencies['freq'] / sum(frequencies['freq']) * 100
    last_digit_freq[key] = frequencies
    col_freq[key] = frequencies['Percentage']
    message = (f"{key}"
    f"{frequencies}"
    f"")
    print(message)



df1['Percentage'] = df1['freq'] / sum(df1['freq']) * 100

transposed = col_freq.transpose()[1:].copy()
plt.boxplot(transposed, sym="r.", medianprops=dict(color="black"))
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
plt.ylabel("Frequency (percentage)")
plt.xlabel("Digit")
plt.title("Digit frequency of first number")
plt.show()


