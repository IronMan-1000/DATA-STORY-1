import pandas as pd
import statistics
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("savings_data.csv")

import csv

with open('savings_data_final.csv',newline="") as f:
  reader = csv.reader(f)
  savings_data = list(reader)
  savings_data.pop(0)

total_entries = len(savings_data)
total_people_given_reminder = 0
for data in savings_data:
  if int(data[3]) == 1:
    total_people_given_reminder += 1


fig = go.Figure(go.Bar(x=["Reminded", "Not Reminded"], y=[total_people_given_reminder, (total_entries - total_people_given_reminder)]))

fig.show()

all_savings=[]
for data in savings_data:
    all_savings.append(float(data[0]))
print(f"Mean of savings - {statistics.mean(all_savings)}")
print(f"Median of savings - {statistics.median(all_savings)}")
print(f"Mode of savings - {statistics.mode(all_savings)}")

reminded_savings = []
not_reminded_savings = []
for data in savings_data:
    if int(data[3])== 1:
        reminded_savings.append(float(data[0]))
    else:
        not_reminded_savings.append(float(data[0]))

print("Results for people who were reminded to save")
print(f"Mean of savings - {statistics.mean(reminded_savings)}")
print(f"Median of savings - {statistics.median(reminded_savings)}")
print(f"Mode of savings - {statistics.mode(reminded_savings)}")

print("\n\n")
print("Results for people who were not reminded to save")
print(f"Mean of savings - {statistics.mean(not_reminded_savings)}")
print(f"Median of savings - {statistics.median(not_reminded_savings)}")
print(f"Mode of savings - {statistics.mode(not_reminded_savings)}")