import os

from django.db import models

BOT_TOKEN = os.getenv('BOT_TOKEN')
BOT_LINK = os.getenv('BOT_LINK')
CONFIRMATION_CHANNEL_ID = os.getenv('CONFIRMATION_CHANNEL_ID')
CHANNEL_PHOTO = os.getenv('CHANNEL_PHOTO')
EXCEPTION_CHANNEL_ID = os.getenv('EXCEPTION_CHANNEL_ID')
CURRENCY = os.getenv('CURRENCY')

messages = {
    'greeting': 'Welcome to UAE Telegram Used Phone Market',
    'select the language': '👇 Please select your language',
    'language_1': '🇺🇸 English',
    'language_2': '🇸🇦 Arabic',
    "selected language doesn't exist": "Selected language doesn't exist",
    'ad id emoji': '🆔',
    'ad title emoji': '📱',
    'ad phone emoji': '📞',
    'ad person emoji': '👤',
    'ad memory emoji': '💾',
    'ad color emoji': '🎨',
    'ad price emoji': '💰',
    'ad description emoji': '📝',
    'ad condition emoji': '🛠',
    'ad document emoji': '📦📄',
    'confirm ad emoji': '✅',
    'decline ad emoji': '❌',
    'ad location emoji': '📍',
    'ad exchange emoji': '♻',
    'up emoji': '👆👆👆👆👆👆👆👆👆👆👆👆👆👆',
    'replay button': '🔄',
    'step emoji': '👣',
    'eye emoji': '👁‍🗨',
    'warning emoji': '⚠',
    'edit emoji': '✏',
    'bot emoji': '🤖',
    'block emoji': '🚫',
    'confirmed ad status': 'Approved ✅',
    'declined ad status': 'Declined ❌',
    'usd': "$ USD",
    'uzs': "AED",
    'new': 'New',
    'ideal': 'Ideal',
    'average': "Normal",
    'old': 'Old',
    'approve ad': "Approve the ad?",
    'sold general': "🏁 Sold out",
    'add watermark': 'Watermark ❓',
    'added watermark': 'Watermark ✅',
    'currency': CURRENCY,
    'block': "Block",
    'repost': "Repost",
    'edit': "Edit",

    'lang_1': {
        'language flag': '🇺🇸',
        'main menu': '⏏️ Main menu',
        'advertise': '📢 Sell your phone',
        'search ads': '🔎 Looking for a phone',
        'back_button': '⬅️ Back',
        'cancel': '❌ Cancel',
        'advertisement menu': '📢 Menu for selling a phone',
        'select from one of these manufacturer': 'Please select phone brand',
        'send ad title': '📌 Please enter model of your phone',
        'send product color': '🎨 Enter phone color',
        'send ad description': '✍ Please enter brief description of your ad or click <b>Continue ➡</b>',
        'we will deal': '🤝 Accept price negotiation',
        'enter your ad price': f'💰 Please enter phone price in {CURRENCY} (only integer numbers)',
        'enter your phone number': '📞 Enter your phone number or click button'
                                   '"<b>📲 Send number</b> button" ',
        'send number button': "📲 Send number",
        'wow cool phone number': 'Wow such a cool phone number :)',
        'main menu guide': 'This is our main menu, if you need support, please use technical support menu',
        'no problem saved your language': 'Language saved, now we will talk using this language',
        'decline my ad': '❌ Cancel the ad',
        'confirm my ad': '✅ Approve the ad',
        'check your ad to confirm': "👆 Please check your ad and approve",
        'your ad has been received, wait for confirmation': "Ad Received, it will be visible "
                                                            "after moderator approval",
        'your ad has been declined': "You cancelled the ad",
        'your ad has been confirmed by moderator':
            "Congrats your ad is approved and visible now \n"
            "After your phone is sold, please don't forget to mark it as sold",
        'your ad has been declined by moderator':
            'Unfortunately, your ad is declined, please check guidelines and try again',
        'ad title': '<b>Title:</b>',
        'ad price': '<b>Price:</b>',
        'ad phone': '<b>Phone:</b>',
        'ad description': '<b>Description:</b>',
        'you must enter digit for price': 'Use integers only for price',
        'my account': 'My account 🏠',
        'my ads': '📢 My ads',
        'you dont have any active ads': "You don't have any active ads",
        'ask your questions from profile below': 'You can ask your questions to the following account:',
        'ask question': 'Ask a question ❓',
        'technical support': '🆘 Technical support',
        'change user language': 'Change language',
        'choose condition': '⚙ Select phone condition :',
        'has document': '📦📄 Has original box?',
        'yes': '✅ Yes',
        'no': "❌ No",
        'is imei registered': "✅ Is the phone IMEI registered?",
        'sum': "AED",
        'usd': '💲 USD',
        'change currency': '💵 Choose currency:',
        'exchange': '🔁 Open to do exchange?',
        'enter province': "Select Emirate, or click "
                          "<b>Location 📍</b>button",
        'enter city': "Select city, or click "
                      "<b>Location 📍</b>button",
        'location': 'Location 📍',
        'choosed': 'Selected',
        'enter memory': '💾 Enter memory capacity',
        'enter number': "Please use integers only",
        'error region': 'No region with this name',
        'error': 'Error',
        'next': '⏩',
        'send photo': "📸 Add photos of your ad \n <i>(Maximum: 6)</i>",
        'continue': 'Continue ➡',
        'next step': "Next step click <b>Continue ➡</b> button \n or you can upload more photos.",
        'select the desired section': "👇 Choose a menu",
        'active ad': "👌 Active ads",
        'ad in check': "🔍 Under moderation review",
        'passive ad': "🏁 Ads marked as sold",
        'your active ads': "👇 Your active ads",
        'your check ads': "👇 Your ads under moderation review",
        'your passive ads': "👇 Ads you marked as sold",
        'choose ad status': "👇 Chose ad status",
        'not ads such as': "😕 You don't have such an ad",
        'sold out': "🎉 Mark as sold",
        'on inspection': '🔍 Under moderation',
        'sold': "🏁 Sold out",
        'your ad': "👉 Your ad",
        'replay your ad': "🔄  Re-post your ad to the channel",
        'congratulations': "🥳 Congrats",
        'exception message': "🤕 Sorry problem occurred with our bot ",
        'photo except': '❗ Please send a photo or click button',
        'imei registered': "IMEI registered",
        'not imei registered': "IMEI not registered",
        'we agree': 'We will deal 🤝',
        'has exchange': 'open to exchange',
        'not exchange': "no exchange",
        'has document box': 'Yes documents',
        'not document box': "No documents",
        'footer text': "📲 Sell a phone 👉 <a href='{channel_link}'>Phone marketplace</a>,\n"
                       "🤖 Buy a phone 👉 <a href='{bot_link}'>MyStore Phone Market</a>",
        'sold out formating': '<b>🎉 #Sold_out</b>',
        'ad owner': "Ad owner",
        'footer text instagram': "📲 Phone marketplace 👉 sell your phone",
        'not your number': "❗ This is not your phone number! Please press <b>📲 Send Number</b> button",
        'click send number button': "Click <b>📲 Send Number</b> button",
        'send me photo only': '❗️Please send me a photo or click button',
        'please click the button': "❗️Please click the button",
        'please send me text': "❗️Please send me text",
        'please send me text or click button': "❗️Please send me text or click button",
        'please send me integer numbers': "❗️Please send me integer numbers",
        'change user location': "📍 Change location",
        'choose category': "⬇ Choose category:",
        'black list': "🔒 You have been blacklisted and cannot post an ad.",
        'max ad count': "🔒 You have reached the limit for free advertising. Please contact admin",
        'text limit': '⚠️The text exceeded the limit. Please shorten the text',
        'number limit': '⚠️The text exceeded the limit. Please shorten the numbers',
        'current location': "📍 Current location: ",

    },

    'lang_2': {
        'language flag': '🇦🇪',
        'main menu': '⏏️ القائمة الرئيسية',
        'advertise': '📢 لدي هاتف للبيع',
        'search ads': '🔎 أبحث عن هاتف',
        'back_button': '⬅️ رجوع',
        'cancel': '❌ إلغاء',
        'advertisement menu': '📢 قائمة بيع الهواتف',
        'select from one of these manufacturer': 'الرجاء تحديد ماركة الهاتف',
        'send ad title': '📌 الرجاء إدخال طراز هاتفك',
        'send product color': '🎨 الرجاء إدخال لون الهاتف',
        'send ad description': '✍ الرجاء إدخال وصف موجز لإعلانك أو اضغط على استمر ➡',
        'we will deal': '🤝 أقبل التفاوض على السعر',
        'enter your ad price': '💰 الرجاء إدخال سعر الهاتف (أرقام صحيحة فقط)',
        'enter your phone number': '📞 الرجاء إدخال رقم هاتفك أو الضغط على '
                                   ' 📲إ رسال الرقم ',
        'send number button': " 📲 إرسال الرقم ",
        'wow cool phone number': 'رقم هاتف جميل :)',
        'main menu guide': 'هذه هي قائمتنا الرئيسية، إذا كنت بحاجة إلى دعم فني، فيرجى استخدام قائمة الدعم الفني',
        'no problem saved your language': 'تم حفظ اللغة بنجاح، الآن سنتحدث باستخدام اللغة المحفوظة',
        'decline my ad': '❌ إلغاء الإعلان',
        'confirm my ad': '✅ أوافق على الإعلان',
        'check your ad to confirm': "👆 يرجى التحقق من إعلانك والموافقة عليه",
        'your ad has been received, wait for confirmation': "تم استلام الإعلان، سيتم عرضه بعد المراجعة والقبول",
        'your ad has been declined': "لقد قمت بإلغاء الإعلان",
        'your ad has been confirmed by moderator':
            "تهانينا، تمت الموافقة على إعلانك بالعنوان التالي, {} , وتمت عملية النشر بنجاح \n"
            "بعد بيع الهاتف، يرجى تحديث الإعلان إلى مباع",
        'your ad has been declined by moderator':
            'للأسف، تم رفض إعلانك الذي يحمل العنوان, {} ، يُرجى مراجعة الإرشادات والمحاولة مرة أخرى ',
        'ad title': 'العنوان:',
        'ad price': 'السعر:',
        'ad phone': 'الهاتف:',
        'ad description': 'الوصف:',
        'you must enter digit for price': 'الرجاء استخدام الأعداد الصحيحة للسعر فقط',
        'my account': '🏠 حسابي',
        'my ads': '📢 إعلاناتي',
        'ask your questions from profile below': 'You can ask your questions to the following account:',
        'you dont have any active ads': "ليس لديك أي إعلانات مفعلة",
        'ask question': 'هل لديك سؤال؟ ',
        'technical support': '❓الدعم الفني',
        'change user language': 'تغيير اللغة',
        'choose condition': '⚙ حدد حالة الهاتف: ',
        'has document': '📦📄 هل لديك علبة الهاتف الأصلية؟ ',
        'yes': '✅ نعم',
        'no': '❌ لا',
        'is imei registered': "✅ هل رقم IMEI الخاص بالهاتف مسجل؟",
        'sum': "AED",
        'usd': 'USD 💲',
        'change currency': '💵 اختر العملة: ',
        'exchange': '🔁 هل ترغب في التبادل؟',
        'enter province': "الرجاء اختيار الإمارة أو اضغط على زر 📍 الموقع ",
        'enter city': "الرجاء اختيار المدينة أو اضغط على زر 📍 الموقع ",
        'location': '📍 الموقع',
        'choosed': 'المحدد',
        'enter memory': '💾 الرجاء إدخال سعة الذاكرة',
        'enter number': "الرجاء إدخال الأعداد الصحيحة فقط",
        'error region': 'لم نجد منطقة بهذا الاسم',
        'error': 'خطأ',
        'next': '⏩',
        'send photo': "📸 الرجاء إضافة الصور لإعلانك (الحد الأقصى: 6)",
        'continue': '➡ للاستمرار',
        'next step': "يمكنك تحميل المزيد من الصور أو اضغط على الزر ➡ التالي للخطوة التالية",
        'select the desired section': "👇 اختر القائمة",
        'active ad': "👌 الإعلانات المفعلة",
        'ad in check': "🔍 قيد المراجعة",
        'passive ad': "🏁 إعلانات منتهية الصلاحية",
        'your active ads': "👆 اعلانات فعالة",
        'your check ads': "👆 الإعلانات قيد المراجعة",
        'your passive ads': "👆 الإعلانات التي تم تغييرها إلى مباع ",
        'choose ad status': "👇 لتغيير حالة الإعلان",
        'not ads such as': "😕 ليس لديك إعلان مثل هذا",
        'sold out': "🎉 تغيير إلى مباع",
        'on inspection': '🔍 قيد المراجعة',
        'sold': "🏁 مباع",
        'your ad': "👉 إعلاناتك",
        'replay your ad': "🔄  لإعادة نشر الإعلان بالعنوان, {} ",
        'congratulations': "تهانينا" '🥳',
        'exception message': "🤕 نأسف لحدوث خلل فني",
        'photo except': '❗ الرجاء ارسال الصورة',
        'imei registered': "IMEI registered",
        'not imei registered': "IMEI not registered",
        'we agree': 'We will deal 🤝',
        'has exchange': 'open to exchange',
        'not exchange': "no exchange",
        'has document box': 'Yes documents',
        'not document box': "No documents",
        'footer text': "📲 Sell a phone 👉 <a href='{channel_link}'>Phone marketplace</a>,\n"
                       "🤖 Buy a phone 👉 <a href='{bot_link}'>MyStore Phone Market</a>",
        'sold out formating': '<b>🎉 #Sold_out</b>',
        'ad owner': "Ad owner",
        'footer text instagram': "📲 Phone marketplace 👉 sell your phone",
        'not your number': "❗ This is not your phone number! Please click <b>📲 Send Number</b> button",
        'click send number button': "Click <b>📲 Send Number</b> button",
        'send me photo only': '❗️Please send me a photo or click button',
        'please click the button': "❗️Please click the button",
        'please send me text': "❗️Please send me text",
        'please send me text or click button': "❗️Please send me text or click button",
        'please send me integer numbers': "❗️Please send me integer numbers",
        'change user location': "📍 Change location",
        'choose category': "⬇ Choose category:",
        'black list': "🔒 You have been blacklisted and cannot post an ad.",
        'max ad count': "🔒 You have reached the limit for free advertising. Please contact admin",
        'text limit': '⚠️The text exceeded the limit. Please shorten the text',
        'number limit': '⚠️The text exceeded the limit. Please shorten the numbers',
        'current location': "📍 Current location: ",

    }

}


