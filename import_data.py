
import numpy as np

file_name = '/mnt/Storage/dump.5'
with open(file_name) as f:
    lines = f.readlines()

timestep_flag = False
num_atoms_flag = False
box_flag = False
atom_flag = False

data = []

for count, line in enumerate(lines):
    elements = len(line.split())
    skip = False
    if elements > 1:
        if line.split()[1] == 'TIMESTEP': 
            timestep_flag = True
            skip = True

        if line.split()[1] == 'NUMBER': 
            num_atoms_flag = True
            skip = True
        
        if line.split()[1] == 'BOX': 
            box_flag = True
            skip = True
            future_lines = 0

        if line.split()[1] == 'ATOMS': 
            atom_flag = True
            skip = True
            future_lines = 0

    if timestep_flag and not skip: 
        data.append({"timestep": int(line.split()[0]), "num_atoms": None,  "box_bound": [], "atoms": None})
        timestep_flag = False

    if num_atoms_flag and not skip: 
        data[-1]["num_atoms"] = int(line.split()[0])
        num_atoms_flag = False

    if box_flag and not skip:
        if future_lines < 3:
            data[-1]["box_bound"].append([float(line.split()[0]), float(line.split()[1])])
            future_lines += 1
        if future_lines == 3:
            box_flag = False

    if atom_flag and not skip:
        if future_lines == 0:
            data[-1]["atoms"] = np.zeros((data[-1]["num_atoms"], 9))

        if future_lines < data[-1]["num_atoms"]:
            
            data[-1]["atoms"][future_lines,:] = np.array(
                [
                int(line.split()[0]),
                int(line.split()[1]),
                int(line.split()[2]),
                float(line.split()[3]),
                float(line.split()[4]),
                float(line.split()[5]),
                int(line.split()[6]),
                int(line.split()[7]),
                int(line.split()[8])
                ]
            )

            future_lines += 1
        
        if future_lines >= data[-1]["num_atoms"]:
            data[-1]["atoms"] = data[-1]["atoms"][data[-1]["atoms"][:,0].argsort()]
            #data[-1]["atoms"] = np.array(data[-1]["atoms"])
            atom_flag = False  
print(data[-1])
np.save("dump.5.npy", data, allow_pickle=True)
print("saved")