import csv
import pandas as pd
import plotly.figure_factory as pff
import statistics

df = pd.read_csv('HeightWeight.csv')
weight_list = df['Weight(Pounds)'].to_list()

weight_mean = statistics.mean(weight_list)
weight_median = statistics.median(weight_list)
weight_mode = statistics.mode(weight_list)

print(f'Mean is: {weight_mean}')
print(f'Median is: {weight_median}')
print(f'Mode is: {weight_mode}')
