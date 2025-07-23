import discord
from discord.ext import commands
from secret import bot_token, application_id

class MyBot(commands.Bot):
    async def setup_hook(self):
        # Load any cogs or extensions here if needed
        pass

    async def on_ready(self):
        await self.wait_until_ready()
        await self.change_presence(
            status=discord.Status.online,
            activity=discord.Activity(
                name="FormdT1.com",
                type=discord.ActivityType.watching,
                state="Monitoring FormdT1 for restocks",
                details="Restock Alerts Bot"
            ),
        )
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")

bot = MyBot(
    command_prefix="!",
    intents=discord.Intents.all(),
    application_id=application_id,
)

bot.run(bot_token)

