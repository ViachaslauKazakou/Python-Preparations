import httpx
 
res = httpx.get('https://ticket.rzd.ru/searchresults/v/1/5a323c29340c7441a0a556bb/5a3244bc340c7441a0a556ca/2024-12-30')
print(res.url)
print(dir(res))
print(res.content)