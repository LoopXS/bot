from . import *

REPOMSG = """
• **Ⲏⲉⲁʀⲧⳑⲉⲋⲋ Ⲉⲭⲥⳑυⲋⲓⳳⲉ Ⲃⲟⲧ** • 
"""

RP_BUTTONS = [
    [Button.url(get_string("bot_3"), "https://xhamsterlive.com")],
    [Button.url("Ⲋυⲣⲣⲟʀⲧ", "https://t.me/DarkPentester")],
]

BTS =[
    [
        Button.url("• Rⲉⲣⲟ •­", "https://xhamsterlive.com"), 
        Button.url("• Ⲋυⲣⲣⲟʀⲧ •­", "https://t.me/DarkPentester"),
    ], 
]
 

ULTSTRING = """🎇 **Thanks for Deploying Ⲏⲉⲁʀⲧⳑⲉⲋⲋ Ⲉⲭⲥⳑυⲋⲓⳳⲉ Ⲃⲟⲧ**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""


@ultroid_cmd(
    pattern="repo$",
    type=["official", "manager", "assistant"],
)
async def repify(e):
    await e.reply(REPOMSG, file=udB.get("STARTMEDIA"), buttons=BTS) 
    

@ultroid_cmd(pattern="cipher$")
async def useUltroid(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        ULTSTRING,
        file="https://telegra.ph/file/8ee3430e4229363c57c9c.jpg",
        buttons=button,
    )
    await eor(rs, f"**[Click Here]({msg.message_link})**")
