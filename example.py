from harpy import harpyChat
from dotenv import load_dotenv

load_dotenv()

while True:
    message = input("You: ")

    hapry = harpyChat()
    response = hapry.chat(message)
    print(response)