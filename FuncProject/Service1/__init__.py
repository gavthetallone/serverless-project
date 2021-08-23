import logging

import azure.functions as func
from azure.cosmos import exceptions, CosmosClient, PartitionKey

import requests

endpoint = ""
key = ""

client = CosmosClient(endpoint, key)

database_name = 'FuncDatabase'
database = client.create_database_if_not_exists(id=database_name)

container_name = 'FuncContainer'
container = database.create_container_if_not_exists(
    id=container_name, 
    partition_key=PartitionKey(path="/password"),
    offer_throughput=400
)

def main(req: func.HttpRequest) -> func.HttpResponse:

    numbers = requests.get('https://gttofuncapp.azurewebsites.net/api/service2?code=m5vje9BPa5YH9pvMAdBmrVpDN0LV7tpS6w4YXMZabVwR0W568J72MQ==').text
    letters = requests.get('https://gttofuncapp.azurewebsites.net/api/service3?code=hQxHDw3MtlXm5WrcMA9cQbaBCm2EVSGa1xfRkacEA3GJr5tkovaKPA==').text

    password = numbers + letters

    container.create_item(body={
        "id":"1",
        "password":password})

    return func.HttpResponse(
        str(numbers + letters),
        status_code=200
    )
