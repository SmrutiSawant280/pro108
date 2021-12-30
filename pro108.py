import scipy
import csv
import plotly.figure_factory as ff
import pandas as p
df = p.read_csv('C:/Users/DELL/Desktop/PRO97/ar.csv')
fig = ff.create_distplot([df['Avg Rating'].tolist()],["Avg Rating"],show_hist = False)
fig.show()