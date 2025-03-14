-- Query 1
SELECT p.part_name, SUM(sd.quantity) AS total_sold
FROM sale_details sd
JOIN parts p USING(part_id)
GROUP BY p.part_name
ORDER BY total_sold DESC
LIMIT 5;


-- Query 2
SELECT
    p.part_name,
    AVG(dd.selling_price) AS avg_selling_price,
    AVG(p.retail_price) AS avg_retail_price,
    AVG(p.retail_price - dd.selling_price) AS price_difference
FROM delivery_details dd
JOIN delivery_requests dr USING(request_id)
JOIN parts p USING(part_id)
GROUP BY p.part_name
ORDER BY price_difference DESC;