"Checker Dapa"
import time
from pyrogram.errors.exceptions.bad_request_400 import YouBlockedUser
from userge import userge, Message
from userge.utils.exceptions import StopConversation


#chk
@userge.on_cmd("chk", about={
	'header': "Auth Only",
	'usage': "{tr}chk [Input CC]\n"})
	
async def gen(message: Message):
	"""Cek Auth"""
	replied = message.input_str
	chat = "@rkhackingbot"
	await message.edit("```YAMETE KUDASAIII..```")
	msgs = []
	ERROR_MSG = "Ijin dulu sama @Dappzx"
	try:
		async with userge.conversation(chat) as conv:
			try:
				await conv.send_message("/chk {}".format(replied))
			except YouBlockedUser:
				await message.err(f"**{ERROR_MSG}**", del_in=5)
				return 
			msgs = await conv.get_response(timeout=30, mark_read=True)
			if "Wait" in msgs.text:
				time.sleep(1)
				msgs = await conv.get_response(timeout=30, mark_read=True) 
				if "Wait" in msgs.text:
					time.sleep(1)
					msgs = await conv.get_response(timeout=30, mark_read=True) 
					if "Wait" in msgs.text:
						time.sleep(1)
						msgs = await conv.get_response(timeout=30, mark_read=True) 
						if "Wait" in msgs.text:
							time.sleep(1)
							msgs = await conv.get_response(timeout=30, mark_read=True)
							if "Wait" in msgs.text:
								time.sleep(1)
								msgs = await conv.get_response(timeout=30, mark_read=True)
								if "Wait" in msgs.text:
									time.sleep(1)
									msgs = await conv.get_response(timeout=30, mark_read=True)
									if "Wait" in msgs.text:
										time.sleep(1)
										msgs = await conv.get_response(timeout=30, mark_read=True)
										if "Wait" in msgs.text:
											time.sleep(1)
											msgs = await conv.get_response(timeout=30, mark_read=True)
											if "Wait" in msgs.text:
												time.sleep(1)
												msgs = await conv.get_response(timeout=30, mark_read=True)
												if "Wait" in msgs.text:
													time.sleep(1)
													msgs = await conv.get_response(timeout=30, mark_read=True)
													if "Wait" in msgs.text:
														time.sleep(1)
														msgs = await conv.get_response(timeout=30, mark_read=True) 
														if "Wait" in msgs.text:
															time.sleep(1)
															msgs = await conv.get_response(timeout=30, mark_read=True)  
															if "Wait" in msgs.text:
																time.sleep(1)
																msgs = await conv.get_response(timeout=30, mark_read=True)  
																if "Wait" in msgs.text:
																	time.sleep(1)
																	msgs = await conv.get_response(timeout=30, mark_read=True) 
																	if "Wait" in msgs.text:
																		time.sleep(1)
																		msgs = await conv.get_response(timeout=30, mark_read=True) 
																		if "Wait" in msgs.text:
																			time.sleep(1)
																			msgs = await conv.get_response(timeout=30, mark_read=True) 
																			if "Wait" in msgs.text:
																				time.sleep(1)
																				msgs = await conv.get_response(timeout=30, mark_read=True) 
																				if "Wait" in msgs.text:
																					time.sleep(1)
																					msgs = await conv.get_response(timeout=30, mark_read=True) 
																					if "Wait" in msgs.text:
																						time.sleep(1)
																						msgs = await conv.get_response(timeout=30, mark_read=True) 
																						if "Wait" in msgs.text:
																							time.sleep(1)
																							msgs = await conv.get_response(timeout=30, mark_read=True) 
	except StopConversation:
		pass 
	try:
		await message.edit(f"{msgs.text}")
	except AttributeError:
		await message.edit(f"`Bot tidak merespon!`", del_in=5)


#bin
@userge.on_cmd("bin", about={
	'header': "BIN",
	'usage': "{tr}bin [Enter bin]\n"})
	
