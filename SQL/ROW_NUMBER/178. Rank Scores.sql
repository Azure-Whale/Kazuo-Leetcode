# # Write your MySQL query statement below
# # Needs To reserve duplicates
# # Needs to reserve same rank nuber for same score, Join the rownumber from a unique rank table

# Key, syntax for row number : ROW_NUMBER() OVER(ORDER BY column(...) DESC/ASC)
# Key, You cannot add a distinct to the subquery of row_number, as you cannot add distinct to the order by clause as well
# But a subqery can help you with it

SELECT S.Score, t.row_num as "Rank"
FROM Scores S,
(SELECT ROW_NUMBER() OVER(ORDER BY Score DESC) as row_num, Score
FROM (
SELECT DISTINCT Score FROM Scores
) t ) t
WHERE t.Score = S.Score
ORDER BY S.Score DESC