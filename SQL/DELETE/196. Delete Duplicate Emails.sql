SQL Schema
Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its smallest Id.

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id is the primary key column for this table.
For example, after running your query, the above Person table should have the following rows:

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+


#DELETE a
#FROM Person a, Person b
#WHERE a.email = b.email and a.Id > b.Id

# You can't use the table in the subquery of your delete clause for some certain rules, add a select to make it a sub-subqery, and it would be fine.
DELETE FROM Person WHERE id not in (
    SELECT duplicates FROM (
SELECT MIN(id) as duplicates FROM Person GROUP BY Email) t
)