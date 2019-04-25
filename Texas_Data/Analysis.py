import matplotlib.pyplot as plt
import pandas as pd
import numpy
import sys
import os

# takes csv into dataframe > numpy ndarray
data = pd.read_csv(sys.argv[1], header=None)
data = data.values

# subplot 1
plt.subplot(2, 2, 1, title='Test')
plt.plot(data[:, 0], data[:, 1])
plt.title('List 1 line vs time')

# subplot 2
plt.subplot(2, 2, 4, title='Test')
plt.plot(data[:, 2], data[:, 1])
plt.title('List 2 line vs time')

plt.savefig(sys.argv[2])

