EE - 5423 Cloud Computing Course
Authors: David Espinloa & Adam Lara

Welcome! This is the README for our fictional video store.
I will be helping you intstall everything that is necessary in order for you to
run this program successfully. 

First, you need to make sure you have MYSQL intstalled on to your MPI User in
the cloud. If you do not have MPI installed you can simply save this text as 
mpich_setup.sh and run bash ./mpich_setup.sh on the user where you would like
MPI and the Python files necessary for it to work to be installed.

--------------------------------------------------------------------------------

# Script to install MPICH and related libararies
# along with mpi4py python compiler.
# Remove .txt extension and replace with .sh
# Execute as shell script with bash.
#
# Dr. Jeff Prevost
# 3/31/2020

#MPICH installs
sudo apt update -y
sudo apt install -y build-essential
sudo apt install -y mpich
sudo apt install -y libmpich-dev
sudo apt install -y python3-dev python3-pip


# pip installs for mpi4py
pip3 install --user -U setuptools
pip3 install --user mpi4py
pip3 install --user numpy

--------------------------------------------------------------------------------

Once that is created, we can now proceed to install MYSQL. 
Type this in the termninal of your logged in MPI user 

--------------------------------------------------------------------------------

shell> sudo apt-get install mysql-server 

--------------------------------------------------------------------------------

Once downloaded, it will prompt you how much additional disk space will be used,
Type "Y" then hit enter.

Once the packages are installed, clear the terminal and test to see if mysql is
installed onto your machine. Type this in your terminal. 

--------------------------------------------------------------------------------

shell> sudo mysql 

--------------------------------------------------------------------------------

You will then be prompted to type in the password for your MPI user, if you just
put mysql it will return an error. If it installed correctly you will be greeted
by the MySql monitor. You can now quit out of mysql.

--------------------------------------------------------------------------------

mysql> \q

--------------------------------------------------------------------------------

Now that mysql is intalled on our machines, we can proceed to download Sakila 
which is the fictional database we will be using as the video stores we will be
fetching the user inquired data from. On your terminal type

--------------------------------------------------------------------------------

wget https://downloads.mysql.com/docs/sakila-db.zip

--------------------------------------------------------------------------------

Once the zipped file is downloaded we can unzip it in a destination folder of 
your choice. 

--------------------------------------------------------------------------------

We will now create the database structure and populating it using the following 
commands. Keep in mind, the path is going to be different based on where you 
exctacted the sakila zip file we just downloaded. 

Go into mysql like we had tested before and run both of these commands

--------------------------------------------------------------------------------

mysql> SOURCE C:/temp/sakila-db/sakila-schema.sql;
mysql> SOURCE C:/temp/sakila-db/sakila-data.sql;

--------------------------------------------------------------------------------

Once this is done, we can confirm if the database is installed corectly by 
typing in.

--------------------------------------------------------------------------------

mysql> USE sakila;

mysql> SHOW FULL TABLES; 

--------------------------------------------------------------------------------

Then a list of all the available tables in Sakila will be shown in a variety of
categories which you can look into. 

********************************************************************************

For ease of use, we had downloaded the IDE MySQL workbench in order to visualize
the data structure and make changes to fit our requirements of the project. 

You can download it for your respective operating system following this link.

https://dev.mysql.com/downloads/workbench/

********************************************************************************
