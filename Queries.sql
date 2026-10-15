SELECT d.source, COUNT(*) AS successful_deals, SUM(amount) AS total_revenue
FROM deals d
WHERE status = 'won' AND d.source <> 'unknown'		
GROUP BY d.source
ORDER BY successful_deals DESC;
 
SELECT d.customer_id,COUNT(*) AS total_deals,SUM(amount) AS total_revenue,
		AVG(amount) AS average_deal_amount 
FROM deals d
WHERE status = 'won'
GROUP BY d.customer_id
ORDER BY total_revenue DESC
LIMIT 10;


SELECT c.customer_id, c.name, c.surname,d.status, COUNT(*) total_deals 
FROM customers c
JOIN deals d USING(customer_id)
WHERE d.status = 'won'
GROUP BY c.customer_id, c.name, c.surname, d.status
HAVING COUNT(*) > 2 
ORDER BY total_deals DESC;

