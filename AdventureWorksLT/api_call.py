import requests
import json

def get_data():
    r = requests.get('http://127.0.0.1:8000/dashboard/api/customers')

    if r.status_code == 200:
        customers = r.json()
        return [customer['firstname'] for customer in customers]

    else:
        return r.status_code

def post_data(post_data):
    headers = {'Content-Type': 'application/json'}
    session = requests.Session()
    response = session.post('http://127.0.0.1:8000/dashboard/api/customers/', headers=headers, data=post_data)
    print('Response:', response.text)

    if response.status_code == 201:
        print('Post created successfully!')
    else:
        print('Post creation failed.')

    return response.json()    

data = {
    "customerid": 50137,
    "namestyle": False,
    "title": "Ms",
    "firstname": "Nicole",
    "middlename": "",
    "lastname": "Gibson",
    "suffix": "",
    "companyname": "ggc",
    "salesperson": "lakd",
    "emailaddress": "asdf@gmail.com",
    "phone": "2071748381",
    "passwordhash": "asldkfj",
    "passwordsalt": "sadfa",
    "modifieddate": "2024-03-14T09:17:00Z"
}

#print(get_data())
print(post_data(json.dumps(data)))