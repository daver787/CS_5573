#passRandomDraw_q1.py
#Try modifying some of the parameters in comm.Send and comm.Recv in the code from
#the previous exercise(dest,source,and tag). What happens to the program?
#Does it hang or crash? What do you suppose the tag parameter does?
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

#tags make sure if multiple messages are passed between nodes they can be
#able to be distinguished

#any mismatch between tags causes the program to hang
#a mismatch or no source or dest parameter also causes program to hang     