async def bin(message: Message):
	"""BIN Ingfo"""
	replied = message.input_str
	chat = "@rkhackingbot"
	await message.edit("```YAMETE KUDASAII..```")
	msgs = []
	ERROR_MSG = "Ijin dulu sama @Dappzx"
	try:
		async with userge.conversation(chat) as conv:
			try:
				await conv.send_message("/bin {}".format(replied))
			except YouBlockedUser:
				await message.err(f"**{ERROR_MSG}**", del_in=5)
				return 
			msgs = await conv.get_response(timeout=30, mark_read=True)
			if "Wait" in msgs.text:
				time.sleep(1)
				msgs = await conv.get_response(timeout=30, mark_read=True) 
				if "Wait" in msgs.text:
					time.sleep(1)
					msgs = await conv.get_response(timeout=30, mark_read=True) 
					if "Wait" in msgs.text:
						time.sleep(1)
						msgs = await conv.get_response(timeout=30, mark_read=True) 
						if "Wait" in msgs.text:
							time.sleep(1)
							msgs = await conv.get_response(timeout=30, mark_read=True)
							if "Wait" in msgs.text:
								time.sleep(1)
								msgs = await conv.get_response(timeout=30, mark_read=True)
								if "Wait" in msgs.text:
									time.sleep(1)
									msgs = await conv.get_response(timeout=30, mark_read=True)
									if "Wait" in msgs.text:
										time.sleep(1)
										msgs = await conv.get_response(timeout=30, mark_read=True)
										if "Wait" in msgs.text:
											time.sleep(1)
											msgs = await conv.get_response(timeout=30, mark_read=True)
											if "Wait" in msgs.text:
												time.sleep(1)
												msgs = await conv.get_response(timeout=30, mark_read=True)
												if "Wait" in msgs.text:
													time.sleep(1)
													msgs = await conv.get_response(timeout=30, mark_read=True)
													if "Wait" in msgs.text:
														time.sleep(1)
														msgs = await conv.get_response(timeout=30, mark_read=True) 
														if "Wait" in msgs.text:
															time.sleep(1)
															msgs = await conv.get_response(timeout=30, mark_read=True)  
															if "Wait" in msgs.text:
																time.sleep(1)
																msgs = await conv.get_response(timeout=30, mark_read=True)  
																if "Wait" in msgs.text:
																	time.sleep(1)
																	msgs = await conv.get_response(timeout=30, mark_read=True) 
																	if "Wait" in msgs.text:
																		time.sleep(1)
																		msgs = await conv.get_response(timeout=30, mark_read=True) 
																		if "Wait" in msgs.text:
																			time.sleep(1)
																			msgs = await conv.get_response(timeout=30, mark_read=True) 
																			if "Wait" in msgs.text:
																				time.sleep(1)
																				msgs = await conv.get_response(timeout=30, mark_read=True) 
																				if "Wait" in msgs.text:
																					time.sleep(1)
																					msgs = await conv.get_response(timeout=30, mark_read=True) 
																					if "Wait" in msgs.text:
																						time.sleep(1)
																						msgs = await conv.get_response(timeout=30, mark_read=True) 
																						if "Wait" in msgs.text:
																							time.sleep(1)
																							msgs = await conv.get_response(timeout=30, mark_read=True) 
	except StopConversation:
		pass 
	try:
		await message.edit(f"{msgs.text}")
	except AttributeError:
		await message.edit(f"`Bot tidak merespon!`", del_in=5)


#sk
@userge.on_cmd("sk", about={
	'header': "Cek SK",
	'usage': "{tr}sk [Input SK]\n"})
	
async def key(message: Message):
	"""SK Checker"""
	replied = message.input_str
	chat = "@rkhackingbot"
	await message.edit("```YAMETE KUDASAII..```")
	msgs = []
	ERROR_MSG = "Ijin dulu sama @Dappzx"
	try:
		async with userge.conversation(chat) as conv:
			try:
				await conv.send_message("/sk {}".format(replied))
			except YouBlockedUser:
				await message.err(f"**{ERROR_MSG}**", del_in=5)
				return 
			msgs = await conv.get_response(timeout=30, mark_read=True)
			if "Wait" in msgs.text:
				time.sleep(1)
				msgs = await conv.get_response(timeout=30, mark_read=True) 
				if "Wait" in msgs.text:
					time.sleep(1)
					msgs = await conv.get_response(timeout=30, mark_read=True) 
					if "Wait" in msgs.text:
						time.sleep(1)
						msgs = await conv.get_response(timeout=30, mark_read=True) 
						if "Wait" in msgs.text:
							time.sleep(1)
							msgs = await conv.get_response(timeout=30, mark_read=True)
							if "Wait" in msgs.text:
								time.sleep(1)
								msgs = await conv.get_response(timeout=30, mark_read=True)
								if "Wait" in msgs.text:
									time.sleep(1)
									msgs = await conv.get_response(timeout=30, mark_read=True)
									if "Wait" in msgs.text:
										time.sleep(1)
										msgs = await conv.get_response(timeout=30, mark_read=True)
										if "Wait" in msgs.text:
											time.sleep(1)
											msgs = await conv.get_response(timeout=30, mark_read=True)
											if "Wait" in msgs.text:
												time.sleep(1)
												msgs = await conv.get_response(timeout=30, mark_read=True)
												if "Wait" in msgs.text:
													time.sleep(1)
													msgs = await conv.get_response(timeout=30, mark_read=True)
													if "Wait" in msgs.text:
														time.sleep(1)
														msgs = await conv.get_response(timeout=30, mark_read=True) 
														if "Wait" in msgs.text:
															time.sleep(1)
															msgs = await conv.get_response(timeout=30, mark_read=True)  
															if "Wait" in msgs.text:
																time.sleep(1)
																msgs = await conv.get_response(timeout=30, mark_read=True)  
																if "Wait" in msgs.text:
																	time.sleep(1)
																	msgs = await conv.get_response(timeout=30, mark_read=True) 
																	if "Wait" in msgs.text:
																		time.sleep(1)
																		msgs = await conv.get_response(timeout=30, mark_read=True) 
																		if "Wait" in msgs.text:
																			time.sleep(1)
																			msgs = await conv.get_response(timeout=30, mark_read=True) 
																			if "Wait" in msgs.text:
																				time.sleep(1)
																				msgs = await conv.get_response(timeout=30, mark_read=True) 
																				if "Wait" in msgs.text:
																					time.sleep(1)
																					msgs = await conv.get_response(timeout=30, mark_read=True) 
																					if "Wait" in msgs.text:
																						time.sleep(1)
																						msgs = await conv.get_response(timeout=30, mark_read=True) 
																						if "Wait" in msgs.text:
																							time.sleep(1)
																							msgs = await conv.get_response(timeout=30, mark_read=True) 
	except StopConversation:
		pass 
	try:
		await message.edit(f"{msgs.text}")
	except AttributeError:
		await message.edit(f"`Bot tidak merespon!`", del_in=5)

