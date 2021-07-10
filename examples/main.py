from discord.ext import commands
import discord
from discord_buttons_plugin import *

bot = commands.Bot(command_prefix="!")
buttons = ButtonsClient(bot)


@bot.event
async def on_ready():
    print("The bot is ready!")


@bot.command()
async def cbutton(ctx):
    await buttons.send(
        content="Click Fast!",
        channel=ctx.channel.id,
        components=[
            ActionRow([
                Button(
                    label="CLICK!",
                    style=ButtonType().Primary,
                    custom_id="button_one"
                )
            ])
        ]
    )


@buttons.click
async def button_one(ctx):
    await ctx.reply(f"{ctx.member} Clicked Me!")


"""
@buttons.click
async def button_one(ctx):
    await ctx.reply("Hello!")


@buttons.click
async def button_two(ctx):
    await ctx.reply("There are a total of 5 to try!")


@buttons.click
async def button_three(ctx):
    await ctx.reply("You can send ephemeral messages too!", flags=MessageFlags().EPHEMERAL)


@bot.command()
async def create(ctx):
    await buttons.send(
        content="This is an example message!",
        channel=ctx.channel.id,
        components=[
            ActionRow([
                Button(
                    label="Hello",
                    style=ButtonType().Primary,
                    custom_id="button_one"  # Refer to line 13
                ), Button(
                    label="New colour",
                    style=ButtonType().Secondary,
                    custom_id="button_two"  # Refer to line 17
                )
            ]), ActionRow([
                Button(
                    label="Another one",
                    style=ButtonType().Danger,
                    custom_id="button_three"  # Refer to line 21
                )
            ])
        ]
    )
"""

bot.run("ODYyODI4MTIzNDEzNjc2MDYy.YOeBTw.dqCo7FQkJXbTWVpDtxF449h1rBk")
