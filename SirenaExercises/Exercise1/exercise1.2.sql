SELECT month, plan, revenue_type, sum(amount) FROM (
	SELECT
		to_char(DATE(mrr.created_at),'YYYY-MM-01') AS month,
		a.plan,
		'mrr' AS revenue_type,
		sum(mrr.amount_exc_tax) AS amount
	FROM
		account a
		  JOIN revenue_mrr mrr on a.id = mrr.account_id
	GROUP BY
		month, plan, revenue_type

	UNION 
	
	SELECT
		to_char(DATE(usg.created_at),'YYYY-MM-01') AS month,
		a.plan as plan,
		'usage' as revenue_type,
		sum(usg.amount_exc_tax) AS amount
	FROM
		account a
		  JOIN revenue_usage usg on a.id = usg.account_id
	GROUP BY
		month, plan, revenue_type
) temporary_table 
GROUP BY
	month, plan, revenue_type
ORDER BY month, plan, revenue_type;
	