#vbv
@userge.on_cmd("vbv", about={
	'header': "Braintree 3D Check",
	'usage': "{tr}vbv [Input CC]\n"})
	
async def vbv(message: Message):
	"""Cek 3ds"""
	replied = message.input_str
	chat = "@rkhackingbot"
	await message.edit("```YAMETE KUDASAII..```")
	msgs = []
	ERROR_MSG = "Ijin dulu sama @Dappzx"
	try:
		async with userge.conversation(chat) as conv:
			try:
				await conv.send_message("/vbv {}".format(replied))
			except YouBlockedUser:
				await message.err(f"**{ERROR_MSG}**", del_in=5)
				return 
			msgs = await conv.get_response(timeout=30, mark_read=True)
			if "Wait" in msgs.text:
				time.sleep(1)
				msgs = await conv.get_response(timeout=30, mark_read=True) 
				if "Wait" in msgs.text:
					time.sleep(1)
					msgs = await conv.get_response(timeout=30, mark_read=True) 
					if "Wait" in msgs.text:
						time.sleep(1)
						msgs = await conv.get_response(timeout=30, mark_read=True) 
						if "Wait" in msgs.text:
							time.sleep(1)
							msgs = await conv.get_response(timeout=30, mark_read=True)
							if "Wait" in msgs.text:
								time.sleep(1)
								msgs = await conv.get_response(timeout=30, mark_read=True)
								if "Wait" in msgs.text:
									time.sleep(1)
									msgs = await conv.get_response(timeout=30, mark_read=True)
									if "Wait" in msgs.text:
										time.sleep(1)
										msgs = await conv.get_response(timeout=30, mark_read=True)
										if "Wait" in msgs.text:
											time.sleep(1)
											msgs = await conv.get_response(timeout=30, mark_read=True)
											if "Wait" in msgs.text:
												time.sleep(1)
												msgs = await conv.get_response(timeout=30, mark_read=True)
												if "Wait" in msgs.text:
													time.sleep(1)
													msgs = await conv.get_response(timeout=30, mark_read=True)
													if "Wait" in msgs.text:
														time.sleep(1)
														msgs = await conv.get_response(timeout=30, mark_read=True) 
														if "Wait" in msgs.text:
															time.sleep(1)
															msgs = await conv.get_response(timeout=30, mark_read=True)  
															if "Wait" in msgs.text:
																time.sleep(1)
																msgs = await conv.get_response(timeout=30, mark_read=True)  
																if "Wait" in msgs.text:
																	time.sleep(1)
																	msgs = await conv.get_response(timeout=30, mark_read=True) 
																	if "Wait" in msgs.text:
																		time.sleep(1)
																		msgs = await conv.get_response(timeout=30, mark_read=True) 
																		if "Wait" in msgs.text:
																			time.sleep(1)
																			msgs = await conv.get_response(timeout=30, mark_read=True) 
																			if "Wait" in msgs.text:
																				time.sleep(1)
																				msgs = await conv.get_response(timeout=30, mark_read=True) 
																				if "Wait" in msgs.text:
																					time.sleep(1)
																					msgs = await conv.get_response(timeout=30, mark_read=True) 
																					if "Wait" in msgs.text:
																						time.sleep(1)
																						msgs = await conv.get_response(timeout=30, mark_read=True) 
																						if "Wait" in msgs.text:
																							time.sleep(1)
																							msgs = await conv.get_response(timeout=30, mark_read=True) 
	except StopConversation:
		pass 
	try:
		await message.edit(f"{msgs.text}")
	except AttributeError:
		await message.edit(f"`Bot tidak merespon!`", del_in=5)




