import pyrogram
from pyrogram import Client

friday_ = """
╔═══╗───╔═╗─╔═╗
║ ══╬═╦═╬═╬═╝ ╠═══╦═╦═╗
║ ╔═╣ ╔═╣ ║╔╗ ║╔╗ ╠══ ║
╚═╝ ╚═╝ ╚═╩═══╩═╩═╩═══╝
Copyright (C) 2020-2021 by @FoxXbotOfficials, < https://github.com/FoxXbotOfficials >.
This file is part of < https://t.me/FoxXbotOfficials > project,
and is released under the "GNU v3.0 License Agreement".
Please see < https://telegra.ph/text-05-31-3 >
All rights reserved.
"""

print(friday_)
api_id = input("Enter Your API ID: \n")
api_hash = input("Enter Your API HASH : \n")

with Client("FridayUB", api_id=api_id, api_hash=api_hash) as bot_:
    first_name = (bot_.get_me()).first_name
    string_session_ = f"<b>String Session For {first_name}</b> \n<code>{bot_.export_session_string()}</code>"
    bot_.send_message("me", string_session_, parse_mode="html")
    print(f"String Has Been Sent To Your Saved Message : {first_name}")
