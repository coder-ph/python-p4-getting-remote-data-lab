import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            return response.content
        except:
            return 'an error occured while making request to the provided url'

    def load_json(self):
        try:
            response_body = self.get_response_body()
            return json.loads(response_body)
        except:
            return 'an unexpected error occured'