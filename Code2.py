# Import all modules
import plotly.figure_factory as ff
import pandas as pd
import statistics
import csv

# Read the csv file
df = pd.read_csv("data.csv")

# Find height and convert to list
height_list = df["Height(Inches)"].tolist()

# Mean for height
height_mean = statistics.mean(height_list)

# Median for height
height_median = statistics.median(height_list)

# Mode for height
height_mode = statistics.mode(height_list)

# Print
print("Mean, Median, and Mode of Height is {}, {}, and {} respectively".format(height_mean,height_median,height_mode))

# Standard Deviation for height
height_std_deviation = statistics.stdev(height_list)

# First, Second, and Third Deviation
height_first_std_deviation_start, height_first_std_deviation_end = height_mean-height_std_deviation, height_mean+height_std_deviation
height_second_std_deviation_start, height_second_std_deviation_end = height_mean-(2*height_std_deviation), height_mean+(2*height_std_deviation)
height_third_std_deviation_start, height_third_std_deviation_end = height_mean-(3*height_std_deviation), height_mean+(3*height_std_deviation)

# Percentage of the std_d 1, 2, and 3
height_list_of_data_within_1_std_deviation = [result for result in height_list if result > height_first_std_deviation_start and result < height_first_std_deviation_end]
height_list_of_data_within_2_std_deviation = [result for result in height_list if result > height_second_std_deviation_start and result < height_second_std_deviation_end]
height_list_of_data_within_3_std_deviation = [result for result in height_list if result > height_third_std_deviation_start and result < height_third_std_deviation_end]

# Print
print("{}% of data for height lies within one standard deviation".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within two standard deviation".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within three standard deviation".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(height_list)))