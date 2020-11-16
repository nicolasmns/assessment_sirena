/*
I am assuming that the calculation of the MRR per account_id is the sum of the amount_excl_tax, which I again assume it's the
amount of the revenue without tax, and since the exercise is asking for the historical amount, I took the amount without tax. 
*/ 
SELECT 
	mrr.account_id,
	sum(mrr.amount_exc_tax) as MRR,
	sum(us.amount_exc_tax) as usage,
	sum(o.amount_exc_tax) as paid
FROM revenue_mrr mrr 
	JOIN revenue_usage us ON mrr.account_id = us.account_id 
	  	JOIN orders o ON mrr.account_id = o.account_id
WHERE o.status = 'SUCCESS'
GROUP BY
	mrr.account_id
	
	
	
	
	
	