
import numpy as np
from app import handler
import json

def test_handler_output():

    target = np.arange(15).reshape(3, 6).tolist()

    actual = json.loads(handler(None, None)["body"])["Array"]
    
    assert actual == target