# Write your MySQL query statement below
# order table: order_id and item_id
# order by category

# Key: The function dayofweek("date") will return the day of that date, however, it starts with Sunday which means
1 presents Sunday, and 2 stands for Monday and so on.

WITH New_orders AS(
SELECT *,DAYOFWEEK(order_date) as "day_of_week"
    FROM Orders)
SELECT item_category as "Category",
SUM(CASE WHEN O.day_of_week = 2 THEN O.quantity ELSE 0 END) as "Monday",
SUM(CASE WHEN O.day_of_week = 3 THEN O.quantity ELSE 0 END) as "Tuesday",
SUM(CASE WHEN O.day_of_week = 4 THEN O.quantity ELSE 0 END) as "Wednesday",
SUM(CASE WHEN O.day_of_week = 5 THEN O.quantity ELSE 0 END) as "Thursday",
SUM(CASE WHEN O.day_of_week = 6 THEN O.quantity ELSE 0 END) as "Friday",
SUM(CASE WHEN O.day_of_week = 7 THEN O.quantity ELSE 0 END) as "Saturday",
SUM(CASE WHEN O.day_of_week = 1 THEN O.quantity ELSE 0 END) as "Sunday"
FROM New_orders O
RIGHT JOIN Items I ON O.item_id = I.item_id
GROUP BY item_category
ORDER BY item_category