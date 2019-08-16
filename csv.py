#RUN IN TERMINAL

import sys, os, csv
input_file = r"/home/mnandala/PYTHON/RH_Assets_Threats_points_messy_July_2019.csv"
data1 = csv.reader(reader(open(input_file), delimiter =',')
    data = list(csv.reader(open(input_file), delimiter =','))

row1 = data[1]

for row in data
  for item in row
    item.strip()
#[item.strip() for row in data for item in row]

for row in data:
  for item in row:
    item.title()
#[item.title() for row in data for item in row]


new data = []
for row in data:
    newline = [item.strip() for item in row]
    newdata.append(newline)


newdata = []
for row in data:
    newline = [item.strip() for item in row]
    newline = [item.title() for item in newdata]
    newdata.append(newline)
