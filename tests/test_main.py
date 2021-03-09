from graphene.test import Client
from raybamusic.main import schema


def test_hello__with_name():
    client = Client(schema)
    executed = client.execute('''{ hello(name: "world!") }''')
    assert executed == {
        "data": {
            "hello": "Hello world!"
        }
    }


def test_hello__no_name():
    client = Client(schema)
    executed = client.execute('''{ hello }''')
    assert executed == {
        "data": {
            "hello": "Hello stranger"
        }
    }
