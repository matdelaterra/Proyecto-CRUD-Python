import sys

clients = [   
        {
            'name':'Pablo',
            'company':'Google',
            'email':'pablo@google.com',
            'position':'Software engineer'
         },
        {
            'name':'Ricardo',
            'company':'Facebook',
            'email': 'ricardo@facebook.com',
            'position': 'Data engineer'
          }]


def create_client(client):
    global clients 
    if client not in clients:
        clients.append(client)
    else:
        print('Client alredy is in the client\'s list')


def list_clients():
    global clients
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']))


def update_client(client):
    global clients
    if client in clients:
        index = clients.index(client)
        print('***New client data***')
        updated_client_name = _ask_client()
        clients[index] = updated_client_name
        print('Modified')
    else:
        print('Client is not in clients list')


def delete_client(client):
    global clients

    if client in clients:
        clients.remove(client)
        
    else:
        print('Client is not in clients list')


def search_client(client):
    global clients
    for selected_client in clients:
        if selected_client != client:
            continue
        else:
            return True

def _print_welcome():
    print('Welcome to platzi ventas')
    print('*'*50)
    print('What would you do today?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[D]elete client')
    print('[U]pdate client')
    print('[S]earch client')

def _get_client_field(field_name):
    field = None
    while not field:
        field = input(f'What is the client {field_name}: ')

    return field

def _ask_client():
    
    client = {
            'name': _get_client_field('name'),
            'company' : _get_client_field('company'),
            'email' : _get_client_field('email'),
            'position': _get_client_field('position')
            }
    return client
if __name__ == '__main__':
    _print_welcome()
    command = input('')
    command = command.upper()

    if command == 'C':
        client = _ask_client()
        create_client(client)
        list_clients()

    elif command == 'L':
        list_clients()

    elif command == 'D':
        client = _ask_client()
        delete_client(client)
        list_clients()

    elif command == 'U':
        client = _ask_client()
        update_client(client)
        list_clients()

    elif command == 'S':
        client = _ask_client()
        found = search_client(client)
        if found:
            print('The client is in the client\'s list')
        else:
            print(f'The client: {client_name} is not in the client\'s list')
    else:
        print('El comando es inválido')

