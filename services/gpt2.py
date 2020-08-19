import requests
import json

class GPT2Service:

    def __init__(self, config):
        self.url = config["url"]


    def complete(self, text):
        headers = {
            'Authorization': 'Bearer YOUR_ORG_OR_USER_API_TOKEN',
            'Content-Type': 'application/json',
        }
        data = json.dumps(text)

        response = requests.post(self.url, headers=headers, data=data)
        return response.json()[0]['generated_text']


if __name__ == "__main__":
    s = GPT2Service()
    r = s.complete("I am going to")
    print(r)