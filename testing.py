import pandas as pd
import numpy as np
import re
from matplotlib import pyplot as plt
from plotly.offline import plot
import plotly.graph_objs as go

df = pd.read_csv('naturalDisaster.csv')
df.drop(['Extreme temperature','Mass movement (dry)','Volcanic activity','Drought'], axis = 1, inplace = True)
df = df[df["Country"].str.contains("income")==False]
df['Flood'] = pd.to_numeric(df['Flood'],errors='coerce')
df = df.replace(np.nan, 0)
df= df[df['Flood'] > 150]
df
x = df['Country']
y = df['Flood']

plt.xlabel('Country')
plt.ylabel('Flood')
plt.bar(x,y)
plt.show()