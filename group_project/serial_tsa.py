#serial version of tsa_model for predicting sakila revenue on per store basis
#imports
import mysql.connector
import pandas as pd
#make connection to the database
mydb=mysql.connector.connect(
	host="localhost",
	database="sakila",
	user="root",
	passwd="clearlab")

#sql query to bring in store data at daily level
sql_query="""
select
date(p.payment_date), 
st.store_id,
sum(p.amount) as store_revenue
from store as s
inner join staff as st on s.store_id=st.store_id
inner join payment as p on st.staff_id=p.staff_id
group by st.store_id,date(payment_date);"""

#create dataframe to hold the data using pandas
store_df=pd.read_sql(sql_query,con=mydb)

store_1_df=store_df[[store_df.store_id==1]]
store_2_df=store_df[[store_df.store_id==2]]