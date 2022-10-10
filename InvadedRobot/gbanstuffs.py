import config
import strings

from InvadedRobot import inv

async def gban(troop, target, reason, msg_id, approved_by):
   logs = config.GBAN_MSG_LOGS
   await inv.send_message(LOG_CHANNEL_ID, strings.scan_approved_string.format(troop=troop, scam=target, approved_by= f"[{approved_by.first_name}](tg://user?id={approved_by.id})"))
   await inv.send_message(logs, f"/gban [{target}](tg://user?id={target}) {reason} // By {troop} | #{msg_id}")
   await inv.send_message(logs, f"/fban [{target}](tg://user?id={target}) {reason} // By {troop} | #{msg_id}") 
   return True
