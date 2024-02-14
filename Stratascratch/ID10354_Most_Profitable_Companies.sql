--PostgreSQL

SELECT company, profits
FROM (select company, sum(profits) as profits
      from forbes_global_2010_2014
      group by company) as temp
ORDER BY profits DESC
LIMIT 3;