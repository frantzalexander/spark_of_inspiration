import requests

class RequestData():
    def __init__(self):
        self.website_url = "https://zenquotes.io/api/random"
        
    def get_quote(self):
        self.response = requests.get(url = self.website_url)
        self.response.raise_for_status()
        self.data = self.response.json()
        self.quote_data = {
                "Quote": self.data[0]["q"],
                "Author": self.data[0]["a"]
            }
        
        return self.quote_data