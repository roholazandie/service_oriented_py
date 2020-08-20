import requests
import json
from services.service import Service

class NewsService(Service):
    def __init__(self, config=None):
        Service.__init__(self, config)
        self._url = config["url"]
        self._headers = config["headers"]
        self._current_article = 0


    def get_content_info(self, top_headlines):
        content = top_headlines['articles'][self._current_article]['content']
        return content

    def get_title_info(self, top_headlines):
        title = top_headlines['articles'][self._current_article]['title']
        return title

    def get_description_info(self, top_headlines):
        print("getting description info")
        description = top_headlines['articles'][self._current_article]['description']
        return description

    def clean_text(self, text):
        text = text.replace("Image copyrightReutersImage caption", "")
        text = text.replace("\n", " ")
        text.encode("ascii", errors="ignore")
        # summary = re.sub('\[.*\]', '', summary)
        return text

    def format_response(self, top_headlines):
        description = self.get_description_info(top_headlines)
        title = self.get_title_info(top_headlines)
        
        # YLogger.debug(client_context, f"article description: {description}")

        search = f"The title of the article is {title}, here is a quick summary...{description} ."
        search += " Should I read the full article?"
        return search

    def ask_news(self):
        response = requests.request("GET", url=self._url, headers=self._headers, params=None)
        headline_dict = response.json()
        headline = headline_dict['value'][self._current_article]['name']
        return headline

if __name__ == "__main__":
    config = {
                "url": "https://microsoft-azure-bing-news-search-v1.p.rapidapi.com/",
                "headers": {
                    "x-rapidapi-host": "microsoft-azure-bing-news-search-v1.p.rapidapi.com",
                    "x-rapidapi-key": "2d82bb5d95msh2a4e5c2a45a8eb3p18b00ejsn98308d90b548"
                }
            }
    ns = NewsService(config)
    print(ns.ask_news())