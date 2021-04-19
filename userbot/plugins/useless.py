import asyncio
from collections import deque

from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import lightning_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Ultimate"

@borg.on(lightning_cmd(pattern=r"Fbi$"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 12)
    await event.edit("Arresting...")
    animation_chars = [
        "**This is the Fbi **",
        f"**Federal bureau of investigation I know you're too dumb to know that**",
        f"**You made a bad statement against MY BOSS **",
        "**Anywayx the investigation has been done you can't understand...**",
        "**Under the bot rule decree 49 of 2021**",
        "**You're hereby charged to 200years of cleaning my Master foot**",
        "**Your generations will continue your good work fortunately**",
        "**Arise servant and do as he commands",
        "**Start telling your dad and mum and siblings to start packing their baggage and luggages**",
        "I don't even know if any of your relatives know how to play with cock",
        "Anywayx you're now a slave and your master can make you a sex or play toy if he wants he's free",
        "**Congratulations on your achievement slut**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])




@borg.on(lightning_cmd(pattern=f"carss", outgoing=True))
async def _(event):
    if event.fwd_from:
        retun
    await event.edit("🚘-------------")
    await event.edit("-🚘------------")
    await event.edit("--🚘-----------")
    await event.edit("---🚘----------")
    await event.edit("----🚘---------")
    await event.edit("-----🚘--------")
    await event.edit("------🚘-------")
    await event.edit("-------🚘------")
    await event.edit("--------🚘-----")
    await event.edit("---------🚘----")
    await event.edit("----------🚘---")
    await event.edit("-----------🚘--")
    await event.edit("------------🚘-")
    await event.edit("-------------🚘")
    await asyncio.sleep(3)
    await event.delete()




@borg.on(lightning_cmd(pattern=f"verizon$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 19)
    await event.edit("attacking verizon...")
    animation_chars = [
        "`Connecting To Verizon NETWORK ....`",
        "`Connecting to Customers call`",
        "`Hello, Welcome to Verizon `",
        "`We are actually maintaining our network`",
        "`We are making upgrades actually`",
        "`Thanks to our director`",
        "`Mr Chris and his teams`",
        "`They are good people`",
        "`lol, the slut cut the call`",
        "*NEW CALL UPCOMING...*",
        "`Hey bitch`",
        "`What is it`",
        "`Verizon has been compromised by us`",
        "`Donate 20 million dollars now`",
        "`none of my business,tell Verizon suscribers`",
        "`Oh I never thought you're nobody`",
        "`I can see that in your face through your voice `",
        "`Get the fuck off nibba`",
        "**Donate to Save Verizon....**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 19])


CMD_HELP.update(
    {
     "| | Useless | |": "`.Fbi`\
     
     \n\n| Useless |: `.carss`\
     \n\n| Useless |: `.rain`\` Animation plugin.`\
     
    }
)
