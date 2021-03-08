
import json
import numpy as np

def handler3(event, context):
    body = {
        "message": "Hello, world! Your function executed successfully!"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response