class CallbackData:
    main_menu_button = 'main menu'
    back_button = 'back button'
    confirm = 'confirm'
    decline = 'decline'
    sold_out = 'sold_out'


class BotUserSteps:
    LISTING_LANGUAGE = 1
    LIST_REGION = 2
    LIST_CHILD_REGION = 3
    GETTING_USER_PHONE = 4
    MAIN_MENU = 5
    LIST_CATEGORY = 6
    GET_DETAIL = 7
    GET_DETAIL_EDIT = 8
    GETTING_PRICE = 9
    GET_DESCRIPTION = 10
    GETTING_PHOTO = 11
    ASK_CONFIRMATION = 12
    PERSONAL_CABINET = 13
    CHANGE_LOCATION = 14
    CHANGE_CHILD_LOCATION = 15
    EDIT_LANGUAGE = 16
    MY_ADS = 17
    SEND_AD_BY_STATUS = 18
    GET_AD = 19
    CHANGE_STATUS = 20


class BotUserLanguageChoices(models.TextChoices):
    LANGUAGE_1 = 'lang_1' #english
    LANGUAGE_2 = 'lang_2' #arabic


class InstaConst:
    hash_tags = '.\n.\n #Apparatuz #apparatuz_telefon #apparat #telefon #telefonbozor #telefon_bozor'


