import requests, dotenv, os

# Load the environment variables
dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')

# Set the header
header = {'authorization': TOKEN}

def sendMessage(content, channel):
    payload = {"content": content, "tts": False, "flags": 0}
    requests.post(channel, headers=header, data=payload)