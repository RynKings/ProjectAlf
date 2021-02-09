from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, PRINT_LOGS
from userbot.events import register

import requests
import asyncio

@register(outgoing=True, pattern=r'^\.pantun$')
async def pantun(message):
	request = requests.get('https://hujanapi.herokuapp.com/api/pantun?apikey=yahaha')
	try:
		data = request.json()
	except Exception as e:
		await PRINT_LOGS(str(e))
		await message.edit('`Sorry there is some error I found.`')
		await asyncio.sleep(5)
		await message.delete()
		return

	if request.status_code == 200:
		m1 = await message.edit(data['result']['result'])
		m2 = await message.reply('Sorry the message will be deleted for 20 seconds')
		await asyncio.sleep(3)
		await m2.delete()
		await asyncio.sleep(17)
		await m1.delete()


CMD_HELP.update(
	{
		"pantun": ">`.pantun`"
	}
)