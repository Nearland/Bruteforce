import requests
import pprint
import main

response = requests.post('https://httpbin.org/post', json={'login': 'admin', 'password': '1234'})

print(response.status_code)
if response.status_code == 200:
    r = response.json()
    print(pprint.pprint(r))
    print(r['json']['password'])
else:
    print('error')

m = main.find_max([1, 2, 3, 7, 3, -90, 12, 45, 2, 44, 0])
print(m)
m = main.find_max([5, 8, 90])
print(m)