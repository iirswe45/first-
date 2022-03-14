#!/bin/bash

set -e

#mpirun -n 16 /usr/bin/lmp_stable -in in.1 # Run 10,000 steps of soft potential A=1 

#mpirun -n 16 /usr/bin/lmp_stable -in in.2 # Run 10,000 steps of soft potential A= 5

#mpirun -n 16 /usr/bin/lmp_stable -in in.3 # Run 10,000 steps of soft potential A= 10

#mpirun -n 16 /usr/bin/lmp_stable -in in.4 # Run 10,000 steps of soft potential A= 30

#mpirun -n 16 /usr/bin/lmp_stable -in in.5 # Run 100,000 steps of LJ, NVE, Langevin

#mpirun -n 16 /usr/bin/lmp_stable -in in.6 > in.6.log  # Run 100,000 steps of NPT

# mpirun -n 16 /usr/bin/lmp_stable -in in.7 > log.7

#mpirun -n 12 /usr/bin/lmp_stable -in in.9

#mpirun -n 12 /usr/bin/lmp_stable -in in.10

mpirun -n 16 /usr/bin/lmp_stable -in in.11
#~/.local/bin/lmp -sf gpu -pk gpu 1 -in in.11

#mpirun -n 16 /usr/bin/lmp_stable -in in.12              #Change temperature 
#~/.local/bin/lmp -sf gpu -pk gpu 0 -in in.12

#mpirun -n 12 /usr/bin/lmp_stable -sf gpu -pk gpu 1 -in in.11 #Run for NPT
#lmp_machine -sf gpu -pk gpu 1 -in in.script 
#mpirun -n 12 /usr/bin/lmp_stable -in in.12               #gpu Change temperature 
