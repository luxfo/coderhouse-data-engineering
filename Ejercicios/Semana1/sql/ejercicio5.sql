select  cust.customerId,
        cust.name,
        sum(c.productsold) as VentasTotales
        count(c.callid) as LlamadasTotales
from customers cust
     inner join calls c on (cust.customerId = calls.customerid)
where cust.occupation like '%Engineer%'
group by cust.customerId, cust.name
order by cust.name desc

select  cust.customerId,
        cust.name,
        sum(c.productsold) as VentasTotales
        count(c.id) as LlamadasTotales
from customers cust
     inner join calls c on (cust.customerId = calls.customerid)
group by cust.customerId, cust.name
order by cust.name desc
