import requests
from bs4 import BeautifulSoup
import os

from dotenv import load_dotenv

load_dotenv()
class PriveeAI:

    def __init__(self, url="https://www.privee.ai/"):
        self.url = url

    def fetch_page(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        cookies = {
            "user_session": os.getenv("SESSION_TOKEN")
        }
        response = requests.get(self.url,headers=headers, cookies=cookies, verify=False)
        response.raise_for_status()
        if response.status_code == 200:
            return BeautifulSoup(response.content, "html.parser")
        else:
            print(f"Request failed with status code {response.status_code}")
            return None
    def update_username(self,your_username: str):
        headers = {
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            }
        payload = {
            "uid": os.getenv("USERID"),
            "oldUsername": None,
            "username": your_username

        }
        cookies = {
            "user_session":os.getenv("SESSION_TOKEN")
        }
        api_url = f"https://www.privee.ai/api/v1/user/updateUsernameById"
        try:
            response = requests.post(api_url, json=payload, cookies=cookies, headers=headers)
            response.raise_for_status()
            data = response.json()
            return data["username"]
        except requests.exceptions.HTTPError as err:
            print("HTTP error occurred:", err)
        except Exception as err:
            print("Other error occurred:", err)   

    def chat(self, message:str):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        }
        payload = {
            "botContext": None,
            "bot_username": os.getenv("CHATID"),
            "lastMessages": [],
            "userMessage": message,
            "userMessageOriginal": message,
            "user_id": os.getenv("USERID"),
            "story_id": "main",
            "selectedLLM": os.getenv("LLM")
        }
        cookies = {
            "user_session":os.getenv("SESSION_TOKEN")
        }
        api_url = f"https://www.privee.ai/api/v1/chat/botResponse"
        try:
            response = requests.post(api_url, json=payload, cookies=cookies, headers=headers)
            response.raise_for_status()
            data = response.json()
            return data["msg"]["response"]
        except requests.exceptions.HTTPError as err:
            print("HTTP error occurred:", err)
        except Exception as err:
            print("Other error occurred:", err)