class ExceptionLinks:
    apparatuz_link = [
        'https://t.me/apparatuz_telefon',
        'https://t.me/apparatuz_chat',
        'https://t.me/apparatuz_bot',
        't.me/apparatuz_telefon',
        't.me/apparatuz_chat',
        't.me/apparatuz_bot'
    ]

    username = [
        'apparatuz_telefon',
        'apparatuz_chat',
        'apparatuz_bot',
        'ijahongirmirzo',
        'Mashhurbek_Mashrabov'
    ]

    admins_id = [1004815988, 1329553523]


class BotWords:
    answer_mention = [
        'Chaqirdizmi aka ? 🙄',
        'Xa brad ✋',
        'Man shottaman 😎',
        'Mani chaqirdizmi 🤨'
    ]

    answer_admin_mention = [
        'Ho\'jayinni chaqirdizmi 🙄',
        'Ho\'jayinni hozir chaqiraman 🏃‍'
    ]

    answer_mention_admin = [
        'Labbe ho\'jayin 🙄',
        'Chaqirdizmi ho\'jayin 🤚'
    ]

    call_to_chat = [
        'Aka lichkaga o\'tib  yozvorin, gap bor 😎\nSpam bo\'lsezam muammo yo\'q',
        'Brad lichkaga o\'tsez telefonizi bepul reklama qivoramiz 😉\nSpam bo\'lsezam muammo yo\'q'
    ]

    schedule_words = [
        "Assalomu alaykum. Akalar kim e'lon bermoqchi bo'lsa tezda lichkaga o'tamiz 🏃\nE'lon berish bepul ✨",
        "Nima gap akalar 😎. Kim e'lon bermoqchidi ? Lichkaga yozvorsin",
        "Kimi sotiladigan telefoni boridi o'zi 👀? Tezda lichkaga o'tib yozvorsin cho'tki qilib reklama qivoramiz.\n📌 E'lon berish bepul",
        "Qani kimi sotiladigan telefoni bor ? Lichkaga o'tilar chotki qilib reklama qivoramiz.\n📌 E'lon berish bepul"
    ]

    remove_photo = [
        "brad e'lonizi man orqali bersez bo'ladi, lichkaga o'ting o'zim cho'tki reklama qivoraman 😎",
        "aka e'loniz bo'lsa tez lichkaga o'ting, bez ochered qivoraman 🤫",
        "sizi e'loniz bor diyishdi 👀, lichkaga o'ting sizi kutyapman"
    ]
