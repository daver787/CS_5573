use sakila;
select
date(p.payment_date), 
st.store_id,
sum(p.amount) as store_revenue
from store as s
inner join staff as st on s.store_id=st.store_id
inner join payment as p on st.staff_id=p.staff_id
where year(cast(p.payment_date as date))=2005
group by st.store_id,date(payment_date)
