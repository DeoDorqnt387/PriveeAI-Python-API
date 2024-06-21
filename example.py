from privee import priveeAI
from dotenv import load_dotenv

load_dotenv()

while True:
    message = input("You: ")

    hapry = priveeAI()
    response = hapry.chat(message)
    print(response)
