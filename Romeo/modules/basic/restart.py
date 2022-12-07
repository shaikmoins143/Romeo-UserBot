import os
import shutil
import asyncio
from git import Repo
from pyrogram.types import Message
from pyrogram import filters, Client
from git.exc import GitCommandError, InvalidGitRepositoryError
from Romeo.helper.basic import edit_or_reply
from Romeo import SUDO_USER

from Romeo.modules.help import *


@Client.on_message(filters.command(["restart", "reload"], ".") & (filters.me | filters.user(SUDO_USER)))
async def restart(client, m: Message):
    reply = await m.edit("**Restarting...**")
    
    await reply.edit(
        "Successfully Restarted RomeoBot...\n\n💞 Wait 1-2 minutes\nLoad plugins...</b>")
    os.system(f"kill -9 {os.getpid()} && python3 -m Romeo")
