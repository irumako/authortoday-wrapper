from .catalog import Catalog


# Client Class
class Client:

    def __init__(self, token: str):
        self.catalog = Catalog(token)
