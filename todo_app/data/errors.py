class TrelloApiError(Exception):
    def __init__(self, message, path, method):
        super().__init__("Trello API Error: {message} Occurred on {method} request to {path}".format(message=message, method=method, path=path))
