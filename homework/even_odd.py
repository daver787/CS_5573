#Name:David Espinola
#Date:04/03/2020
#even_odd.py
#Write a program in which the processes with even rank print "Hello" and process
#with odd rank print "Goodbye." Print the process number along with the "Hello"
#or "Goodbye"(for example,"Goodbye from process 3").
import numpy
from mpi4py import MPI 
comm=MPI.COMM_WORLD
rank=comm.Get_rank()
#size=comm.Get_size()

if rank%2==0:
	print("Hello from process",rank)
else:
    print("Goodbye from process",rank)