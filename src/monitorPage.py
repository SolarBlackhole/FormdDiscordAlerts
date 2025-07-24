import asyncio

import discord
from discord import app_commands
from discord.ext import commands, tasks
from discord.utils import get
import random
import datetime


from products import products.products
from monitorPage_helper import check_product_availability

class MonitorPage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.check_product.start()

    def cog_unload(self):
        self.check_product.cancel()

    @tasks.loop(minutes=1)
    async def check_product(self):
        # Example random product check
        product_name = random.choice(list(products.keys()))
        variant_id = random.choice(list(products[product_name]["variants"].keys()))
        print(f"Checking availability for {product_name} (Variant ID: {variant_id})")

        availability = check_product_availability(product_name, variant_id)
        
        if availability:
            print(f"{product_name} is available!")
            

    @check_product.before_loop
    async def before_check_product(self):
        await self.bot.wait_until_ready()  

class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="config", description="Configure the bot settings")
    async def config(self, interaction: discord.Interaction):
        await interaction.response.send_message("Configuration command executed.")

    @app_commands.command(name="status", description="Check the bot status")
    async def status(self, interaction: discord.Interaction):
        uptime = datetime.datetime.now() - self.bot.start_time
        await interaction.response.send_message(f"Bot is running for {uptime}.")
    
    @app_commands.command(name="interval", description="Set the check interval in minutes")