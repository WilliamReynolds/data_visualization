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


# make plots. 
fs = 10
pos = [1, 2, 3, 4, 5, 6]
points = 200
options = 'points=200, widths=0.3, showmeans=True, showextrema=True, showmedians=True'

fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(6, 6))

# plot 1 
#axes[0, 0].violinplot(np_alb_nonan[:,1], pos, points=50, widths=0.3, showmeans=True, showextrama=True, showmedians=True)
axes[0, 0].violinplot(np_alb_nonan[:,1], pos, options)
axes[0, 0].set_title(structures[1], fontsize=fs) 

# plot 2
axes[0, 1].violinplot(np_alb_nonan[:,1], pos, options)
axes[0, 1].set_title(structures[1], fontsize=fs) 

# plot 3
axes[1, 0].violinplot(np_alb_nonan[:,1], pos, options)
axes[1, 0].set_title(structures[1], fontsize=fs) 

# plot 4
axes[1, 1].violinplot(np_alb_nonan[:,1], pos, options)
axes[1, 1].set_title(structures[1], fontsize=fs) 

# plot 5
axes[2, 0].violinplot(np_alb_nonan[:,1], pos, options)
axes[2, 0].set_title(structures[1], fontsize=fs) 

# plot 6
axes[2, 1].violinplot(np_alb_nonan[:,1], pos, options)
axes[2, 1].set_title(structures[1], fontsize=fs) 

plt.show()
"""
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
"""
