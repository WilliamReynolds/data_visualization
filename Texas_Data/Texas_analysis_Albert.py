import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import os
import openpyxl
import xlrd


# open the texas spreadsheet and pull the sheet. 

#wb = openpyxl.load_workbook(sys.argv[1])
#sheets = wb.sheetnames()

# pandas to open excel and save csv
df_alb = pd.read_excel(sys.argv[1],sheet_name='Albert_Volumes')
#df_gm = pd.read_excel(sys.argv[1],sheet_name='Albert_GM_Volumes')
df_str = pd.read_excel(sys.argv[1],sheet_name='Structure_Threshold_Volumes')

# pair down df only data to graph
structures = [ 'SubjectID', 'Hippocampus_left', 'Hippocampus_right', 'Amygdala_left', 'Amygdala_right', 'Cerebellum_left', 'Cerebellum_right' ] 

df_manedits = df_alb[structures]

#remove nan
df_alb_nan = df_alb.replace('.', np.NaN)
df_alb_nonan = df_alb_nan.dropna()

# converts df into numpy array
np_alb_nonan = df_alb_nonan.values

# subplot 1
plt.subplot(3, 2, 1, title=structures[1])
plt.violinplot(np_alb_nonan[:, 1])

# subplot 2
plt.subplot(3, 2, 2, title=structures[2])
plt.violinplot(np_alb_nonan[:, 2])

# subplot 3
plt.subplot(3, 2, 3, title=structures[3])
plt.violinplot(np_alb_nonan[:, 3])

# subplot 4
plt.subplot(3, 2, 4, title=structures[4])
plt.violinplot(np_alb_nonan[:, 4])

# subplot 5
plt.subplot(3, 2, 5, title=structures[5])
plt.violinplot(np_alb_nonan[:, 5])

# subplot 6
plt.subplot(3, 2, 6, title=structures[6])
plt.violinplot(np_alb_nonan[:, 6])

print (np_alb_nonan)
print (np_alb_nonan[:,1])

plt.savefig(sys.argv[2])

