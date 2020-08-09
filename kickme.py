#by kamikadze3113 (Telegram)
from .. import loader, utils
from asyncio import sleep
import random
from telethon.tl.functions.channels import LeaveChannelRequest
@loader.tds
class LeaveMod(loader.Module):
	strings = {"name": "kickme"}
	@loader.sudo
	async def kickmecmd(self, message):
		"""by kamikazde3113 (Telegram)"""
		text = utils.get_args_raw(message)
		if not text:
			GIF = ["https://i.gifer.com/1UEg.gif", "https://i.gifer.com/5Tp.gif", "https://i.gifer.com/Tia.gif", "https://i.gifer.com/7wD7.gif", "https://i.gifer.com/fya2.gif"]
			text = "Я ливаю с этого дурдома"
			await message.client.send_file(message.to_id, random.choice(GIF))
		if not message.chat:
			await message.edit("Йой это не группа")
			return
		else:
			GIF = ["https://i.gifer.com/1UEg.gif", "https://i.gifer.com/5Tp.gif", "https://i.gifer.com/Tia.gif", "https://i.gifer.com/7wD7.gif", "https://i.gifer.com/fya2.gif"]
		    await message.client.send_file(message.to_id, random.choice(GIF))
		    await message.edit(f"<b>{text}</b>")
		await sleep(1)
		await message.client(LeaveChannelRequest(message.chat_id))