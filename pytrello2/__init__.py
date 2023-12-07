from .client import HttpClient
from .board import BoardManager


class TrelloClient:
    """
    Trello client class.

    Main client class for interacting with the Trello API. Provides high-level
    access to Trello functionality through various manager classes.

    """

    def __init__(self, api_key, token):
        """
        Initializes the TrelloClient with API credentials and sets up necessary
        managers.
        """
        self.http_client = HttpClient(api_key, token)
        self.board = BoardManager(self.http_client)
