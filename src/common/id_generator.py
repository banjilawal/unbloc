class IdGenerator:
    def __init__(self):
        self.travel_request_id = 1
        self.travel_decision_id = 1
        self.board_id = 1
        self.boulder_id = 1
        self.travel_server_id = 1
        self.portal_id = 1
        self.crate_id = 1

    def next_portal_id(self) -> int:
        current_id = self.portal_id
        self.portal_id += 1
        return current_id

    def next_travel_server_id(self) -> int:
        current_id = self.travel_server_id
        self.travel_server_id += 1
        return current_id

    def next_board_id(self) -> int:
        current_id = self.board_id
        self.board_id += 1
        return current_id

    def next_boulder_id(self) -> int:
        current_id = self.boulder_id
        self.boulder_id += 1
        return current_id

    def next_crate_id(self) -> int:
        current_id = self.crate_id
        self.crate_id += 1
        return current_id

    def next_travel_request_id(self) -> int:
        current_id = self.travel_request_id
        self.travel_request_id += 1
        return current_id

    def next_travel_decision_id(self) -> int:
        current_id = self.travel_decision_id
        self.travel_decision_id += 1
        return current_id

global_id_generator = IdGenerator()
