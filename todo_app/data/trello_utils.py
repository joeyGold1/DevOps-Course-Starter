import os
class TrelloUtils():
    def __init__(self):
        not_started_list_id = os.getenv("TRELLO_NOT_STARTED_LIST_ID")
        in_progress_list_id= os.getenv("TRELLO_IN_PROGRESS_LIST_ID")
        completed_list_id = os.getenv("TRELLO_COMPLETE_LIST_ID")

        self.id_to_status = {not_started_list_id: "To Do", in_progress_list_id: "In Progress", completed_list_id: "Complete"}
        self.status_to_id = {"To Do": not_started_list_id, "In Progress": in_progress_list_id, "Complete": completed_list_id}
