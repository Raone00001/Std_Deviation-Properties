# Import all modules
import plotly.figure_factory as ff
import statistics
import random

# Array
dice_result = []

# Loop for repeating the dice values and appeding them
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)

# Finding the mean, median, mode, and standard deviation
# Normal distribution, the 3 M(s) will always be close to each other (peak of the bell curve).
# No matter how many times the data is itterated, the probability/chances of the data occuring stays the same.
mean = sum(dice_result)/len(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)
std_deviation = statistics.stdev(dice_result)

# Calculate first and end std deviation
first_std_deviation_start,first_std_deviation_end = mean-std_deviation,mean+std_deviation

# Var to find list
list_of_data_within_one_std_deviation = (result for result in dice_result if first_std_deviation_start < first_std_deviation_end)

# Print
print("Mean: ",mean)
print("Median: ",median)
print("Mode: ",mode)
print("Std-Deviation: ",std_deviation)
print("Standard Deviation: ".format(len(list_of_data_within_one_std_deviation)*100.0/len(dice_result)))