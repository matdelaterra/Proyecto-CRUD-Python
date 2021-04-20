import sys
import csv
import os
CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []

def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)

def _save_clients_to_storage():
    tmp_table_name = f'{CLIENT_TABLE}.tmp'
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)



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
    _initialize_clients_from_storage()
    _print_welcome()
    command = input('')
    command = command.upper()

    if command == 'C':
        client = _ask_client()
        create_client(client)


    elif command == 'L':
        list_clients()

    elif command == 'D':
        client = _ask_client()
        delete_client(client)
    

    elif command == 'U':
        client = _ask_client()
        update_client(client)


    elif command == 'S':
        client = _ask_client()
        found = search_client(client)
        if found:
            print('The client is in the client\'s list')
        else:
            print(f'The client: {client_name} is not in the client\'s list')
    else:
        print('El comando es inválido')
    
    _save_clients_to_storage()
