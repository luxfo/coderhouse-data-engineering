select distinct occupation
from customers
where occupation like '%Engineer%'
order by occupation asc
