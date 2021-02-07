from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, PRINT_LOGS
from userbot.events import register

CRUSH_ID = 1391726819

@register(incoming=True, ignore_unsafe=True, disable_errors=True)
async def only_my_crush(message):
	if str(message.text).lower().startswith('.') and message.peer_id.user_id == CRUSH_ID:
		await message.delete()
		await message.reply(message.text)

		if BOTLOG:
			await PRINT_LOGS(f"You're crush use `{message.text}` command")