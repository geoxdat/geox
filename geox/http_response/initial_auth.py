class HttpReponseInitialAuth():
    def __init__(self, json_response):
        self.email: str = None
        self.num_of_projects: int = None
        
        self._parser(json_response)
    
    
    def _parser(self, json_response):
        self.email = json_response['email'] \
            if 'email' in json_response else None
        
        self.num_of_projects = json_response['num_of_projects'] \
            if 'num_of_projects' in json_response else None