import os
class TrelloUtils():
    def __init__(self):
        not_started_board_id = os.getenv("TRELLO_NOT_STARTED_LIST_ID")
        completed_board_id = os.getenv("TRELLO_COMPLETE_LIST_ID")
        self.id_to_status = {not_started_board_id: "Not Started", completed_board_id: "Complete"}
        self.status_to_id = {"Not Started": not_started_board_id, "Complete": completed_board_id}