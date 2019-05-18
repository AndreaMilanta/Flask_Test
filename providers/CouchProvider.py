import requests

product = {
    "_id":"123",
    "prodname": "First product",
    "category": "category1",
    "quantity": "4"
}

class CouchProvider(object):
    def reads_product(self) -> str:
        return product,200
        