# import telebot
# from celery import shared_task
# from celery.utils.log import get_task_logger
#
# from bot.constants.bot import BotUserLanguageChoices, BOT_TOKEN, EXCEPTION_CHANNEL_ID
# from bot.models.bot import TelegramBotUser, UserMessage
#
# bot = telebot.TeleBot(BOT_TOKEN)
#
# logger = get_task_logger(__name__)
#
#
#
# @shared_task
# def message_sender_celery(instance_pk):
#     users = TelegramBotUser.objects.all()
#     success = 0
#     unsuccess = 0
#     print(instance_pk)
#     instance = UserMessage.objects.get(pk=instance_pk)
#     print(instance.id)
#     for user in users:
#         try:
#             print(user.chat_id)
#             if user.language == BotUserLanguageChoices.UZBEK:
#                 bot.send_message(chat_id=user.chat_id, text=instance.text_uz)
#             else:
#                 bot.send_message(chat_id=user.chat_id, text=instance.text_ru)
#             success = success + 1
#         except:
#             unsuccess = unsuccess + 1
#     instance.success = success
#     instance.unsuccess = unsuccess
#     instance.save()
#     bot.send_message(chat_id=EXCEPTION_CHANNEL_ID, text=f"🆔 {instance.id}\n"
#                                                                 f"✉ {instance.text_uz}\n"
#                                                                 f"✅ {success}\n"
#                                                                 f"❌ {unsuccess}\n\n"
#                                                                 f"#message")
#
#
