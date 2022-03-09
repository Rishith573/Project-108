import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("data.csv")

fig1 = ff.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"])
fig1.show()