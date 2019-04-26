import matplotlib.pyplot as plt
import pandas as pd
import numpy
import sys
import os
import openpyxl
import xlrd


# open the texas spreadsheet and pull the sheet. 

wb = openpyxl.load_work(sys.argv[1])
sheets = openpyxl.wb.get_sheet_names()

# pandas to open excel and save csv
df_alb = pd.read_excel(sys.argv[1],sheet_name='Albert_Volumes')
df_gm = pd.read_excel(sys.argv[1],sheet_name='Albert_GM_Volumes')
df_str = pd.read_excel(sys.argv[1],sheet_name='Structure_Threshold_Volumes')

# pair down df only data to graph

structures = [ 'Hippocampus_left', 'Hippocampus_right', 'Amygdala_left', 'Amygdala_right', 'Cerebellum_left', 'Cerebellum_right' ] 



# converts df into numpy array
data_alb = df_alb.values
#data_gm = df_gm.values
#data_str = df_str.values

"""
# takes csv into dataframe > numpy ndarray

data = pd.read_csv()
data = data.values
"""

# subplot 1
plt.subplot(2, 2, 1, title='Test')
plt.plot(data[:, 0], data[:, 1])
plt.title('List 1 line vs time')

# subplot 2
plt.subplot(2, 2, 4, title='Test')
plt.plot(data[:, 2], data[:, 1])
plt.title('List 2 line vs time')

plt.savefig(sys.argv[3])

