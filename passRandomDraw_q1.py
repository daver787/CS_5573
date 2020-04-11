#passRandomDraw_q1.py
#Rewrite the first example of code "passRandomDraw.py"so that it passes a n*1
#vector of random draws from one process to the other. For practice,write it so
#that the user inputs at execution the value of n on the command-line (similar to
#the code developed in this section for the trapezoid rule.)
import numpy
from mpi4py import MPI
import sys

comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()

n=int(sys.argv[1])

randNums=numpy.zeros((n,1))

if rank==1:
	randNums=numpy.random.random_sample((n,1))
	print("Process",rank,"drew the numbers",randNums)
	comm.Send(randNums,dest=0)

if rank==0:
    print("Process",rank,"before receiving has the numbers",randNums)
    comm.Recv(randNums,source=1)
    print("Process",rank,"receieved the numbers",randNums)