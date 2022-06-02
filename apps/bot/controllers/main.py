# from io import BytesIO
#
# from telebot.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardRemove, InputMediaPhoto
#
# from apps.ad.constants import ConditionChoices, HasDocumentChoices, CurrencyChoices, AdTypeChoices, AdStatusChoices
# from apps.ad.models import Ad
# from apps.ad.utils import convert_and_watermark_image
# from apps.bot.constants import BotUserSteps, BotUserLanguageChoices, CallbackData, CONFIRMATION_CHANNEL_ID, MAIN_CHANNEL_ID, \
#     GREETING_VOICE, CHANNEL_PHOTO, EXCEPTION_CHANNEL_ID, BOT_TOKEN, InstaConst, CHAT_GROUP_USERNAME
# from apps.bot.controllers.base import BaseController
# from apps.common.models import Manufacturer, Region, Condition
# from pharmacy101.settings import MAX_AD_PHOTO_COUNT
# from geopy.geocoders import Nominatim
#
#
# class BotController(BaseController):
#     def greeting(self):
#         self.sync_user()
#         self.bot.send_voice(chat_id=self.chat_id, voice=GREETING_VOICE)
#
#     def back_reply_button_handler(self):
#         step = self.step
#         if step == BotUserSteps.LISTING_MANUFACTURER:
#             self.main_menu(edit_message=True)
#         elif step == BotUserSteps.GETTING_AD_TITLE:
#             self.list_manufacturer()
#         elif step == BotUserSteps.GETTING_AD_COLOR:
#             self.get_ad_title()
#         elif step == BotUserSteps.GETTING_AD_MEMORY:
#             self.get_ad_color()
#         elif step == BotUserSteps.GET_DESCRIPTION:
#             self.get_imei(edit_message=True)
#         elif step == BotUserSteps.GETTING_PRICE:
#             self.get_ad_currency(edit_message=True)
#         elif step == BotUserSteps.GETTING_PHONE:
#             self.get_ad_type()
#         elif step == BotUserSteps.GETTING_REGION:
#             self.get_ad_phone()
#         elif step == BotUserSteps.GETTING_REGION_CHILD:
#             self.get_ad_region()
#         elif step == BotUserSteps.GETTING_PHOTO:
#             self.get_ad_region()
#         elif step == BotUserSteps.MY_ADS:
#             self.personal_cabinet()
#
#     def back_inline_button_handler(self):
#         step = self.step
#         if step == BotUserSteps.LISTING_CONDITION:
#             self.get_ad_memory(edit_message=True)
#         elif step == BotUserSteps.HAS_DOCUMENT:
#             self.get_ad_condition(edit_message=True)
#         elif step == BotUserSteps.GET_IMEI:
#             self.get_ad_document(edit_message=True)
#         elif step == BotUserSteps.GETTING_CURRENCY:
#             self.get_ad_description(edit_message=True)
#         elif step == BotUserSteps.GETTING_TYPE:
#             self.get_ad_price(edit_message=True)
#
#     def list_language(self, edit_lang=False):
#         uzbek = KeyboardButton(text=self.messages('uzbek'))
#         russian = KeyboardButton(text=self.messages('russian'))
#         markup = self.reply_markup()
#         markup.add(uzbek, russian)
#         self.send_message(
#             message_text=self.messages('select the language'),
#             reply_markup=markup)
#         if edit_lang:
#             self.set_step(BotUserSteps.EDIT_LANGUAGE)
#         else:
#             self.set_step(BotUserSteps.LISTING_LANGUAGE)
#
#     def set_language(self, edit_lang=False):
#         selected_language = self.message_text
#         if selected_language == self.messages('uzbek'):
#             self.user.language = BotUserLanguageChoices.UZBEK
#             self.user.save()
#             self.send_message(message_code='no problem saved your language')
#             if edit_lang:
#                 self.main_menu()
#             else:
#                 self.get_user_phone()
#         elif selected_language == self.messages('russian'):
#             self.user.language = BotUserLanguageChoices.RUSSIAN
#             self.user.save()
#             self.send_message(message_code='no problem saved your language')
#             if edit_lang:
#                 self.main_menu()
#             else:
#                 self.get_user_phone()
#         else:
#             self.send_message(message_text=self.messages("selected language doesn't exist"))
#             self.list_language()
#
#     def get_user_phone(self):
#         if not self.user.phone_number:
#             markup = self.reply_markup()
#             markup.row(KeyboardButton(text=self.t('send number button'),
#                                       request_contact=True))
#             markup.row(self.back_reply_button)
#             self.send_message(message_code='enter your phone number',
#                               reply_markup=markup)
#         else:
#             self.main_menu(send_guide=True)
#         self.set_step(BotUserSteps.GETTING_USER_PHONE)
#
#     def set_user_phone(self):
#         if self.message.contact.phone_number:
#             phone = self.message.contact.phone_number
#         else:
#             self.get_user_phone()
#             return
#         phone = phone.replace('+', '')
#         phone = phone.replace(' ', '')
#         phone = phone.replace('-', '')
#         if not phone.startswith('998'):
#             phone = '998' + phone
#         phone = '+' + phone
#         self.user.phone_number = phone
#         self.user.save()
#         self.send_message(message_code='wow cool phone number')
#         self.main_menu(send_guide=True)
#
#     def main_menu(self, edit_message=False, send_guide=False):
#         self.sync_user()
#         markup = self.reply_markup()
#         # markup.row(KeyboardButton(text=self.t('advertise')), KeyboardButton(text=self.t('search ads')))
#         markup.row(KeyboardButton(text=self.t('advertise')))
#         markup.row(KeyboardButton(text=self.t('my account')), KeyboardButton(text=self.t('technical support')))
#         if edit_message:
#             self.delete_message(message_id=self.callback_query_id)
#             self.send_message(message_code='main menu',
#                               reply_markup=markup)
#         else:
#             self.send_message(message_code='main menu',
#                               reply_markup=markup)
#         self.set_step(BotUserSteps.MAIN_MENU)
#         if send_guide:
#             self.send_message(message_code='main menu guide')
#
#     def list_manufacturer(self):
#         manufacturers = Manufacturer.objects.all().order_by('name')
#         markup = self.inline_markup()
#         buttons_row = []
#         for manufacturer in manufacturers:
#             buttons_row.append(InlineKeyboardButton(manufacturer.name, callback_data=f'made:{manufacturer.id}'))
#         markup.add(*buttons_row)
#         markup.row(self.main_menu_inline_button)
#         self.send_message(message_code='advertisement menu', reply_markup=ReplyKeyboardRemove())
#         message = self.send_message(message_code='select from one of these manufacturer', reply_markup=markup)
#         self.set_step(BotUserSteps.LISTING_MANUFACTURER)
#
#     def set_manufacturer(self):
#         ad = self.ad
#         manufacturer_id = self.callback_data.split(':')[1]
#         manufacturer_id = int(manufacturer_id)
#         manufacturer = Manufacturer.objects.get(id=manufacturer_id)
#         ad.manufacturer = manufacturer
#         ad.save()
#         markup = self.inline_markup()
#         markup.add(InlineKeyboardButton(f"{self.t('choosed')}: {manufacturer.name}", callback_data='None'))
#         self.edit_message(message_code='select from one of these manufacturer', message_id=self.callback_query_id,
#                           reply_markup=markup)
#         self.get_ad_title()
#
#     def get_ad_title(self):
#         markup = self.reply_markup()
#         markup.row(self.back_reply_button, self.main_menu_reply_button)
#         self.send_message(chat_id=self.chat_id,
#                           message_text=self.t('send ad title'),
#                           reply_markup=markup)
#         self.set_step(BotUserSteps.GETTING_AD_TITLE)
#
#     def set_ad_title(self):
#         ad = self.ad
#         title = self.message_text.upper()
#         manufacturer = ad.manufacturer.name.upper()
#         if manufacturer in title:
#             title = title.replace(manufacturer, "")
#             title = title.strip()
#         ad.title = title.title()
#         ad.save()
#         self.get_ad_color()
#
#     def get_ad_color(self):
#         markup = self.reply_markup()
#         markup.row(self.back_reply_button, self.main_menu_reply_button)
#         self.send_message(chat_id=self.chat_id,
#                           message_text=self.t('send product color'),
#                           reply_markup=markup)
#         self.set_step(BotUserSteps.GETTING_AD_COLOR)
#
#     def set_ad_color(self):
#         ad = self.ad
#         ad.color = self.message_text
#         ad.save()
#         self.get_ad_memory()
#
#     def get_ad_memory(self, edit_message=False):
#         markup = self.reply_markup()
#         markup.row(self.back_reply_button, self.main_menu_reply_button)
#         if edit_message:
#             self.delete_message(message_id=self.callback_query_id - 1)
#             self.delete_message(message_id=self.callback_query_id)
#         self.send_message(chat_id=self.chat_id,
#                           message_text=self.t('enter memory'),
#                           reply_markup=markup)
#         self.set_step(BotUserSteps.GETTING_AD_MEMORY)
#
#     def set_ad_memory(self):
#         ad = self.ad
#         memory = self.message_text
#         memory = memory.upper()
#         ad.memory = memory.replace('GB', '').replace('ГБ', '')
#         ad.save()
#         self.get_ad_condition()
#
#     def get_ad_condition(self, edit_message=False):
#         conditions = Condition.objects.all()
#         markup = self.inline_markup()
#         buttons_row = []
#         for condition in conditions:
#             buttons_row.append(
#                 InlineKeyboardButton(condition.name_uz if self.user.language == 'uz' else condition.name_ru,
#                                      callback_data=f'condition:{condition.id}'))
#         markup.add(*buttons_row)
#         markup.row(self.back_inline_button, self.main_menu_inline_button)
#         if edit_message:
#             self.edit_message(message_code='choose condition', message_id=self.callback_query_id, reply_markup=markup)
#         else:
#             self.send_message(message_code='next', reply_markup=ReplyKeyboardRemove())
#             self.send_message(message_code='choose condition', reply_markup=markup)
#         self.set_step(BotUserSteps.LISTING_CONDITION)
#
#     def set_ad_condition(self):
#         ad = self.ad
#         condition_id = self.callback_data.split(':')[1]
#         condition_id = int(condition_id)
#         condition = Condition.objects.get(id=condition_id)
#         ad.condition = condition
#         ad.save()
#         markup = self.inline_markup()
#         markup.add(InlineKeyboardButton(
#             f"{self.t('choosed')}: {condition.name_uz if self.user.language == 'uz' else condition.name_ru}",
#             callback_data='None'))
#         self.edit_message(message_code='choose condition', message_id=self.callback_query_id,
#                           reply_markup=markup)
#         self.get_ad_document()
#
#     def get_ad_document(self, edit_message=False):
#         markup = self.inline_markup()
#         markup.add(InlineKeyboardButton(self.t('yes'), callback_data='document:1'))
#         markup.add(InlineKeyboardButton(self.t('no'), callback_data='document:2'))
#         markup.row(self.back_inline_button, self.main_menu_inline_button)
#         if edit_message:
#             self.edit_message(message_code='has document', message_id=self.callback_query_id, reply_markup=markup)
#         else:
#             self.send_message(message_code='has document', reply_markup=markup)
#         self.set_step(BotUserSteps.HAS_DOCUMENT)
#
#     def set_ad_document(self):
#         document = self.callback_data.split(':')[1]
#         ad = self.ad
#         ad.has_document = int(document)
#         ad.save()
#         if document == '1':
#             msg_text = self.t('yes')
#         else:
#             msg_text = self.t('no')
#         markup = self.inline_markup()
#         markup.add(InlineKeyboardButton(f"{self.t('choosed')}: {msg_text}", callback_data='None'))
#         self.edit_message(message_code='has document', message_id=self.callback_query_id, reply_markup=markup)
#         self.get_imei()
#
#     def get_imei(self, edit_message=False):
#         markup = self.inline_markup()
#         markup.add(InlineKeyboardButton(self.t('yes'), callback_data='imei:1'))
#         markup.add(InlineKeyboardButton(self.t('no'), callback_data='imei:2'))
#         markup.row(self.back_inline_button, self.main_menu_inline_button)
#         if edit_message:
#             self.send_message(message_code='next', reply_markup=ReplyKeyboardRemove())
#         self.send_message(message_code='is imei registered', reply_markup=markup)
#         self.set_step(BotUserSteps.GET_IMEI)
#
#     def set_ad_imei(self):
#         imei = self.callback_data.split(':')[1]
#         ad = self.ad
#         ad.is_imei_registered = imei == '1'
#         ad.save()
#         if imei == '1':
#             msg_text = self.t('yes')
#         else:
#             msg_text = self.t('no')
#         markup = self.inline_markup()
#         markup.add(InlineKeyboardButton(f"{self.t('choosed')}: {msg_text}", callback_data='None'))
#         self.edit_message(message_code='is imei registered', message_id=self.callback_query_id,
#                           reply_markup=markup)
#         self.get_ad_description()
#
#     def get_ad_description(self, edit_message=False):
#         markup = self.reply_markup()
#         markup.row(self.continue_reply_button)
#         markup.row(self.back_reply_button, self.main_menu_reply_button)
#         if edit_message:
#             self.delete_message(message_id=self.callback_query_id)
#         self.send_message(message_code='send ad description', reply_markup=markup)
#         self.set_step(BotUserSteps.GET_DESCRIPTION)
#
#     def set_ad_description(self):
#         ad = self.ad
#         ad.description = self.message_text
#         ad.save()
#         self.get_ad_currency()
#
#     def get_ad_currency(self, edit_message=False):
#         markup = self.inline_markup()
#         markup.add(InlineKeyboardButton(self.t('sum'), callback_data='currency:1'))
#         markup.add(InlineKeyboardButton(self.t('usd'), callback_data='currency:2'))
#         markup.row(self.back_inline_button, self.main_menu_inline_button)
#         self.send_message(message_code='next', reply_markup=ReplyKeyboardRemove())
#         self.send_message(message_code='change currency', reply_markup=markup)
#         self.set_step(BotUserSteps.GETTING_CURRENCY)
#
#     def set_ad_currency(self):
#         currency = self.callback_data.split(':')[1]
#         ad = self.ad
#         ad.currency = int(currency)
#         ad.save()
#         if currency == '1':
#             msg_text = self.t('sum')
#         else:
#             msg_text = self.t('usd')
#         markup = self.inline_markup()
#         markup.add(InlineKeyboardButton(f"{self.t('choosed')}: {msg_text}", callback_data='None'))
#         self.edit_message(message_code='change currency', message_id=self.callback_query_id,
#                           reply_markup=markup)
#         self.get_ad_price()
#
#     def get_ad_price(self, edit_message=False):
#         markup = self.reply_markup()
#         markup.add(KeyboardButton(text=self.t('we will deal')))
#         markup.row(self.back_reply_button, self.main_menu_reply_button)
#         if edit_message:
#             self.delete_message(message_id=self.callback_query_id)
#         self.send_message(message_code='enter your ad price', reply_markup=markup)
#         self.set_step(BotUserSteps.GETTING_PRICE)
#
#     def set_ad_price(self):
#         ad = self.ad
#         price = self.message_text
#         if price == self.t('we will deal'):
#             ad.price = None
#             ad.save()
#             self.get_ad_type()
#         else:
#             price = self.number_formatter(price)
#             try:
#                 ad.price = float(price)
#                 ad.save()
#                 self.get_ad_type()
#             except:
#                 self.send_message(message_code='you must enter digit for price', reply_to_message_id=self.message_id)
#                 self.get_ad_price()
#
#     def get_ad_type(self):
#         markup = self.inline_markup()
#         markup.add(InlineKeyboardButton(self.t('yes'), callback_data='type:2'))
#         markup.add(InlineKeyboardButton(self.t('no'), callback_data='type:1'))
#         markup.row(self.back_inline_button, self.main_menu_inline_button)
#         self.send_message(message_code='next', reply_markup=ReplyKeyboardRemove())
#         self.send_message(message_code='exchange', reply_markup=markup)
#         self.set_step(BotUserSteps.GETTING_TYPE)
#
#     def set_ad_type(self):
#         ad_type = self.callback_data.split(':')[1]
#         ad = self.ad
#         ad.ad_type = int(ad_type)
#         ad.save()
#         if ad_type == '2':
#             msg_text = self.t('yes')
#         else:
#             msg_text = self.t('no')
#         markup = self.inline_markup()
#         markup.add(InlineKeyboardButton(f"{self.t('choosed')}: {msg_text}", callback_data='None'))
#         self.edit_message(message_code='exchange', message_id=self.callback_query_id,
#                           reply_markup=markup)
#         self.get_ad_phone()
#
#     def get_ad_phone(self):
#         markup = self.reply_markup()
#         markup.row(KeyboardButton(text=self.t('send number button'),
#                                   request_contact=True))
#         markup.row(self.back_reply_button, self.main_menu_reply_button)
#         self.send_message(message_code='enter your phone number', reply_markup=markup)
#         self.set_step(BotUserSteps.GETTING_PHONE)
#
#     def set_ad_phone(self):
#         ad = self.ad
#         try:
#             if self.message.contact.phone_number:
#                 phone = self.message.contact.phone_number
#                 if '+' in phone:
#                     ad.phone_number = phone
#                 else:
#                     ad.phone_number = '+' + phone
#                 ad.save()
#                 self.get_ad_region()
#             else:
#                 self.get_ad_phone()
#         except:
#             try:
#                 phone = self.message_text[len(self.message_text) - 9:]
#                 if phone.isdigit():
#                     if len(self.message_text) >= 9:
#                         ad.phone_number = '+998' + phone
#                         ad.save()
#                         self.get_ad_region()
#                     else:
#                         self.send_message(message_code='error', reply_to_message_id=self.message_id)
#                         self.get_ad_phone()
#                 else:
#                     self.send_message(message_code='enter number', reply_to_message_id=self.message_id)
#                     self.get_ad_phone()
#             except:
#                 self.get_ad_phone()
#
#     def get_ad_region(self, child=False, edit_message=False):
#         ad = self.ad
#         markup = self.reply_markup(3)
#         markup.row(KeyboardButton(self.t('location'), request_location=True))
#         if child:
#             try:
#                 if self.user.language == 'uz':
#                     parent_region = Region.objects.get(name_uz=self.message_text, parent=None, is_active=True)
#                 else:
#                     parent_region = Region.objects.get(name_ru=self.message_text, parent=None, is_active=True)
#                 ad.region = parent_region
#                 ad.save()
#                 regions = Region.objects.filter(parent=parent_region, is_active=True).order_by('name_uz')
#                 buttons_row = []
#                 for region in regions:
#                     buttons_row.append(KeyboardButton(region.name_uz if self.user.language == 'uz' else region.name_ru))
#                 markup.add(*buttons_row)
#                 markup.row(self.back_reply_button, self.main_menu_reply_button)
#                 self.send_message(message_code='enter city', reply_markup=markup)
#                 self.set_step(BotUserSteps.GETTING_REGION_CHILD)
#             except:
#                 self.send_message(message_code='error region', reply_to_message_id=self.message_id)
#         else:
#             regions = Region.objects.filter(parent=None, is_active=True).order_by('name_uz')
#             buttons_row = []
#             for region in regions:
#                 buttons_row.append(KeyboardButton(region.name_uz if self.user.language == 'uz' else region.name_ru))
#             markup.add(*buttons_row)
#             if edit_message:
#                 self.delete_message(message_id=self.callback_query_id)
#             markup.row(self.back_reply_button, self.main_menu_reply_button)
#             self.send_message(message_code='enter province', reply_markup=markup)
#             self.set_step(BotUserSteps.GETTING_REGION)
#
#     def set_ad_location(self):
#         ad = self.ad
#         ad.location = f"{self.message.location.latitude},{self.message.location.longitude}"
#         ad.save()
#         self.get_ad_photo()
#
#     def set_ad_region(self):
#         ad = self.ad
#         try:
#             if self.user.language == 'uz':
#                 region = Region.objects.get(name_uz=self.message_text, parent_id=ad.region.id)
#             else:
#                 region = Region.objects.get(name_ru=self.message_text, parent_id=ad.region.id)
#             ad.region = region
#             ad.save()
#             self.get_ad_photo()
#         except:
#             self.get_ad_region(child=True)
#
#     def get_ad_photo(self):
#         ad = self.ad
#         ad.photos.all().delete()
#         markup = self.reply_markup()
#         markup.add(self.continue_reply_button)
#         markup.row(self.back_reply_button, self.main_menu_reply_button)
#         self.send_message(message_code='send photo', reply_markup=markup)
#         self.set_step(BotUserSteps.GETTING_PHOTO)
#
#     def set_ad_photo(self):
#         if self.message.content_type == 'photo':
#             ad = self.ad
#             has_any_photos = ad.photos.exists()
#             if not has_any_photos:
#                 ad.photos.create(telegram_photo_id=self.message.photo[-1].file_id)
#                 self.send_message(message_code='next step')
#             if has_any_photos:
#                 if ad.photos.count() < MAX_AD_PHOTO_COUNT - 1:
#                     ad.photos.create(telegram_photo_id=self.message.photo[-1].file_id)
#                 else:
#                     self.ask_ad_confirmation()
#         else:
#             self.send_message(message_code='photo except')
#
#     def ask_ad_confirmation(self):
#         markup = self.inline_markup()
#         markup.row(InlineKeyboardButton(self.messages('confirm ad emoji'), callback_data=CallbackData.confirm),
#                    InlineKeyboardButton(self.messages('decline ad emoji'), callback_data=CallbackData.decline))
#         self.send_message(message_code='next', reply_markup=ReplyKeyboardRemove())
#         self.send_full_ad(chat_id=self.chat_id, ad=self.ad, user_self=True)
#         self.send_message(message_code='check your ad to confirm', reply_markup=markup)
#         self.set_step(BotUserSteps.ASK_CONFIRMATION)
#
#     def send_full_ad(self, chat_id, ad, status=None, user_self=False, watermark=False):
#         text_added = False
#         media_list = []
#         if ad.photos.all().exists():
#             for photo in ad.photos.all():
#                 if not text_added:
#                     # if instagram:
#                     #     url = self.create_photo_url(file_id=photo.telegram_photo_id)
#                     #     post_instagram_image(media_url=url,caption=self.instagram_text_formatter(ad))
#                     if watermark:
#                         image = convert_and_watermark_image(self.create_photo_url(photo.telegram_photo_id))
#                         buf = BytesIO()
#                         image.save(buf, 'jpeg')
#                         buf.seek(0)
#                         image_bytes = buf.read()
#                         media_list.append(
#                             InputMediaPhoto(image_bytes,
#                                             caption=self.ad_text_formatter(ad, user_self=user_self), parse_mode='HTML'))
#                         buf.close()
#                     else:
#                         media_list.append(
#                             InputMediaPhoto(photo.telegram_photo_id,
#                                             caption=self.ad_text_formatter(ad, user_self=user_self), parse_mode='HTML'))
#                     text_added = True
#                 else:
#                     if watermark:
#                         image = convert_and_watermark_image(self.create_photo_url(photo.telegram_photo_id))
#                         buf = BytesIO()
#                         image.save(buf, 'jpeg')
#                         buf.seek(0)
#                         image_bytes = buf.read()
#                         media_list.append(InputMediaPhoto(image_bytes))
#                         buf.close()
#                     else:
#                         media_list.append(InputMediaPhoto(photo.telegram_photo_id))
#             media_list.append(InputMediaPhoto(CHANNEL_PHOTO))
#             message = self.bot.send_media_group(chat_id=chat_id, media=media_list)
#             message_id = message[0].message_id
#         else:
#             message = self.bot.send_photo(chat_id=chat_id, photo=CHANNEL_PHOTO,
#                                           caption=self.ad_text_formatter(ad, user_self=user_self),
#                                           parse_mode='HTML')
#             message_id = message.message_id
#         if status:
#             markup = self.inline_markup()
#             if status == AdStatusChoices.ACTIVE:
#                 text = self.t('sold out')
#                 callback_data = CallbackData.sold_out
#             elif status == AdStatusChoices.WAITING_FOR_CONFIRMATION:
#                 text = self.t('on inspection')
#                 callback_data = None
#             else:
#                 text = self.t('sold')
#                 callback_data = None
#             markup.add(InlineKeyboardButton(text, callback_data=f'{callback_data}:{ad.id}'))
#             message = self.send_message(message_text=self.messages('up emoji'), reply_markup=markup)
#             # if message
#         return message_id
#
#     def ad_text_formatter(self, ad, edit_message=False, user_self=False):
#         self.sync_user()
#         title = f'{ad.manufacturer.name} {ad.title}'
#         color = ad.color
#         memory = f"{ad.memory} GB"
#         condition = ad.condition.name_uz if self.user.language == 'uz' else ad.condition.name_ru
#         has_document = self.messages('has document') if ad.has_document == HasDocumentChoices.YES else self.messages(
#             'not document')
#         is_imei_registered = self.messages('imei registered') if ad.is_imei_registered else self.messages(
#             'not imei registered')
#         if ad.description:
#             description = ad.description + '\n'
#         else:
#             description = ad.description
#         if ad.price is None:
#             price = self.messages('we agree')
#         else:
#             price = int(ad.price)
#             price = self.make_price(price)
#             price = f"{price} {self.messages('usd') if ad.currency == CurrencyChoices.US_DOLLAR else self.messages('uzs')}"
#         if ad.ad_type == AdTypeChoices.SELL:
#             ad_type = self.messages('not exchange')
#         else:
#             ad_type = self.messages('has exchange')
#         if ad.user.username:
#             telegram_user_id = '@' + ad.user.username
#         else:
#             chat_id = int(ad.user.chat_id)
#             telegram_user_id = f'<a href = "tg://user?id={chat_id}">E\'lon egasi</a>'
#             if user_self:
#                 telegram_user_id = ad.user.name
#         phone_number = ad.phone_number
#         if ad.location is not None:
#             geolocator = Nominatim(user_agent="myGeocoder")
#             location = geolocator.reverse(ad.location)
#             address = location.raw['address']
#             state_1 = address.get('state', '')
#             state = state_1.split(' ')[0] + " v, "
#             city = address.get('city', '')
#             county = address.get('county', '')
#             region = f"<a href='https://maps.google.com/?q={ad.location}'>{state if state_1 else ''}{city if city else county}</a>"
#         else:
#             region = ad.region.name_uz
#             parent_region = ad.region.parent.name_uz.split(' ')[0] + " v, "
#             region = f"{parent_region}{region}"
#         link = f"<a href='https://t.me/+vFm7E8Nx8uk5YTI6'>📲 Apparat.uz</a> 👉 bu yirik telefon bozor \n" \
#                f"<a href='https://t.me/apparatuz_bot'>🤖 Apparat.uz bot</a> 👉 bepul e'lon berish"
#         result = f"{'<b>🎉 #Sotildi</b>' if edit_message else ''}\n" \
#                  f"{self.messages('ad id emoji')} {ad.id}\n" \
#                  f"{self.messages('ad title emoji')} {title}\n" \
#                  f"{self.messages('ad condition emoji')} {condition}\n" \
#                  f"{self.messages('ad color emoji')} {color}\n" \
#                  f"{self.messages('ad memory emoji')} {memory}\n" \
#                  f"{self.messages('ad document emoji')} {has_document}\n" \
#                  f"{self.messages('confirm ad emoji') if ad.is_imei_registered else self.messages('decline ad emoji')} {is_imei_registered}\n" \
#                  f"{self.messages('ad price emoji')} {price}\n" \
#                  f"{self.messages('ad exchange emoji')} {ad_type}\n" \
#                  f"{self.messages('ad person emoji')} {'<b>Sotildi</b>' if edit_message else telegram_user_id}\n" \
#                  f"{self.messages('ad phone emoji')} {'<b>Sotildi</b>' if edit_message else phone_number}\n" \
#                  f"{self.messages('ad location emoji')} {region}\n" \
#                  f"{self.messages('ad description emoji') + ' ' + description if description else ''}  \n" \
#                  f"{link}"
#         return result
#
#     def instagram_text_formatter(self, ad):
#         title = f'{ad.manufacturer.name} {ad.title}'
#         color = ad.color
#         memory = f"{ad.memory} GB"
#         condition = ad.condition.name_uz
#         has_document = self.messages('has document') if ad.has_document == HasDocumentChoices.YES else self.messages(
#             'not document')
#         is_imei_registered = self.messages('imei registered') if ad.is_imei_registered else self.messages(
#             'not imei registered')
#         if ad.description:
#             description = ad.description + '\n'
#         else:
#             description = ad.description
#         if ad.price is None:
#             price = self.messages('we agree')
#         else:
#             price = int(ad.price)
#             price = self.make_price(price)
#             price = f"{price} {self.messages('usd') if ad.currency == CurrencyChoices.US_DOLLAR else self.messages('uzs')}"
#         if ad.ad_type == AdTypeChoices.SELL:
#             ad_type = self.messages('not exchange')
#         else:
#             ad_type = self.messages('has exchange')
#         phone_number = ad.phone_number
#         if ad.location is not None:
#             geolocator = Nominatim(user_agent="myGeocoder")
#             location = geolocator.reverse(ad.location)
#             address = location.raw['address']
#             state_1 = address.get('state', '')
#             state = state_1.split(' ')[0] + " v, "
#             city = address.get('city', '')
#             county = address.get('county', '')
#             region = f"{state if state_1 else ''}{city if city else county}"
#         else:
#             region = ad.region.name_uz
#             parent_region = ad.region.parent.name_uz.split(' ')[0] + " v, "
#             region = f"{parent_region}{region}"
#         link = "📲 Apparat.uz da bepul e'lon bering"
#         hash_tags = InstaConst.hash_tags
#         result = f"{self.messages('ad title emoji')} {title}\n" \
#                  f"{self.messages('ad condition emoji')} {condition}\n" \
#                  f"{self.messages('ad color emoji')} {color}\n" \
#                  f"{self.messages('ad memory emoji')} {memory}\n" \
#                  f"{self.messages('ad document emoji')} {has_document}\n" \
#                  f"{self.messages('confirm ad emoji') if ad.is_imei_registered else self.messages('decline ad emoji')} {is_imei_registered}\n" \
#                  f"{self.messages('ad price emoji')} {price}\n" \
#                  f"{self.messages('ad exchange emoji')} {ad_type}\n" \
#                  f"{self.messages('ad phone emoji')} {phone_number}\n" \
#                  f"{self.messages('ad location emoji')} {region}\n" \
#                  f"{self.messages('ad description emoji') + ' ' + description if description else ''}  \n" \
#                  f"{link} \n" \
#                  f"{hash_tags}"
#         return result
#
#     def set_ad_confirmation_by_user(self):
#         ad = self.ad
#         if ad.status != AdStatusChoices.WAITING_FOR_CONFIRMATION:
#             self.delete_message(message_id=self.callback_query_id)
#             self.send_message(message_code='your ad has been received, wait for confirmation')
#             self.send_ad_to_confirmation_channel(ad=ad)
#             ad.status = AdStatusChoices.WAITING_FOR_CONFIRMATION
#             ad.save()
#             self.main_menu()
#
#     def set_ad_declination_by_user(self):
#         self.ad.delete()
#         self.delete_message(message_id=self.callback_query_id)
#         self.send_message(message_code='your ad has been declined')
#         self.main_menu()
#
#     def send_ad_to_confirmation_channel(self, ad):
#         self.send_full_ad(chat_id=CONFIRMATION_CHANNEL_ID, ad=ad)
#         markup = self.inline_markup()
#         # markup.row(InlineKeyboardButton(self.messages('add watermark'), callback_data=f'watermark:{ad.id}'))
#         markup.row(InlineKeyboardButton(self.messages('confirm ad emoji'),
#                                         callback_data=f'confirm_ad_by_moderator:{ad.id}'),
#                    InlineKeyboardButton(self.messages('decline ad emoji'),
#                                         callback_data=f'decline_ad_by_moderator:{ad.id}'))
#         self.send_message(chat_id=CONFIRMATION_CHANNEL_ID,
#                           message_text=self.messages('approve ad'),
#                           reply_markup=markup)
#
#     def set_ad_confirmation_by_moderator(self):
#         _, ad_id = self.callback_data.split(":")
#         ad = Ad.objects.get(pk=ad_id)
#         # if ',' in str(ad.channel_message_id):
#         #     instagram = False
#         # else:
#         #     instagram=True
#         message_id = self.send_full_ad(chat_id=MAIN_CHANNEL_ID, ad=ad, watermark=True)
#         if not ad.channel_message_id:
#             ad.channel_message_id = message_id
#             ad_count = 0
#         else:
#             ad.channel_message_id = f'{ad.channel_message_id},{message_id}'
#             ad_count = len(ad.channel_message_id.split(','))
#         ad.status = AdStatusChoices.ACTIVE
#         ad.save()
#         if ad_count == 0:
#             self.send_message(chat_id=ad.user.chat_id,
#                               message_text=f"{self.t('your ad has been confirmed by moderator', ad.user.language).format(f'{ad.manufacturer.name} {ad.title}')}\n"
#                                            f"<a href='https://t.me/apparatuz_telefon/{message_id}'>{self.t('your ad')}</a>")
#         else:
#             self.send_message(chat_id=ad.user.chat_id,
#                               message_text=f"{self.t('replay your ad', ad.user.language).format(f'{ad.manufacturer.name} {ad.title}')}\n"
#                                            f"<a href='https://t.me/apparatuz_telefon/{message_id}'>{self.t('your ad')}</a>")
#         markup = self.inline_markup()
#         markup.row(InlineKeyboardButton(self.messages('confirmed ad status'), callback_data='confirmed ad emoji'),
#                    InlineKeyboardButton(self.messages('edit emoji'),
#                                         url=f'https://app.ilmsoft.uz/apparatuz/admin/ad/ad/{ad.id}/change/'),
#                    InlineKeyboardButton(f"{self.messages('replay button')}{f'({ad_count})' if ad_count != 0 else ''}",
#                                         callback_data=f'confirm_ad_by_moderator:{ad.id}'))
#         self.edit_message(chat_id=CONFIRMATION_CHANNEL_ID, message=self.messages('confirmed ad status'),
#                           message_id=self.callback_query_id, reply_markup=markup)
#
#     def set_ad_declination_by_moderator(self):
#         _, ad_id = self.callback_data.split(":")
#         ad = Ad.objects.get(pk=ad_id)
#         ad.status = AdStatusChoices.DECLINED
#         ad.save()
#         self.send_message(chat_id=ad.user.chat_id,
#                           message_text=self.t('your ad has been declined by moderator', ad.user.language).format(
#                               ad.title))
#         markup = self.inline_markup()
#         markup.row(InlineKeyboardButton(text=self.messages('declined ad status'),
#                                         callback_data='declined ad emoji'))
#         self.edit_message(chat_id=CONFIRMATION_CHANNEL_ID, message=self.messages('declined ad status'),
#                           message_id=self.callback_query_id, reply_markup=markup)
#
#     def technical_support(self):
#         markup = self.inline_markup()
#         markup.add(InlineKeyboardButton(text='1.' + self.t('ask question'), url='t.me/Mashhurbek_Mashrabov'))
#         markup.add(InlineKeyboardButton(text='2.' + self.t('ask question'), url='t.me/ijahongirmirzo'))
#         self.send_message(message_code='ask your questions from profile below', reply_markup=markup)
#
#     def personal_cabinet(self):
#         markup = self.reply_markup()
#         markup.row(KeyboardButton(text=self.t('my ads')),
#                    KeyboardButton(text=f"{self.t('language flag')} {self.t('change user language')}"))
#         markup.add(self.main_menu_reply_button)
#         self.send_message(message_code='select the desired section', reply_markup=markup)
#         self.set_step(BotUserSteps.PERSONAL_CABINET)
#
#     def my_ads(self):
#         ads = self.user.ads.all()
#         markup = self.reply_markup(3)
#         markup.row(KeyboardButton(text=self.t('active ad')))
#         markup.row(KeyboardButton(text=self.t('ad in check')), KeyboardButton(text=self.t('passive ad')))
#         markup.row(self.back_reply_button, self.main_menu_reply_button)
#         active_ads = ads.filter(status=AdStatusChoices.ACTIVE)
#         if active_ads:
#             for ad in active_ads:
#                 self.send_full_ad(chat_id=self.chat_id, ad=ad, status=AdStatusChoices.ACTIVE)
#             self.send_message(message_code='your active ads')
#         else:
#             self.send_message(message_code='you dont have any active ads')
#         self.send_message(message_code='choose ad status', reply_markup=markup)
#         self.set_step(BotUserSteps.MY_ADS)
#
#     def send_ad_by_status(self):
#         ads = self.user.ads.all()
#         if self.message_text == self.t('active ad'):
#             status = AdStatusChoices.ACTIVE
#             text = self.t('your active ads')
#         elif self.message_text == self.t('ad in check'):
#             status = AdStatusChoices.WAITING_FOR_CONFIRMATION
#             text = self.t('your check ads')
#         else:
#             status = AdStatusChoices.PASSIVE
#             text = self.t('your passive ads')
#         ads = ads.filter(status=status)
#         if ads:
#             for ad in ads:
#                 self.send_full_ad(chat_id=self.chat_id, ad=ad, status=status)
#             self.send_message(message_text=text)
#         else:
#             self.send_message(message_code='not ads such as')
#
#     def change_status(self):
#         ad_id = self.callback_data.split(':')[1]
#         ad = Ad.objects.get(id=ad_id)
#         ad.status = AdStatusChoices.PASSIVE
#         ad.save()
#         markup = self.inline_markup()
#         markup.add(InlineKeyboardButton(self.t('sold'), callback_data='None'))
#         channel_message_id = str(ad.channel_message_id)
#         message_ids = channel_message_id.split(',')
#         for message_id in message_ids:
#             self.bot.edit_message_caption(caption=f'{self.ad_text_formatter(ad, edit_message=True)}.',
#                                           chat_id=MAIN_CHANNEL_ID,
#                                           message_id=int(message_id), parse_mode='HTML')
#         self.edit_message(message=self.messages('up emoji'), message_id=self.callback_query_id, reply_markup=markup)
#
#     def send_exception(self, e):
#         self.send_message(message_code='exception message')
#         user_step = self.user.step
#         self.main_menu()
#         if self.user.username:
#             telegram_user_id = '@' + self.user.username
#         else:
#             telegram_user_id = f'<a href="tg://user?id={int(self.chat_id)}">{self.user.name if self.user.name else "Name"}</a>'
#         phone_number = self.user.phone_number
#         except_message = f"{self.messages('ad person emoji')} {telegram_user_id}\n" \
#                          f"{self.messages('step emoji')} {user_step}\n" \
#                          f"{self.messages('ad phone emoji')} {phone_number}\n\n" \
#                          f"{self.messages('warning emoji')} {e[len(e) - 1024:]}"
#         markup = self.inline_markup()
#         markup.add(InlineKeyboardButton(self.messages('ad condition emoji'), callback_data='exception'))
#         self.send_message(chat_id=EXCEPTION_CHANNEL_ID, message_text=except_message, reply_markup=markup)
#
#     def viewed_exception(self):
#         markup = self.inline_markup()
#         markup.add(InlineKeyboardButton(self.messages('confirm ad emoji'), callback_data='None'))
#         self.edit_message(chat_id=EXCEPTION_CHANNEL_ID, message=self.message.message.text, reply_markup=markup,
#                           message_id=self.callback_query_id, )
#
#     def add_watermark(self):
#         _, ad_id = self.callback_data.split(":")
#         ad = Ad.objects.get(pk=ad_id)
#         if ad.photos.all().exists():
#             for photo in ad.photos.all():
#                 url = self.create_photo_url(file_id=photo.telegram_photo_id)
#                 img_id = convert_and_watermark_image(url)
#                 photo.telegram_photo_id = img_id
#                 photo.save()
#             ad.save()
#         markup = self.inline_markup()
#         markup.row(InlineKeyboardButton(self.messages('confirm ad emoji'),
#                                         callback_data=f'confirm_ad_by_moderator:{ad.id}'),
#                    InlineKeyboardButton(self.messages('decline ad emoji'),
#                                         callback_data=f'decline_ad_by_moderator:{ad.id}'))
#         self.edit_message(message=self.messages('approve ad'),
#                           reply_markup=markup,
#                           chat_id=CONFIRMATION_CHANNEL_ID,
#                           message_id=self.callback_query_id)
