from geox.exceptions import ServerErrorException


class HttpReponseDataset():
    def __init__(self, json_response: dict, dataset_type: str):
        self.data = json_response['data'] if 'data' in json_response else []
        self.max_result = json_response['max_result'] if 'max_result' in json_response else None
        self.dataset_type = dataset_type
        
    def _is_max_result_reached(self):
        if self.max_result is None:
            raise ServerErrorException('Cannot retrieve "max result" data from server.')
        
        return len(self.data) < self.max_result
    
    def get_next_index(self):
        next_index = -2
        if len(self.data) > 0 and not self._is_max_result_reached():
            next_index = self.data[-1]['id'] + 1

        return next_index