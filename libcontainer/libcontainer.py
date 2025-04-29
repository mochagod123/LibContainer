import discord
from discord.ext import commands
import aiohttp

class Container():
    def __init__(self, bot: commands.Bot):
        self.token = bot.http.token
        self.comp = []

    def text(self, content: str):
        return {
            "type": 10,
            "content": content
        }

    def separator(self):
        return {"type": 14}

    def labeled_link(self, button_label: str, url: str):
        return {
            "type": 2,
            "style": 5,
            "label": button_label,
            "url": url
        }

    def labeled_customid_button(self, button_label: str, custom_id: str, style: int = 4):
        return {
            "type": 2,
            "style": style,
            "label": button_label,
            "custom_id": custom_id
        }
    
    def labeled_button(self, label: str, button: dict):
        return {
            "type": 9,
            "components": [
                {
                    "type": 10,
                    "content": label
                }
            ],
            "accessory": button
        }

    def action_row(self, components: list):
        return {
            "type": 1,
            "components": components
        }

    def add_view(self, view: dict):
        self.comp.append(view)

    async def send(self, channel: int):
        url = f"https://discord.com/api/v10/channels/{channel}/messages"
        headers = {
            "Authorization": f"Bot {self.token}",
            "Content-Type": "application/json"
        }
        data = {
            "flags": 32768,
            "components": [
                {
                    "type": 17,
                    "components": self.comp
                }
            ]
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as resp:
                return await resp.json()