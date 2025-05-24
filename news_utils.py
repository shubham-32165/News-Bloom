# app/news_utils.py

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

NEWS_API_KEY = '18b2d45a6c5e4d4bb27faf9448d139b9'

def fetch_news_by_query(query, page_size=12):
    url = f'https://newsapi.org/v2/everything?q={query}&language=en&pageSize={page_size}&apiKey={NEWS_API_KEY}'
    try:
        response = requests.get(url, verify=False)
        data = response.json()
        if data.get("status") != "ok":
            print(f"Error fetching {query}: {data}")
            return []
        return data.get("articles", [])
    except Exception as e:
        print(f"Exception while fetching news for {query}:", e)
        return []
