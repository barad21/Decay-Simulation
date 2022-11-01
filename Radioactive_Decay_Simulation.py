#%% Author and Date Information:
"""
Created on Wed Oct 26 11:29:12 2022

@author: 1bora
"""

#%% Libraries: 

import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


#%% Radioactive Decay Simulation:

time = np.arange(0,10,0.001)

Q_0 = 10

k_list = [0.5, 1.5]

Mass = []


for k in k_list:
    
    Mass_temp = []
    
    for t in time:
        
        Q = Q_0*math.e**(-k*t)
        
        Mass_temp.append(Q)
    
    Mass.append(Mass_temp)


plt.figure("Radioactive Decay Simulation", dpi= 1000, figsize=(10,8))


fig, axs = plt.subplots(dpi=1000, figsize=(10,8))
axs.set_facecolor("gray")

for m in Mass:
    
    plt.scatter(x=time, y=m)

orange_patch = mpatches.Patch(color="tab:orange", label='k = 1.5')
blue_patch = mpatches.Patch(color="tab:blue", label= "k= 0.5")

plt.legend(handles=[orange_patch, blue_patch], fontsize= 18)

plt.xticks(np.arange(0,11,1), np.arange(0,11,1), fontsize= 12)
plt.yticks(np.arange(0,11,1), np.arange(0,11,1), fontsize= 12)

plt.grid(True)

plt.title("Radioactive Decay Simulation \n Mass (kg) vs. Time (s)", fontsize=25)

plt.ylabel("Mass (kg)", fontsize=18)
plt.xlabel("Time (s)", fontsize=18)


plt.savefig("Radioactive_Decay_Simulation.jpeg", dpi= 1000)


