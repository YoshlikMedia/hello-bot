# from datetime import date, datetime
#
# from bot.constants.ad import AdStatusChoices
# from bot.models.ad import Ad
# from bot.constants.bot import BotUserLanguageChoices
# from bot.webhook_handler import bot
# from config.celery import app
# from config.settings.base import AD_SOLD_EXPIRE_DAY, AD_RENEW_DAY
#
#
# def channel(ad: Ad, username=False, link=False):
#     if username:
#         if ad.language == BotUserLanguageChoices.LANGUAGE_1:
#             return ad.category.channel.username_1
#         else:
#             return ad.category.channel.username_2
#     elif link:
#         if ad.language == BotUserLanguageChoices.LANGUAGE_1:
#             return ad.category.channel.link_1
#         else:
#             return ad.category.channel.link_2
#     else:
#         if ad.language == BotUserLanguageChoices.LANGUAGE_1:
#             return ad.category.channel.channel_id_1
#         else:
#             return ad.category.channel.channel_id_2
#
# @app.task
# def remove_sold_ad():
#     ads = Ad.objects.filter(status=AdStatusChoices.PASSIVE, channel_message_id__isnull=False)
#     today = date.today()
#     print('111111111111111111111111111111')
#     for ad in ads:
#         try:
#             ad_ids = ad.channel_message_id.split(',')
#             for one_ad_id in ad_ids:
#                 ad_id, ad_date = one_ad_id.split(':')
#                 ad_date = datetime.strptime(ad_date, '%Y-%m-%d').date()
#                 delta = today - ad_date
#                 if delta.days > AD_SOLD_EXPIRE_DAY:
#                     bot.delete_message(chat_id=channel(ad), message_id=ad_id)
#                     print("success deleted")
#         except:
#             print("failed")
#             continue
#
# @app.task
# def renew_ad():
#     ads = Ad.objects.filter(status=AdStatusChoices.ACTIVE, channel_message_id__isnull=False)
#     today = date.today()
#     print('222222222222222')
#     for ad in ads:
#         try:
#             ad_ids = ad.channel_message_id.split(',')
#             for one_ad_id in ad_ids:
#                 ad_id, ad_date = one_ad_id.split(':')
#                 ad_date = datetime.strptime(ad_date, '%Y-%m-%d').date()
#                 delta = today - ad_date
#                 if delta.days > AD_RENEW_DAY:
#                     bot.delete_message(chat_id=channel(ad), message_id=ad_id)
#                     print("success deleted")
#         except:
#             print("failed")
#             continue
