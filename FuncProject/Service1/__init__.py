import logging

import azure.functions as func

import requests


def main(req: func.HttpRequest) -> func.HttpResponse:

    numbers = requests.get('https://gttofuncapp.azurewebsites.net/api/service2?code=m5vje9BPa5YH9pvMAdBmrVpDN0LV7tpS6w4YXMZabVwR0W568J72MQ==').text
    letters = requests.get('https://gttofuncapp.azurewebsites.net/api/service3?code=hQxHDw3MtlXm5WrcMA9cQbaBCm2EVSGa1xfRkacEA3GJr5tkovaKPA==').text

    return func.HttpResponse(
        str(numbers + letters),
        status_code=200
    )
