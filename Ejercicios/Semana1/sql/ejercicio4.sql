select  calls.callid,
        cust.customerId,
        cust.name,
        case when cust.Age > 30 then 'Si' else 'No' end As Mayor30,
        calls.productsold
from customers cust
     inner join calls c on (cust.customerId = calls.customerid)
where cust.occupation like '%Engineer%'
order by cust.name desc


