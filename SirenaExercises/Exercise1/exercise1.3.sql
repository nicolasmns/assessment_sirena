-- The sum(amount_exc_tax) works when there are two registers with the same account_id on the same month, this will give the
-- total amount of the MRR for that month, preventing duplicates with different amounts.
SELECT to_char(date(created_at),'YYYY-MM-01') AS month, mrr.account_id, sum(amount_exc_tax) AS amount  
FROM revenue_mrr mrr
JOIN
	(SELECT * FROM
		(SELECT max(to_char(date(created_at),'YYYY-MM-01')) AS month, account_id
		FROM revenue_mrr
		GROUP BY account_id) temp_mrr
	WHERE month NOT IN (SELECT max(to_char(date(created_at),'YYYY-MM-01')) FROM revenue_mrr) ) rlast
ON 
	to_char(date(created_at),'YYYY-MM-01') = rlast.month and mrr.account_id = rlast.account_id
GROUP BY
    to_char(date(created_at),'YYYY-MM-01'), mrr.account_id
	
	
	
	
	
	
	
	
	
	
	
	
	
	