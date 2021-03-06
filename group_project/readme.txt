EE - 5423 Cloud Computing Course
Authors: David Espinola & Adam Lara

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

shell> sudo mysql -u root -p

--------------------------------------------------------------------------------

You will then be prompted to type in the password for your MPI user, if you just
put mysql it will return an error. If it installed correctly you will be greeted
by the MySql monitor. 

--------------------------------------------------------------------------------

Test it out by seeing what databases you have available. Type this into your
terminal

--------------------------------------------------------------------------------

mysql> show databases;

--------------------------------------------------------------------------------

You will then see something like this.

--------------------------------------------------------------------------------

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sakila             |
| sys                |
+--------------------+
5 rows in set (0.02 sec)

--------------------------------------------------------------------------------


You can now quit out of mysql.

--------------------------------------------------------------------------------

mysql> \q

--------------------------------------------------------------------------------

Now that mysql is installed on your machine, we need to create a user with root
access in the mysql database so the python program we created is able able to 
interact without any error. Go back into mysql.

--------------------------------------------------------------------------------

shell> sudo mysql -u root -p 

--------------------------------------------------------------------------------

Change to the mysql database

--------------------------------------------------------------------------------

mysql> use mysql;

--------------------------------------------------------------------------------

Now we need to acccess the table that shows us the users who have root access

--------------------------------------------------------------------------------

mysql> select user,host,plugin from mysql.user;

--------------------------------------------------------------------------------

A table like this should show up.

--------------------------------------------------------------------------------

+------------------+-----------+-----------------------+
| user             | host      | plugin                |
+------------------+-----------+-----------------------+
| root             | localhost | auth_socket           |
| mysql.session    | localhost | mysql_native_password |
| mysql.sys        | localhost | mysql_native_password |
| debian-sys-maint | localhost | mysql_native_password |
+------------------+-----------+-----------------------+
4 rows in set (0.00 sec)

--------------------------------------------------------------------------------

We are now going to be creating a user to add to this table. Within the single 
quotes place your own information except for 'localhost' and after identified by
input a password. I suggest using the same password you used for your MPI user
to keep it simple. 

--------------------------------------------------------------------------------

mysql> create user '****'@'localhost' identified by '******';

--------------------------------------------------------------------------------

To grant your yourself user access

--------------------------------------------------------------------------------

mysql> grant all privelages on *.* to '****'@'localhost';

--------------------------------------------------------------------------------

Now that the user has been created we need to change it so you can
have root access.

--------------------------------------------------------------------------------

mysql> update user set plugin="auth_socket" where User='****';

--------------------------------------------------------------------------------

To make sure we have made changes to the user table we need to flush the 
original privelages, then exit. 

--------------------------------------------------------------------------------

mysql> flush privileges;

--------------------------------------------------------------------------------

mysql> exit;

--------------------------------------------------------------------------------

Restart the mysql server from your MPI user.

--------------------------------------------------------------------------------

shell> sudo service mysql restart.

--------------------------------------------------------------------------------

You should now be able to access the mysql server with the user you created 
without having to sudo in.

--------------------------------------------------------------------------------

shell> mysql -u **** -p

--------------------------------------------------------------------------------

You should now be able to use mysql without having to sudo in, just to verify 
though we can go back into that user table. 

--------------------------------------------------------------------------------

mysql> select user,host,plugin from mysql.user;

--------------------------------------------------------------------------------

The user you have created should show up like so

--------------------------------------------------------------------------------

+------------------+-----------+-----------------------+
| user             | host      | plugin                |
+------------------+-----------+-----------------------+
| root             | localhost | mysql_native_password |
| mysql.session    | localhost | mysql_native_password |
| mysql.sys        | localhost | mysql_native_password |
| debian-sys-maint | localhost | mysql_native_password |
| *********        | localhost | mysql_native_password |
+------------------+-----------+-----------------------+
4 rows in set (0.00 sec)

-------------------------------------------------------------------------------- 

Now that mysql is intalled on our machines, we can proceed to download Sakila 
which is the fictional database we will be using as the video stores we will be
fetching the user inquired data from. On your terminal type.

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

Once sakila has been installed, we need to download Prophet. Prophet is the 
python library we will be using to input the dataframes we get from Sakila that 
is going to help us forecast future sales revenue along with some other packages 
that we need to run our code. Input these commands into your terminal. 

--------------------------------------------------------------------------------

MPI User shell> pip install fbprophet

MPI User shell> pip install pymysql 

MPI User shell> pip install sqlaclchemy 

--------------------------------------------------------------------------------

Now we need to install Tableau, unfortunately Tableau public is not able to 
connect to the mySQL database, we actually need the professional version in 
order to do that. Fortunately though we can get full access for a year as 
students. Below is a link to that. 

https://www.tableau.com/academic/students

It is going to ask for some general information. I suggest using your school 
email that way it can verify that you are a student correctly. You will then be 
sent instructions and a license code on how to Install Tableau to your desktop.

If you are running on linux, you will either have to VM or run it in a container
since it only can run either on Windows or Mac. 

--------------------------------------------------------------------------------
To run the completed python script type mpiexec -n 3 python3 serial_tsa.py
From the same folder as your python script.

This will create the table in MySQL for Tableau to pull from.

To see the completed Tableau go to https://public.tableau.com/views/sakila_forecast/Dashboard1?:display_count=y&publish=yes&:origin=viz_share_link
