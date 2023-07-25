select  ag.name as AgentName,
        count(c.callid) as NCalls,
        max(c.duration) as Shortest,
        min(c.duration) as Longest,
        avg(c.duration) as AvgDuration,
        sum(c.productsold) as TotalSales
from agents ag
     inner join calls c on (ag.agentid = calls.agentid)
where c.pickedup = 1
group by ag.name
order by ag.name
