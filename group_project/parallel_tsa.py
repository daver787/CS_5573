#serial version of tsa_model for predicting sakila revenue on per store basis
#imports
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fbprophet import Prophet

#imports for MPI
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()


if rank==0:
     #make connection to the database
    mydb=mysql.connector.connect(
     host="localhost",
     database="sakila",
     user="root",
     passwd="clearlab")

    #sql query to bring in store data at daily level
    sql_query="""
    select
    date(p.payment_date)as payment_date, 
    st.store_id,
    sum(p.amount) as store_revenue
    from store as s
    inner join staff as st on s.store_id=st.store_id
    inner join payment as p on st.staff_id=p.staff_id
    where year(cast(p.payment_date as date))=2005
    group by st.store_id,date(payment_date)
    ;"""

     #create dataframe to hold the data using pandas
    store_df=pd.read_sql(sql_query,con=mydb)

    #convert date column to datetime object and drop previous date column
    store_df['ds']=pd.to_datetime(store_df['payment_date'])
    store_df.drop(columns='payment_date',inplace=True)

    #seperate the stores to fit different TSA model to each one.
    store_1_df=store_df[store_df['store_id']==1]
    store_2_df=store_df[store_df['store_id']==2]

    #set the index to be the date column for input into fbprophet model
    store_1_df=store_1_df.rename(columns={'store_revenue':'y'}).drop(columns='store_id')
    store_2_df=store_2_df.rename(columns={'store_revenue':'y'}).drop(columns='store_id')
    stores=[store_1_df,store_2_df]
    for i in range(2):
         comm.send(stores[i],dest=i+1)

else:
     stores=comm.recv(source=0)
     print(stores.head(),rank)
     #m=Prophet()
     #m.fit(stores)
     #future=m.make_future_dataframe(periods=30)
     #forecast=m.predict(future)
     #fig1=m.plot(forecast)
     #plt.show()

