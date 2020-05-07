# Script to install MPICH and related libararies
# along with mpi4py python compiler.
# Remove .txt extension and replace with .sh
# Execute as shell script with bash.
#
# Dr. Jeff Prevost
# 3/31/2020
#Updated for project use by David Espinola, M.S.
#05/07/2020

#MPICH installs and sql
sudo apt update -y
sudo apt install -y build-essential
sudo apt install -y mpich
sudo apt install -y libmpich-dev
sudo apt install -y python3-dev python3-pip
sudo apt install -y mysql-server

# pip installs for mpi4py and project
pip3 install --user -U setuptools
pip3 install --user mpi4py
pip3 install --user numpy
pip3 install --user fbprophet
pip3 install --user pymysql
pip3 install --user mysql
pip3 install --user sqlalchemy
pip3 install --user pandas