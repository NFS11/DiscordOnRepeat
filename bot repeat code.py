import discord

# Replace with your bot's token
TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

# Intents allow the bot to read messages
intents = discord.Intents.default()
intents.message_content = True  # Required for reading message content

client = discord.Client(intents=intents)

# Replace this with your Discord user ID to restrict the !logout command
BOT_OWNER_ID = YOUR_DISCORD_USER_ID  # e.g., 123456789012345678

@client.event
async def on_ready():
    print(f'Bot is online as {client.user}')

@client.event
async def on_message(message):
    # Prevent the bot from replying to itself
    if message.author == client.user:
        return

    # Handle commands
    if message.content.startswith("!"):
        command_parts = message.content.split(" ", 1)  # Split the command into name and arguments
        command = command_parts[0].lower()  # Get the command keyword (e.g., !repeat)
        args = command_parts[1] if len(command_parts) > 1 else None  # Get the arguments (if any)

        if command == "!repeat":
            if args:
                await message.channel.send(args)
            else:
                await message.channel.send("Nothing was provided to repeat. Use the command like this: (e.g !repeat I like juice).")

        elif command == "!ping":
            await message.channel.send(f"{message.author.mention}, Online and working!")

        elif command == "!logout":
            if message.author.id == BOT_OWNER_ID:
                await message.channel.send("You are authorised to logout the bot token. Logging off...")
                await client.close()
            else:
                await message.channel.send("You are not authorised to logout bot token. Command failed.")

# Run the bot
try:
    client.run(TOKEN)
except Exception as e:
    print(f"Failed to start the bot: {e}")
