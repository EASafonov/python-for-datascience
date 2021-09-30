import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

table = 'bankTestReport.csv'
df = pd.read_csv(table, sep=";")
rows, cols = df.shape
columns_names = df.columns.values.tolist()
print(columns_names)
df.drop(df.index, inplace=True)
df = pd.DataFrame(np.random.randint(0, 100, size=(rows, cols)), columns=columns_names)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df.age, df.duration, df.campaign, s=df.pdays)
plt.show()
