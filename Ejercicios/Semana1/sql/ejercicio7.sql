select  ag.name as AgentName,
        avg(c.duration) as AvgDuration
from agents ag
     inner join calls c on (ag.agentid = calls.agentid)
where c.pickedup = 1
  and c.productsold = 1
group by ag.name
order by ag.name

select  ag.name as AgentName,
        avg(c.duration) as AvgDuration
from agents ag
     inner join calls c on (ag.agentid = calls.agentid)
where c.pickedup = 1
  and c.productsold = 0
group by ag.name
order by ag.name