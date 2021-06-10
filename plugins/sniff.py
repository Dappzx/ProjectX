"Sniff CFG by Qano & Modifed by Dappzx"
import time
from pyrogram.errors.exceptions.bad_request_400 import YouBlockedUser
from userge import userge, Message
from userge.utils.exceptions import StopConversation


#sniff
@userge.on_cmd("sniff", about={ 
	'header': "SNIFF",
	'usage': "{tr}sniff [Reply ke cfg]\n"})
	
async def sniff(message: Message):
	"""Untuk sniff cfg"""
	user = await userge.get_me()
	uname = user.username
	replied = message.reply_to_message
	if not replied:
		await message.err("```Reply ke cfg.```", del_in=5)
		return 
	if "npv2" in replied.document.file_name:
		chat = "@npv_unlock_bot"
		await message.edit("```Wait for result... ```")
		msgs = []
		ERROR_MSG = "Unblok bot @npv_unlock_bot untuk menggunakan command ini"
		try:
			async with userge.conversation(chat) as conv:
				try:
					await conv.forward_message(replied)
				except YouBlockedUser:
					await message.err(f"**{ERROR_MSG}**", del_in=5)
					return 
				msgs = await conv.get_response(timeout=30, mark_read=True)
				result = msgs.text
				if "VMESS" in result:
					result = f"{result}".replace("=>","»") 
		except StopConversation:
			pass 
		try:
			await message.edit(f"{result}")
		except AttributeError:
			await message.edit(f"`Bot tidak merespon!`", del_in=5)
	else:
		chat = "@hcdecryptor_bot"
		await message.edit("```Wait for result... ```")
		msgs = []
		ERROR_MSG = "Unblok bot @hcdecryptor_bot untuk menggunakan command ini"
		try:
			async with userge.conversation(chat) as conv:
				try:
					await conv.forward_message(replied)
				except YouBlockedUser:
					await message.err(f"**{ERROR_MSG}**", del_in=5)
					return 
				msgs = await conv.get_response(timeout=30, mark_read=True)
				result = msgs.text
				if "Satisfied with the result" in result:
					result = result.replace("Satisfied with the result? Follow us!","").replace("🌐 BOT CHANNEL: @hctoolschannel","").replace("🌐 BOT GROUP: @hctools","").replace("💻 SOURCE CODE: https://github.com/hctools/hcdrill-tg","")
					result = f"Dec by: @{uname}\n\n{result}".replace("[>]","»")
		except StopConversation:
			pass 
		try:
			await message.edit(f"{result}")
		except AttributeError:
			await message.edit(f"`Bot tidak merespon!`", del_in=5)
