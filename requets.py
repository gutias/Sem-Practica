import requests  
import json

r = requests.get('https://reqres.in/api/users/2')
response=r.text
print(response)
re=r.json()
print(re)
# i=0  

# for datos in re['data']:
#     people={
#         "id":re['data'][i]['id'],
#         "email":re['data'][i]['email'],
#         "nombre":re['data'][i]['first_name']+" "+re['data'][i]['last_name'],
#     }
#     print(people)
#     i=i+1