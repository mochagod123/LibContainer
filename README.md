# LibContainer
discord.pyで、Containerを使うためのライブラリ

使い方
```
import libcontainer.container as container
from discord.ext import commands
import discord

bot = commands.Bot(command_prefix="!!", intents=discord.Intents.all())

@bot.command(name="testing")
async def testing(ctx: commands.Context):
    co = container.Container(bot)
    b1 = co.labeled_customid_button(button_label="Test", custom_id="test_beta_view_button")
    co.add_view(co.labeled_button("Test", b1))
    l1 = co.labeled_link("Test", url="https://google.com")
    l2 = co.labeled_link("Test", url="https://google.com")
    co.add_view(co.action_row([l1, l2]))
    co.add_view(co.separator())
    co.add_view(co.text("Test"))
    print(co.comp)
    print(await co.send(ctx.channel.id))

bot.run("Token")
```