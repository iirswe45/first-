import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import math

data = np.load("dump.11.npy", allow_pickle=True)

num_steps = len(data)
num_mol = np.amax(data[0]["atoms"][:,2]) # zeroth time step, all, mol id.
print("number of molecules in sim box: ",num_mol)
num_monomer = np.amax(data[0]["atoms"][:,0]) / num_mol
print("number of monomer per chain", num_monomer)

start_bead = 22 # beads you want to measure MSD
end_bead = 26
num_beads = end_bead - start_bead +1
monomers = 50 # total number of monomers per chain

inc_atoms = np.linspace(start_bead,end_bead,num=num_beads)
for ind in range(1,15): # loop through chains not monomers
    inc_atoms = np.append(inc_atoms, np.linspace(start_bead,end_bead, num=num_beads)+monomers*ind)

print(inc_atoms)

x0 = data[0]["atoms"][inc_atoms.astype(int),9]        # + 2*data[0]["box_bound"][0][1]*data[0]["atoms"][:,6]
y0 = data[0]["atoms"][inc_atoms.astype(int),10]       # + 2*data[0]["box_bound"][1][1]*data[0]["atoms"][:,7]
z0 = data[0]["atoms"][inc_atoms.astype(int),11]       # + 2*data[0]["box_bound"][1][1]*data[0]["atoms"][:,8]
t0 = data[0]["timestep"]
msdX = []
msdY = []
msdZ = []
dt = []

for i in range(1, len(data)): # calculate Rg for the first chain
    dt.append(data[i]["timestep"] - data[0]["timestep"])
    x = data[i]["atoms"][inc_atoms.astype(int),9]           # + 2*data[i]["box_bound"][0][1]*data[i]["atoms"][:,6]
    y = data[i]["atoms"][inc_atoms.astype(int),10]          # + 2*data[i]["box_bound"][1][1]*data[i]["atoms"][:,7]
    z = data[i]["atoms"][inc_atoms.astype(int),11]          # + 2*data[i]["box_bound"][2][1]*data[i]["atoms"][:,8]
    msdX.append(np.mean(np.abs(x - x0)**2))
    msdY.append(np.mean(np.abs(y - y0)**2))
    msdZ.append(np.mean(np.abs(z - z0)**2))

msdX = np.array(msdX)
msdY = np.array(msdY)
msdZ = np.array(msdZ)


MSD = np.add(msdX, msdY, msdZ)

np.savetxt("MSD.11.dat", np.transpose([dt, MSD]), delimiter=' ', newline='\n') # Change the file name saved here


fig = plt.figure()
plt.loglog(dt,MSD)
plt.xlabel('time lag [lj time]')
plt.ylabel('MSD [lj]')
plt.grid(axis = 'y')
plt.grid(axis = 'x')
plt.show()
    
