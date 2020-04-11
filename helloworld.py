#Name:David Espinola
#Date:04/03/2020
#helloworld.py
#Write thr "Hello World" program from class example so that every process
#prints out its rank and the size of the communicator(for example, process 3 on a
#communicator of size 5 print "Hello World from process 3 out of 5!").
import numpy
from mpi4py import MPI 
comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()

print("Hello from process",rank,"out of",size,"!")
