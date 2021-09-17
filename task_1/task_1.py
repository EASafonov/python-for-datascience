import numpy as np


table = 'bankTestReport.csv'
data = np.loadtxt(table, delimiter=';', skiprows=1)
rows, cols = data.shape
ones_array = np.eye(cols, rows)
mult_array = np.dot(data, ones_array)
np.savetxt('result.csv', mult_array, delimiter=';')
