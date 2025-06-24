from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import
InputAudioStream
import asyncio

API_ID = 22553378
API_HASH = 55c94444ce8830c3247dd72881a26f39
SESSION = "BQFYIyIANdShGVMRe557Z9Tlp_wNwsf...."

app = Client(session_name=SESSION,api_id=API_ID,api_hash=API_HASH)
pytg = PyTgCalls(app)

# === Admin Commands ===

@app.on_message(filters.command("ban", ".") & filters.me)
async def ban(_, msg):
    if msg.reply_to_message:
         await
app.ban_chat_member(msg.chat.id,msg.reply_to_message.from_user.id)
         await msg.reply("✅️User banned.")

@app.on_message(filters.command("unban" , ".") & filters.me)
async def unban(_, msg):
    if len(msg.command) > 1:
         await
app.unban_chat_member(msg.chat.id, int(msg.command[1]))
                 await msg.reply("🥳User unbanned.")
