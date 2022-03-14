import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import math

#def correct

data = np.load("dump.12.npy", allow_pickle=True)

##### Calculate radius of gyration ##########
print("starting Rg calc")
rg2 = []
print(data[0]["atoms"][:,0])
num_mol = np.amax(data[0]["atoms"][:,2]) # zeroth time step, all, mol id.
print("number of molecules in sim box: ",num_mol)
num_monomer = np.amax(data[0]["atoms"][:,0]) / num_mol
print("number of monomer per chain", num_monomer)

plot = False #True

x = []
y = []
z = []

rIJ2_tot = np.zeros((len(data),int(num_mol)))
rIJ_tot = np.zeros((len(data),int(num_mol)))

num_mono=87
num_chain=230

start_index = range(0, num_mono*num_chain-1, num_mono)
nstep = []
# print(start_index)
for mol_num, index in enumerate(start_index): 
    print(index)
    for i in range(len(data)): # calculate Rg for the first chain
        #if index <= 8613:
        x = data[i]["atoms"][index:index+num_mono,9]  #+ data[i]["box_bound"][0][1]*data[i]["atoms"][index:index+30,6]
        y = data[i]["atoms"][index:index+num_mono,10] # + data[i]["box_bound"][1][1]*data[i]["atoms"][index:index+30,7]
        z = data[i]["atoms"][index:index+num_mono,11] # + data[i]["box_bound"][2][1]*data[i]["atoms"][index:index+30,8]
        if plot:
            fig = plt.figure()
            ax = plt.axes(projection='3d')
            ax.scatter(x, y, z, 'gray')
            ax.plot3D(x,y,z)
            plt.show()

        X1, X2 = np.meshgrid(x, x)
        Y1, Y2 = np.meshgrid(y, y)
        Z1, Z2 = np.meshgrid(z, z)
        rIJ2 = (X1-X2)**2 + (Y1-Y2)**2 + (Z1-Z2)**2
        rIJ2_sum = np.sum(rIJ2)
        
        
        
        #for J in range(int(num_monomer)):
        #    for I in range(int(num_monomer)):
        #        rIJ2 = (x[I]-x[J])**2 + (y[I]-y[J])**2 + (z[I]-z[J])**2
        #        rIJ2_sum = rIJ2_sum + rIJ2
        
        rIJ2_tot[i,mol_num] = rIJ2_sum/(2 * num_monomer**2)
        rIJ_tot[i,mol_num] = math.sqrt(rIJ2_tot[i,mol_num])
        if index == 0:
            nstep.append(data[i]['timestep'])
        
np.savetxt('Rg_out.txt', rIJ_tot, delimiter=',')
np.savetxt('nstep.txt', nstep, delimiter=',')


#print(rIJ_tot)
#print(rIJ2_tot)
print(np.mean(rIJ_tot))

#print("x", data[0]["box_bound"][0][1]*data[i]["atoms"][0:180,6])
#print("y", data[0]["box_bound"][1][1]*data[i]["atoms"][0:180,7])
#print("z", data[0]["box_bound"][2][1]*data[i]["atoms"][0:180,8])

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(x, y, z,'o')
ax.plot3D(x,y,z)
plt.show()
