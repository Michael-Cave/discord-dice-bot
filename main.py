import discord
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Sets intents and enables message content reading
INTENTS = discord.Intents.default()
INTENTS.message_content = True

bot = discord.Client(intents=INTENTS)

# EVENT LISTENER FOR WHEN THE BOT SWITCHES FROM OFFLINE TO ONLINE
@bot.event
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")

        guild_count += 1

    print(f"MoonDiceRoller is in {guild_count} servers")


# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL
@bot.event
async def on_message(message):
    print(f"I've received a message: {message.content}")
    # CHECKS IF THE MESSAGE SENT IS "HELLO"
    if message.content == "hello":
        print("Hello recieved")
        # SENDS BACK A MESSAGE TO THE CHANNEL.
        await message.channel.send("get fucked")



# EXECUTES THE BOT WITH THE SPECIFIED TOKEN.
bot.run(DISCORD_TOKEN)