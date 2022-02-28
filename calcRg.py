import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import math

#def correct

data = np.load("dump.5.npy", allow_pickle=True)

##### Calculate radius of gyration ##########
print("starting Rg calc")
rg2 = []

num_mol = np.amax(data[0]["atoms"][:,2]) # zeroth time step, all, mol id.
print("number of molecules in sim box: ",num_mol)
num_monomer = np.amax(data[0]["atoms"][:,0]) / num_mol
print("number of monomer per chain", num_monomer)

x = []
y = []
z = []

rIJ2_tot = []
rIJ_tot = []

start_index = range(0, 399*180, 180)
# print(start_index)
for index in start_index: 
    print(index)
    for i in range(len(data)): # calculate Rg for the first chain
        x = data[i]["atoms"][index:index+180,3] + 2*data[i]["box_bound"][0][1]*data[i]["atoms"][index:index+180,6]
        y = data[i]["atoms"][index:index+180,4] + 2*data[i]["box_bound"][1][1]*data[i]["atoms"][index:index+180,7]
        z = data[i]["atoms"][index:index+180,5] + 2*data[i]["box_bound"][2][1]*data[i]["atoms"][index:index+180,8]

         rIJ2_sum = 0
         for J in range(int(num_monomer)):
             for I in range(int(num_monomer)):
                 rIJ2 = (x[I]-x[J])**2 + (y[I]-y[J])**2 + (z[I]-z[J])**2
                 rIJ2_sum = rIJ2_sum + rIJ2
        
         rIJ2_tot.append(rIJ2_sum/(2 * num_monomer**2))
         rIJ_tot.append(math.sqrt(rIJ2_tot[-1]))

print(rIJ_tot)
print(rIJ2_tot)
print(np.mean(rIJ_tot))

#print("x", data[0]["box_bound"][0][1]*data[i]["atoms"][0:180,6])
#print("y", data[0]["box_bound"][1][1]*data[i]["atoms"][0:180,7])
#print("z", data[0]["box_bound"][2][1]*data[i]["atoms"][0:180,8])

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(x, y, z, 'gray')
plt.show()