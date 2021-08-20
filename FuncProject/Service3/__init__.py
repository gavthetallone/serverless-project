import logging

import azure.functions as func

import random


def main(req: func.HttpRequest) -> func.HttpResponse:

    return func.HttpResponse(
        chr(random.randint(ord('a'), ord('z'))),
        status_code=200
    )
