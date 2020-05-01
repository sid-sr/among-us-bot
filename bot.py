# Discord bot code:
# author: Siddharth Sriraman
import os
from dotenv import load_dotenv
from amongus import AmongUsClient

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = AmongUsClient(GUILD)
client.run(TOKEN)