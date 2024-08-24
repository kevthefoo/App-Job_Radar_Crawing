import requests, dotenv, os

# Load the environment variables
dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')
CHANNEL_HOOK = os.getenv('CHANNEL_HOOK')
HOOK_CHANNEL_URL = f"https://discord.com/api/v9/channels/{CHANNEL_HOOK}/messages"

# Set the header
header = {'authorization': TOKEN}

def sendMessage(content):
    payload = {"content": content, "tts": False, "flags": 0}
    requests.post(HOOK_CHANNEL_URL, headers=header, data=payload)