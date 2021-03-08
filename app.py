import json
import numpy as np


def handler(event, context):

    a = np.arange(15).reshape(3, 5)

    print("Your numpy array :")
    print(a)

    body = {
        "message": "Hello, world! Your function executed successfully!",
        "Array": a.tolist()
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
