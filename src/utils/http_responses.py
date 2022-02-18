class Response:

    def __init__(self, response, status_code):
        self.response = response
        self.status_code = status_code

    def build_response(self, resource:str):
        response = {
            "resource": {resource: self.response},
            "errors": [],
            "status_code": self.status_code,
        }
        return response

    def build_list_response(self, resource:str):
        response = {
            "resources": {resource:[self.response]},
            "errors": [],
            "status_code": self.status_code,
        }
        return response