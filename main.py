import requests
import json 

API_KEY = "tpUTwTx6GTH-"
PROJECT_TOKEN = "tz0yaGzgDusq"
RUN_TOKEN = "tYB5B3Dawx_p"

response = requests.get(f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data', params={"api_key": API_KEY})
data = json.loads(response.text)
# print(data["total"])

class Data: 
    def __init__(self, api_key, project_token):
        self.api_key = API_KEY
        self.project_token = PROJECT_TOKEN
        self.params = {
            "api_key": self.api_key
        }
        self.get_data()

    def get_data(self):
        response = requests.get(f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data', params={"api_key": API_KEY})
        self.data = json.loads(response.text)
    
    def get_total_cases(self):
        data = self.data['total']
        
        for content in data:
            if content['name'] == 'Coronavirus Cases:':
                return content['value']
        
    def get_total_deaths(self):
        data = self.data['total']
        
        for content in data:
            if content['name'] == 'Deaths:':
                return content['value']
            
        return "0"

    def get_country_data(self, country):
        data = self.data['country']
        
        for content in data:
            if content['name'].lower() == country.lower():
                return content
            
        return "0"


data = Data(API_KEY, PROJECT_TOKEN)
