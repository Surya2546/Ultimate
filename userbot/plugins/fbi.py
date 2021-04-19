# Give credit 
# Give credit to chris
# copy and don't give credit, you'll die 

import asyncio

from userbot.utils import lightning_cmd


@borg.on(lightning_cmd(pattern=r"fbi"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 4

    animation_ttl = range(0, 12)

    # input_str = event.pattern_match.group(1)

    # if input_str == "fbi":

    await event.edit("Arresting")

      animation_chars = [
        "**This is the Fbi ",
        f"Federal bureau of investigation I know you're too dumb to know that**",
        f"**You made a bad statement against MY BOSS ",
        "Anywayx the investigation has been done you can't understand...**",
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
    


