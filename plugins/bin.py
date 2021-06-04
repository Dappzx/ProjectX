"Checker CC by Qano"
import time
from pyrogram.errors.exceptions.bad_request_400 import YouBlockedUser
from userge import userge, Message
from userge.utils.exceptions import StopConversation


#gen
@userge.on_cmd("gen", about={
	'header': "GEN CC",
	'usage': "{tr}gen [Enter bin]\n"})
	
async def gen(message: Message):
	"""Untuk gen cc"""
	replied = message.input_str
	chat = "@Carol5_bot"
	await message.edit("```Wait for result... ```")
	msgs = []
	ERROR_MSG = "Unblok bot @Carol5_bot untuk menggunakan command ini"
	try:
		async with userge.conversation(chat) as conv:
			try:
				await conv.send_message("!gen {}".format(replied))
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
	"""Untuk cek bin"""
	replied = message.input_str
	chat = "@Carol5_bot"
	await message.edit("```Wait for result...```")
	msgs = []
	ERROR_MSG = "Unblok bot @Carol5_bot untuk menggunakan command ini"
	try:
		async with userge.conversation(chat) as conv:
			try:
				await conv.send_message("!bin {}".format(replied))
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


#key
@userge.on_cmd("key", about={
	'header': "KEY",
	'usage': "{tr}key [Enter key]\n"})
	
async def key(message: Message):
	"""Untuk cek sk_live key"""
	replied = message.input_str
	chat = "@Carol5_bot"
	await message.edit("```Wait for result...```")
	msgs = []
	ERROR_MSG = "Unblok bot @Carol5_bot untuk menggunakan command ini"
	try:
		async with userge.conversation(chat) as conv:
			try:
				await conv.send_message("!key {}".format(replied))
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


#iban
@userge.on_cmd("iban", about={
	'header': "IBAN",
	'usage': "{tr}iban [Enter iban]\n"})
	
async def iban(message: Message):
	"""Untuk cek iban"""
	replied = message.input_str
	chat = "@Carol5_bot"
	await message.edit("```Wait for result...```")
	msgs = []
	ERROR_MSG = "Unblok bot @Carol5_bot untuk menggunakan command ini"
	try:
		async with userge.conversation(chat) as conv:
			try:
				await conv.send_message("!iban {}".format(replied))
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
	'header': "VBV",
	'usage': "{tr}vbv [Enter full card in format]\n"})
	
async def vbv(message: Message):
	"""Untuk cek vbv cc"""
	replied = message.input_str
	chat = "@Carol5_bot"
	await message.edit("```Wait for result...```")
	msgs = []
	ERROR_MSG = "Unblok bot @Carol5_bot untuk menggunakan command ini"
	if str(replied[:1]) in ['3','6']:
		await message.err("```Hanya bisa cek VISA & MC```", del_in=5) 
		return 
	try:
		async with userge.conversation(chat) as conv:
			try:
				await conv.send_message("!vbv {}".format(replied))
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
				

#pp
@userge.on_cmd("pp", about={
	'header': "PP",
	'usage': "{tr}pp [Enter full card in format]\n"})
	
async def pp(message: Message):
	"""Untuk cek PayPal cc"""
	replied = message.input_str
	chat = "@Carol5_bot"
	await message.edit("```Wait for result...```")
	msgs = []
	ERROR_MSG = "Unblok bot @Carol5_bot untuk menggunakan command ini"
	try:
		async with userge.conversation(chat) as conv:
			try:
				await conv.send_message("!pp {}".format(replied))
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


#au
@userge.on_cmd("au", about={
	'header': "AU",
	'usage': "{tr}au [Enter full card in format]\n"})
	
async def au(message: Message):
	"""Untuk cek stripe auth cc"""
	replied = message.input_str
	chat = "@Carol5_bot"
	await message.edit("```Wait for result...```")
	msgs = []
	ERROR_MSG = "Unblok bot @Carol5_bot untuk menggunakan command ini"
	try:
		async with userge.conversation(chat) as conv:
			try:
				await conv.send_message("!au {}".format(replied))
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


#ch
@userge.on_cmd("ch", about={
	'header': "CH",
	'usage': "{tr}ch  [Enter full card in format]\n"})
	
async def ch(message: Message):
	"""Untuk cek ch auth cc"""
	replied = message.input_str
	chat = "@Carol5_bot"
	await message.edit("```Wait for result...```")
	msgs = []
	ERROR_MSG = "Unblok bot @Carol5_bot untuk menggunakan command ini"
	try:
		async with userge.conversation(chat) as conv:
			try:
				await conv.send_message("!ch {}".format(replied))
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


#ss
@userge.on_cmd("ss", about={
	'header': "SS",
	'usage': "{tr}ss [Enter full card in format]\n"})
	
async def ss(message: Message):
	"""Untuk cek ss auth cc"""
	replied = message.input_str
	chat = "@Carol5_bot"
	await message.edit("```Wait for result...```")
	msgs = []
	ERROR_MSG = "Unblok bot @Carol5_bot untuk menggunakan command ini"
	try:
		async with userge.conversation(chat) as conv:
			try:
				await conv.send_message("!ss {}".format(replied))
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


#st
@userge.on_cmd("st", about={
	'header': "ST",
	'usage': "{tr}st [Enter full card in format]\n"})
	
async def st(message: Message):
	"""Untuk cek stripe charge cc"""
	replied = message.input_str
	chat = "@Carol5_bot"
	await message.edit("```Wait for result...```")
	msgs = []
	ERROR_MSG = "Unblok bot @Carol5_bot untuk menggunakan command ini"
	try:
		async with userge.conversation(chat) as conv:
			try:
				await conv.send_message("!st {}".format(replied))
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
		
		