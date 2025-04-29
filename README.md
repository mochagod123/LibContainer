# LibContainer
discord.pyで、Containerを使うためのライブラリ

インストール
```
pip install -U git+https://github.com/mochagod123/LibContainer
```

使い方
```
import libcontainer as container
from discord.ext import commands
import discord

bot = commands.Bot(command_prefix="!!", intents=discord.Intents.all())

@bot.command(name="send")
async def send(ctx: commands.Context):
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

@bot.command(name="edit")
async def edit(ctx: commands.Context, message: discord.Message):
    co = container.Container(bot)
    b1 = co.labeled_customid_button(button_label="Test2", custom_id="test_beta_view_button")
    co.add_view(co.labeled_button("Test2", b1))
    l1 = co.labeled_link("Test2", url="https://google.com")
    l2 = co.labeled_link("Test2", url="https://google.com")
    co.add_view(co.action_row([l1, l2]))
    co.add_view(co.separator())
    co.add_view(co.text("Test2"))
    print(co.comp)
    print(await co.edit(message, ctx.channel.id))

bot.run("Token")
```