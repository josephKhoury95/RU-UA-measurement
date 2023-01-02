# Darknet Analysis:

Note: needs access to the MERIT ORION Network Telescope: https://github.com/Merit-Research/darknet-events

Backscatter events:   
 
 ```
select SourceIP, Port, First, Last, Bytes, Packets, Traffic, Country, ASN, Org, Prefix, RDNS  
from `orion-20191028.orion_network_telescope.events`  
WHERE  
    First >= "2021-12-01"  
    AND First <= "2022-12-01"  
    AND (traffic = 12  
    OR traffic = 14  
    OR traffic = 1)  
    AND (country = "UA"  
      OR country = "RU")  
ORDER BY First   
```

Scannnig events:  

```
select SourceIP, Port, First, Last, Bytes, Packets, Traffic, Mirai, Country, ASN, Org, Prefix, RDNS  
from `orion-20191028.orion_network_telescope.events`   
WHERE  
    First >= "2021-12-01"  
    AND First <= "2022-06-30"  
    AND (traffic = 11  
    OR traffic = 16  
    OR traffic = 0)  
    AND (country = "UA"  
      OR country = "RU")  
ORDER BY First  
```


