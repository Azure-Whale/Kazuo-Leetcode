SQL Schema
Table: Logs

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
id is the primary key for this table.


Write an SQL query to find all numbers that appear at least three times consecutively.

Return the result table in any order.

The query result format is in the following example:



Logs table:
+----+-----+
| Id | Num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+

Result table:
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
1 is the only number that appears consecutively for at least three times.





# Key: To obtain a consecutive result, using self-join to join adjacent rows to see if there is consecutive rows satisfying
the condition.


# Write your MySQL query statement below

SELECT DISTINCT L1.num as "ConsecutiveNums"
FROM Logs L1, Logs L2, Logs L3
WHERE
L1.Id = ( L2.Id + 1 )
AND
L1.Id = ( L3.Id -1)
AND L1.num = L2.num
AND L1.num = L3.num