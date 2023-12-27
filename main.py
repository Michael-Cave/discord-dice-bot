import discord
import os
from dotenv import load_dotenv
import dicemath

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
    # Splits the message
    split_message = message.content.split(" ")
    roll_command = False
    if split_message[0] == "-roll":
        subsplit = split_message[1].split("d")
        quantity = int(subsplit[0])
        sides = int(subsplit[1])

        #Initializes the expected dice and rolls them
        if len(split_message) > 2:
            if split_message[2] == "Shadowrun":
                dice = dicemath.Shadowrun(quantity, sides)
                result = dice.roll_dice()
                rolls, glitch_report, exploded_report = result
                await message.channel.send(f"Results: {rolls} \n {glitch_report} \n {exploded_report}")
        else :
            dice = dicemath.Dice(quantity, sides)
            result = dice.roll_dice()
            # SENDS BACK A DEFAULT MESSAGE TO THE CHANNEL.
            await message.channel.send(f"Results: {result}")



# EXECUTES THE BOT WITH THE SPECIFIED TOKEN.
bot.run(DISCORD_TOKEN)