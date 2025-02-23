import requests
response = requests.get('http://googleууу.com', timeout=10)
print('Status Code:', response.status_code)
