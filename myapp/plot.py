import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["Name", "Marks"]
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv")
display(df)
xaxis=df['AAPL_x']
yaxis=df['AAPL_y']
x=list(xaxis)
y=list(yaxis)
plt.plot(x, y)
plt.show()