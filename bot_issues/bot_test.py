import telebot
import config
import req_jira_worklogs
import req_jira_types

bot = telebot.TeleBot(config.TOKEN)

bot.send_message(608365487, str("Issues without worklogs: %s") % req_jira_worklogs.worklogs)
bot.send_message(608365487, str("Issues with General question types: %s") % req_jira_types.types)
