
import csv
import pandas as pd

#Read the txt file
data = []
with open('s1dataset.txt', newline='') as file:
    s1_data = csv.reader(file, delimiter=' ')
    for row in s1_data:
        data.append(row)  #alamcenamos cada fila en la lista data

#Convert the data to a pandas dataframe
df = pd.DataFrame(data)
print(list(df))

df.columns = [
    "Number of STAs",
    "Load",
    "Size(x)",
    "Size(y)",
    "Area",
    "Contention window",
    "Channel width",
    "Packet size",
    "Max RSSI",
    "Avg RSSI",
    "Min RSSI",
    "Avg Probability of failure",
    "Throughput",
    "Average delay",
    "Total airtime",
    "Proportional airtime"
]


