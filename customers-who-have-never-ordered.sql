# Write your MySQL query statement below
SELECT Customers.Name as Customers
FROM Customers
WHERE customers.id not in(
    select customerid from orders
);
