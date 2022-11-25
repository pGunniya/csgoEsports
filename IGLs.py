import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import nan
from matplotlib.patches import PathPatch
import scipy as scipy
from scipy import stats


df = pd.read_excel("Are IGLs Bad.xlsx")
#print(df)

#plt.hist(df['Rating2.0'])
#plt.show()
x = df['Just Awps'].mean()
y = df["Just IGL's"].mean()
z = df['Everyone else'].mean()
t = df['Rating Percentiles'].mean()
ratings = [t, x, y, z]
#print(ratings)

a = df['Just Awps raw'].mean()
b = df["Just IGL's raw"].mean()
c = df['Everyone else raw'].mean()
d = df['Rating2.0'].mean()
ratingsRaw = [d,a,b,c]
#print(ratingsRaw)

#plt.hist(x = df['Rating2.0'])
#plt.show()

#plt.violinplot(df["Rating2.0"])
#plt.show()



# Converting df column values to numpy array
igl = df["Just IGL's raw"]
igl2 = igl.values
igl3 = igl2[np.logical_not(np.isnan(igl2))]

awp = df['Just Awps raw']
awp2 = awp.values
awp3 = awp2[np.logical_not(np.isnan(awp2))]

rifle = df['Everyone else raw']
rifle2 = rifle.values
rifle3 = rifle2[np.logical_not(np.isnan(rifle2))]



print(rifle.describe())



#Violinplots on the same axes

fig, (ax1, ax2, ax3) = plt.subplots(nrows = 1, 
                               ncols = 3,
                               figsize =(9, 4),
                               sharey = True)
  
ax1.set_ylabel('HLTV 2.0 Rating')

ax1.set_title('Riflers')
ax1.violinplot(rifle3, showmedians = True, showextrema = True)
line25 = ax1.axhline(y = .92, color = "red")
line75 = ax1.axhline(y = 1.115, color = "green")
patch = PathPatch(ax1.collections[0].get_paths()[0], transform=ax1.transData)
line25.set_clip_path(patch) # clip the line by the form of the violin
line75.set_clip_path(patch)
  
ax2.set_title('In Game Leaders')
ax2.violinplot(igl3, showmedians = True, showextrema = True)
line25 = ax2.axhline(y = .887, color = "red")
line75 = ax2.axhline(y = 1.01, color = "green")
patch = PathPatch(ax2.collections[0].get_paths()[0], transform=ax2.transData)
line25.set_clip_path(patch) # clip the line by the form of the violin
line75.set_clip_path(patch)

ax3.set_title('Awps')
ax3.violinplot(awp3, showmedians = True, showextrema = True)
line25 = ax3.axhline(y = .955, color = "red")
line75 = ax3.axhline(y = 1.115, color = "green")
patch = PathPatch(ax3.collections[0].get_paths()[0], transform=ax3.transData)
line25.set_clip_path(patch) # clip the line by the form of the violin
line75.set_clip_path(patch)

# Function to show the plot
plt.show()


fig2, (ax11, ax22, ax33) = plt.subplots(nrows = 3, 
                               ncols = 1,
                               figsize =(9, 4), sharex = True )

ax11.set_title('Riflers')
ax11.hist(x = rifle3)

ax22.set_title("Igl's")
ax22.hist(x = igl3)

ax33.set_title('Awps')
ax33.hist(x = awp3)

plt.show()

standardDeviations = [rifle3.std(), igl3.std(), awp3.std()]


print(scipy.stats.ttest_ind(a = rifle3, b = igl3, equal_var = False))
print(scipy.stats.ttest_ind(a = rifle3, b = awp3, equal_var = False))
print(scipy.stats.ttest_ind(a = igl3, b = awp3, equal_var = False))