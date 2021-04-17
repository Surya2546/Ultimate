# Always give credit
# Give credit to me
# Give credit to chris

import asyncio

from userbot.utils import lightning_cmd


@borg.on(lightning_cmd("anipic"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 4
    animation_ttl = range(0, 10)
    # input_str = event.pattern_match.group(1)
    # if input_str == "anipic":
    await event.edit("anipic")
    animation_chars = [
        "Ultimate bring me the list of anime pictures you have",
        "OMG **{DEFAULTUSER}** i don't really have much with me😥",
        "I will always make you happy boss let me loot some from the net",
        "Connecting to INTERNET SERVER",
        "NAME - {DEFAULTUSER}",
        "LOOTING SPEED - 280KB/S",
        "DONE🤝",
        "https://telegra.ph/file/88ca5566d336014defda9.jpg",
        "https://telegra.ph/file/f2625ee5b877f5a145b0a.jpg",
        "https://telegra.ph/file/75cf5e36d5ec0ce3605e1.jpg",
        "https://telegra.ph/file/10333ab5b47d3a1478395.jpg",
        "https://telegra.ph/file/65c398ad65e80efcb8e21.jpg",
        "https://telegra.ph/file/bc046a522a4ad92ba8f30.jpg",
        "https://telegra.ph/file/4cf87615bd9e7069e4ca5.jpg",
        "https://telegra.ph/file/da35c1da15e80e87604c4.jpg",
        "https://telegra.ph/file/a696ae2ba6a5255cc4f6c.jpg",
        "https://telegra.ph/file/f9555803966e984a1b1a0.jpg",
        "https://telegra.ph/file/de0e4ee483f5bd442e8c5.jpg",
        "https://telegra.ph/file/997e2fde9f0420ac8fabf.jpg",
        "https://telegra.ph/file/496f209c09688d985853e.jpg",
        "https://telegra.ph/file/b7b2ce9e528a8787d0858.jpg",
        "https://telegra.ph/file/c19519f3bb7796a773566.jpg",
        "https://telegra.ph/file/e51302c45f23cb2dad40b.jpg",
        "https://telegra.ph/file/dd46c0d64ee8272839a6e.jpg",
        "https://telegra.ph/file/1ae925f56fde36ff1cf2f.jpg",
        "https://telegra.ph/file/e3d373379c6e42ce8f10e.jpg",
        "https://telegra.ph/file/fc3bc012e243f6b243718.jpg",
        "https://telegra.ph/file/1d48fc23b0590cb69cd98.jpg",
        "https://telegra.ph/file/397da1e39f349e3696e45.jpg",
        "https://telegra.ph/file/973e20f6003916f7d47b1.jpg",
        "https://telegra.ph/file/50aeb934af436730a3448.jpg",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])
