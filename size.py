#Name: David Espinola
#Date:04/03/2020
#size.py
#Sometimes the program you write can only run correctly if it has a certain number
#of processes.Although you typically want to avoid writing these kinds of programs,
#sometimes it is inconvenient or unavoidable.Write a program that runs only if it has 
#5 processes. Upon failure,the root node should print "Error:This program must run with
#with 5 processes" and upon success it should print "Success!" To exit,call the function Comm.Abort()
 
import numpy
from mpi4py import MPI
comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()

if size==5 and rank==0:
        print("Success")
elif size!=5 and rank==0:
  print("Error: This program must run with 5 processes.")
  if rank !=0:
      comm.Abort(1)