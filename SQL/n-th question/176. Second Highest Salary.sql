"""SQL Schema
Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
Attention, the return value should be null if there is no No.2
Solutions:
1. Use Aggregation function, it would automatically return Max if there is no corresponding value
2. Use SELECT IFNULL((your query), NULL)"""

SELECT IFNULL((
SELECT e1.Salary
FROM Employee e1
WHERE 1 = (SELECT COUNT(DISTINCT(e2.Salary))
    FROM Employee e2
    WHERE
           e1.Salary < e2.Salary

)),NULL) as 'SecondHighestSalary'


SELECT MAX(Salary) AS SecondHighestSalary
FROM
(SELECT DISTINCT Salary
 from Employee
 Order by Salary desc
limit 1,1) inter