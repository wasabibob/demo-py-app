import pytest
import sys

def test_example():
    assert 1 + 1 == 2

# Test the python runtime vesrion
def test_version():
    if sys.version_info >= (3, 10):
        print("Using Python 3.10 or newer.")
    else:
        print("Python version is older than 3.10.")
    assert sys.version_info >= (3, 10)

# Test the index route
#def test_index(client):
#    response = client.get('/')
#    assert response.status_code == 200
#    assert b'Hello, World!' in response.data