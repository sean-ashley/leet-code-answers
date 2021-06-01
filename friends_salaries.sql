SELECT name FROM students
INNER JOIN friends ON students.ID = friends.ID
INNER JOIN packages as p1 ON students.ID = p1.ID
INNER JOIN packages as p2 ON friends.Friend_ID = p2.id
WHERE p1.salary < p2.salary
ORDER BY p2.salary;
