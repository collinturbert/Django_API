import requests
import json
from decouple import config

def CRUD(type, table, header, pk=None, data={}):
    if type not in ["Get", "Post", "Put", "Delete"]:
        raise ValueError("Invalid input for type, make sure you use Get, Post, Put, or Delete")
    
    # Set URL
    url = f'http://127.0.0.1:8000/api/{table}/'
    if pk is not None:
        url += f'{pk}/'
    
    # Get response for Get method or to use as example
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        responseData = response.json()
    else:
        print(f'Got an invalid response: {response.status_code}')
        return response.status_code

    # Run through various CRUD methods
    if type == 'Get':
        print(responseData)
        return responseData
    
    elif type == 'Post':
        print(f"Data example: {responseData[0]}")
        for key in responseData[0].keys():
            value = input(f"Value for {key}: ")
            if value.strip():
                data[key] = value
        
        data = json.dumps(data)
        session = requests.Session()
        postResponse = session.post(url, headers=header, data=data)
        print('Response:', postResponse.text)
        return postResponse.status_code
    
    elif type == 'Put' and pk is not None:
        putData = responseData
        for key, value in putData.items():
            print(f'Current data: {key}: {value}')
            updatedValue = input(f'Enter updated value for {key} (leave blank to keep current):')
            if updatedValue.strip():
                putData[key] = updatedValue
        data = json.dumps(putData)
        session = requests.Session()
        putResponse = session.put(url, headers=header, data=data)
        print('Response:', putResponse.text)
        return putResponse.status_code
    
    elif type == 'Delete' and pk is not None:
        delete_check = input(f'Are you sure you want to delete instance {pk} from {table}? (0=False, 1=True)')
        if int(delete_check) == 1:
            deleteResponse = requests.delete(url, headers=header)
            print('Response: (204 = Deleted)', deleteResponse.status_code)
            return deleteResponse.status_code
        else:
            print('Delete operation cancelled')
            return
    
    else:
        print("Something went wrong, double check your input and make sure you include a pk for Put and Delete")
        print('Operation Cancelled')


def main():
    try:
        header = {
            'Content-Type': 'application/json',
            'Authorization': config('TOKEN'),
        }

        CRUD('Post', 'Contacts', header=header)

    except Exception as e:
        print(f'An error occurred in the main function: {e}')

    finally:
        print('Finished!')


if __name__ == '__main__':
    main()
