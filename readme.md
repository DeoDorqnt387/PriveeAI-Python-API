### An API For [PriveeAI](https://www.privee.ai/)!
![](https://github.com/DeoDorqnt387/PriveeAI-Python-API/blob/main/images/1.png)


## Example Usage For chatting:

```python
from privee import priveeAI
from dotenv import load_dotenv

load_dotenv()

while True:
    message = input("You: ")

    hapry = priveeAI()
    response = hapry.chat(message)
    print(response)
```

## Prerequisites
> Rename the file .env.expl to .env
> 
> Open CMD and Run pip install -r requirements.txt to install the required dependencies

## Usage
You need to provide some information in the .env:
> SESSION_TOKEN # Go to the [PriveeAI](https://www.privee.ai/) website. Press F12, go to the applications tab, select Cookies, find user_session and get the value paste it here.

> USERID # Enter the chat section of a random bot. Press F12. Click on the Network tab. Send a message to the bot. It should set something called botResponse. Click on it and click on Payload in the Incoming Tab. Take your user_id from there and paste it.

> CHATID # Click on a random bot. copy the part of the link where the name of the bot is written. Paste it.

> LLM # Privee-8b, Privee-70b, Privee-120b, GPT4

## You can also change your username.
```python
from privee import priveeAI
from dotenv import load_dotenv

load_dotenv()

hapry = priveeAI()
response = hapry.update_username("your-usename")
print(response)
```
