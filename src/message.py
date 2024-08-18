import requests, dotenv, os

# Load the environment variables
dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')
CHANNEL_1 = os.getenv('CHANNEL_1')


# Set the header
header = {'authorization': TOKEN}

def sendMessage(content):
    payload = {"content": content, "tts": False, "flags": 0}
    requests.post(CHANNEL_1, headers=header, data=payload)