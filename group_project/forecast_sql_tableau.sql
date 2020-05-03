SELECT
date(p.payment_date) as payment_date, 
st.store_id,
sum(p.amount) as store_revenue,
'store_sales' as type
FROM store AS s
INNER JOIN staff AS st ON s.store_id=st.store_id
INNER JOIN payment AS p ON st.staff_id=p.staff_id
WHERE year(cast(p.payment_date as date))=2005
GROUP BY st.store_id,date(payment_date)
UNION
SELECT
payment_date,
store_id,
store_revenue,
'forecast' AS type
FROM store_forecast
where payment_date>'2005-08-23'