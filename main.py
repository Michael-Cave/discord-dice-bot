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
            modifier = split_message[2]
            if split_message[2] == "Shadowrun":
                if sides != 6:
                    await message.channel.send("Shadowrun exclusively uses a d6 dice pool.  Please try again with the correct dice.")
                else :
                    dice = dicemath.Shadowrun(quantity, sides)
                    result = dice.roll_dice()
                    rolls, glitch_report, exploded_report = result
                    await message.channel.send(f"Results: {rolls}, {dice._hits} hits! \n {glitch_report} \n {exploded_report}")
            elif split_message[2] == "D&D":
                dice = dicemath.Dungeons_and_dragons(quantity, sides)
                result = dice.roll_dice()
                if dice._critical != None:
                    rolls, dice._critical, outcome = result
                    await message.channel.send(f"Results: {rolls} \n {dice._critical} \n {outcome}")
                else :
                    rolls, outcome = result
                    await message.channel.send(f"Results: {rolls} \n {outcome}")
            
            elif split_message[2] == "Advantage":
                dice = dicemath.Dungeons_and_dragons(quantity, sides, adv=True)
                result = dice.roll_dice()
                if dice._critical != None:
                    rolls, dice._critical, outcome = result
                    await message.channel.send(f"Results: {rolls} \n {dice._critical} \n {outcome}")
                else :
                    rolls, outcome = result
                    await message.channel.send(f" Results: {rolls} \n {outcome}")

            elif split_message[2] == "Disadvantage":
                dice = dicemath.Dungeons_and_dragons(quantity, sides, disadv=True)
                result = dice.roll_dice()
                if dice._critical != None:
                    rolls, dice._critical, outcome = result
                    await message.channel.send(f"Results: {rolls} \n {dice._critical} \n {outcome}")
                else :
                    rolls, outcome = result
                    await message.channel.send(f" Results: {rolls} \n {outcome}")

            elif split_message[3] == "D&D":
                dice = dicemath.Dungeons_and_dragons(quantity, sides, modifier)
                result = dice.roll_dice()
                if dice._critical != None:
                    rolls, dice._critical, outcome = result
                    await message.channel.send(f"Results: {rolls} \n {dice._critical} \n {outcome}")
                else :
                    rolls, outcome = result
                    await message.channel.send(f"Results: {rolls} \n {outcome}")
            
            elif split_message[3] == "Advantage":
                dice = dicemath.Dungeons_and_dragons(quantity, sides, modifier, True)
                result = dice.roll_dice()
                if dice._critical != None:
                    rolls, dice._critical, outcome = result
                    await message.channel.send(f"Results: {rolls} \n {dice._critical} \n {outcome}")
                else :
                    rolls, outcome = result
                    await message.channel.send(f" Results: {rolls} \n {outcome}")

            elif split_message[3] == "Disadvantage":
                dice = dicemath.Dungeons_and_dragons(quantity, sides, modifier, disadv=True)
                result = dice.roll_dice()
                if dice._critical != None:
                    rolls, dice._critical, outcome = result
                    await message.channel.send(f"Results: {rolls} \n {dice._critical} \n {outcome}")
                else :
                    rolls, outcome = result
                    await message.channel.send(f" Results: {rolls} \n {outcome}")
        else :
            dice = dicemath.Dice(quantity, sides)
            result = dice.roll_dice()
            # SENDS BACK A DEFAULT MESSAGE TO THE CHANNEL.
            await message.channel.send(f"Results: {result}")



# EXECUTES THE BOT WITH THE SPECIFIED TOKEN.
bot.run(DISCORD_TOKEN)