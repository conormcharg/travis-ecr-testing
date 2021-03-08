
import numpy as np
from app import handler2
import json

def test_handler_output():

    target = np.arange(15).reshape(3, 5).tolist()

    actual = json.loads(handler2(None, None)["body"])["Array"]
    
    assert actual == target