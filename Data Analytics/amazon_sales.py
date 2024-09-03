import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

data = pd.read_csv("C:/Users/shigoyal/Downloads/Amazon Sales data.csv")
data = pd.DataFrame(data= data)
print(data.size)
#print(data.columns)
# print(data.info)
#print(data.dtypes)

print(plt.figure(figsize=(10,20)))
print(sb.heatmap(data.isnull()))