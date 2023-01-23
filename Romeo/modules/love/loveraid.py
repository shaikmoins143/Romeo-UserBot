import asyncio
from pyrogram import filters, Client
from Romeo.modules.help import *
from Romeo.helper.utility import get_arg
from pyrogram.types import *
from pyrogram import __version__
import os
import sys
import asyncio
import re
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from cache.data import *
from Romeo.database.rraid import *
from Romeo import SUDO_USER
from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message
DEVS = int(5368154755)
from Romeo.helper.PyroHelpers import get_ub_chats
from Romeo.modules.basic.profile import extract_user, extract_user_and_reason
SUDO_USERS = SUDO_USER
LOVES = []


@Client.on_message(
    filters.command(["lr"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def raid(xspam: Client, e: Message):  
      Romeo = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Romeo) == 2:
          counts = int(Romeo[0])
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          ok = await xspam.get_users(Romeo[1])
          id = ok.id
#          try:
#              userz = await xspam.get_users(id)
#          except:
#              await e.reply(f"`404 : User Doesn't Exists In This Chat !`")
#              return #remove # to enable this
          if int(id) in VERIFIED_USERS:
                text = f"Chal Chal baap Ko mat sikha"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"Abe Lawde that guy part of my devs."
                await e.reply_text(text)
          else:
              fname = ok.first_name
              mention = f"[{fname}](tg://user?id={id})"
              for _ in range(counts):
                    reply = choice(LOVE)
                    msg = f"{mention} {reply}"
                    await xspam.send_message(e.chat.id, msg)
                    await asyncio.sleep(0.10)
      elif e.reply_to_message:
          msg_id = e.reply_to_message.from_user.id
          counts = int(Romeo[0])
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          try:
              userz = await xspam.get_users(id)
          except:
              await e.reply(f"`404 : User Doesn't Exists In This Chat !`")
              return
          if int(id) in VERIFIED_USERS:
                text = f"Chal Chal baap Ko mat sikha"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"Abe Lawde that guy part of my devs."
                await e.reply_text(text)
          else:
              fname = ok.first_name
              mention = f"[{fname}](tg://user?id={id})"
              for _ in range(counts):
                    reply = choice(LOVE)
                    msg = f"{mention} {reply}"
                    await xspam.send_message(e.chat.id, msg)
                    await asyncio.sleep(0.10)
      else:
          await e.reply_text("Usage: .raid count username")


add_command_help(
    "lraid",
    [
        [".lr", "<user id and count>`."],
    ],
)

@Client.on_message(
    filters.command(["drlr"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def gmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    ex = await message.edit_text("`Processing...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await ex.edit(f"`Please specify a valid user!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await ex.edit(f"`Please specify a valid user!`")
        return
    try:
        if user.id not in (await get_rraid_users()):
           await ex.edit("Loveraid is not activated on this user")
           return
        await unrraid_user(user.id)
        LOVES.remove(user.id)
        await ex.edit(f"[{user.first_name}](tg://user?id={user.id}) DeActivated LoveRaid!")
    except Exception as e:
        await ex.edit(f"**ERROR:** `{e}`")
        return


add_command_help(
    "loveraid",
    [
        [".rlr", "Reply To User\n To LoveRaid on Someone."],
        [".drlr", "To Disable LoveRaid."],
    ],
)
