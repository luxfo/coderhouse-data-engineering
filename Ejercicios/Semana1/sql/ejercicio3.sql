select  customerId,
        name,
        case when Age > 30 then 'Si' else 'No' end As Mayor30
from customers
order by name desc
