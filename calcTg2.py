import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import math

#def correct

data = np.load("dump.12.npy", allow_pickle=True)

##### Calculate Tg ##########
print("starting Tg calc")
print(data[0]["atoms"][:,0])
num_mol = np.amax(data[0]["atoms"][:,2]) # zeroth time step, all, mol id.
print("number of molecules in sim box: ",num_mol)
num_monomer = np.amax(data[0]["atoms"][:,0]) / num_mol
print("number of monomer per chain", num_monomer)

vx = []
vy = []
vz = []
vol = []

for i in range(len(data)):
    vx = np.append(vx, np.mean(data[i]["atoms"][:,12]**2))
    vy = np.append(vy, np.mean(data[i]["atoms"][:,13]**2))
    vz = np.append(vz, np.mean(data[i]["atoms"][:,14]**2))
    #print(data[i]["box_bound"][1][1])
    vol = np.append(vol, np.power(2*data[i]["box_bound"][1][1],3))
    
    
vx = np.array(vx)
vy = np.array(vy)
vz = np.array(vz)
v = np.add(vx, vy, vz)
m=1
kb=1
T=1/2*m*1/kb*(v)
rho = m*len(data[0]["atoms"][:,1]) / vol
print(T)

fig = plt.figure()
plt.scatter(T,1/rho)
plt.xlabel('T')
plt.ylabel('rho')
#plt.grid(axis = 'y')
#plt.grid(axis = 'x')
plt.show()
np.savetxt("temp_rho.dat", np.transpose([T, rho]), delimiter=' ', newline='\n') # Change the file name saved here
