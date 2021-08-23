import logging

import azure.functions as func

import random


def main(req: func.HttpRequest) -> func.HttpResponse:

    return func.HttpResponse(
        str(random.randrange(10000, 99999)),
        status_code=200
    )
