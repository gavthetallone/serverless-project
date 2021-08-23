import logging

import azure.functions as func

import random


def main(req: func.HttpRequest) -> func.HttpResponse:

    letters = ""

    for i in range(0,5):
        letters += chr(random.randint(ord('a'), ord('z')))

    
    return func.HttpResponse(
        letters,
        status_code=200
    )
