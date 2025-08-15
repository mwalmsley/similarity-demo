import os

from azure.cosmos import CosmosClient

import tmp_secrets

def get_container(database_name='q1', container_name='zoobot'):
    # container means "collection of items", the nosql version of a table
    # this is the class you use to add, edit, delete, etc.
    URL = os.environ['ACCOUNT_URI']
    KEY = os.environ['ACCOUNT_KEY']
    client = CosmosClient(URL, credential=KEY)

    # https://azuresdkdocs.z19.web.core.windows.net/python/azure-cosmos/latest/index.html#get-an-existing-container
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)
    return container