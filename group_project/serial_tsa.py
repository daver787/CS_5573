#serial version of tsa_model for predicting sakila revenue on per store basis
#imports
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fbprophet import Prophet


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
print(store_1_df.info())
print(store_2_df.info())

#set the index to be the date column for input into fbprophet model
store_1_df=store_1_df.rename(columns={'store_revenue':'y'}).drop(columns='store_id')
store_2_df=store_2_df.rename(columns={'store_revenue':'y'}).drop(columns='store_id')

#graph the data to have idea for parameter settings for model
store_1_df.plot(x='ds',y='y',color='red',kind='scatter')
store_2_df.plot(x='ds',y='y',color='blue',kind='scatter')
plt.show()

#fit the prophet model and set the parameters based on observations in graph
#model for store_1
m=Prophet()
m.fit(store_1_df)

#model for store_2
n=Prophet()
n.fit(store_2_df)

#future dataframes to hold predictions for both stores
future_1=m.make_future_dataframe(periods=30)

future_2=n.make_future_dataframe(periods=30)


#make predictions to be held in future dataframes
forecast_1=m.predict(future_1)

forecast_2=n.predict(future_2)


#plot the results of the predicition
fig1=m.plot(forecast_1)
fig2=n.plot(forecast_2)
plt.show()

#show the decomposition of the model
fig3=m.plot_components(forecast_1)
fig4=n.plot_components(forecast_2)
plt.show()

