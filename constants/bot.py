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
    'select the language': 'π Please select your language',
    'language_1': 'πΊπΈ English',
    'language_2': 'πΈπ¦ Arabic',
    "selected language doesn't exist": "Selected language doesn't exist",
    'ad id emoji': 'π',
    'ad title emoji': 'π±',
    'ad phone emoji': 'π',
    'ad person emoji': 'π€',
    'ad memory emoji': 'πΎ',
    'ad color emoji': 'π¨',
    'ad price emoji': 'π°',
    'ad description emoji': 'π',
    'ad condition emoji': 'π ',
    'ad document emoji': 'π¦π',
    'confirm ad emoji': 'β',
    'decline ad emoji': 'β',
    'ad location emoji': 'π',
    'ad exchange emoji': 'β»',
    'up emoji': 'ππππππππππππππ',
    'replay button': 'π',
    'step emoji': 'π£',
    'eye emoji': 'πβπ¨',
    'warning emoji': 'β ',
    'edit emoji': 'β',
    'bot emoji': 'π€',
    'block emoji': 'π«',
    'confirmed ad status': 'Approved β',
    'declined ad status': 'Declined β',
    'usd': "$ USD",
    'uzs': "AED",
    'new': 'New',
    'ideal': 'Ideal',
    'average': "Normal",
    'old': 'Old',
    'approve ad': "Approve the ad?",
    'sold general': "π Sold out",
    'add watermark': 'Watermark β',
    'added watermark': 'Watermark β',
    'currency': CURRENCY,
    'block': "Block",
    'repost': "Repost",
    'edit': "Edit",

    'lang_1': {
        'language flag': 'πΊπΈ',
        'main menu': 'βοΈ Main menu',
        'advertise': 'π’ Sell your phone',
        'search ads': 'π Looking for a phone',
        'back_button': 'β¬οΈ Back',
        'cancel': 'β Cancel',
        'advertisement menu': 'π’ Menu for selling a phone',
        'select from one of these manufacturer': 'Please select phone brand',
        'send ad title': 'π Please enter model of your phone',
        'send product color': 'π¨ Enter phone color',
        'send ad description': 'β Please enter brief description of your ad or click <b>Continue β‘</b>',
        'we will deal': 'π€ Accept price negotiation',
        'enter your ad price': f'π° Please enter phone price in {CURRENCY} (only integer numbers)',
        'enter your phone number': 'π Enter your phone number or click button'
                                   '"<b>π² Send number</b> button" ',
        'send number button': "π² Send number",
        'wow cool phone number': 'Wow such a cool phone number :)',
        'main menu guide': 'This is our main menu, if you need support, please use technical support menu',
        'no problem saved your language': 'Language saved, now we will talk using this language',
        'decline my ad': 'β Cancel the ad',
        'confirm my ad': 'β Approve the ad',
        'check your ad to confirm': "π Please check your ad and approve",
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
        'my account': 'My account π ',
        'my ads': 'π’ My ads',
        'you dont have any active ads': "You don't have any active ads",
        'ask your questions from profile below': 'You can ask your questions to the following account:',
        'ask question': 'Ask a question β',
        'technical support': 'π Technical support',
        'change user language': 'Change language',
        'choose condition': 'β Select phone condition :',
        'has document': 'π¦π Has original box?',
        'yes': 'β Yes',
        'no': "β No",
        'is imei registered': "β Is the phone IMEI registered?",
        'sum': "AED",
        'usd': 'π² USD',
        'change currency': 'π΅ Choose currency:',
        'exchange': 'π Open to do exchange?',
        'enter province': "Select Emirate, or click "
                          "<b>Location π</b>button",
        'enter city': "Select city, or click "
                      "<b>Location π</b>button",
        'location': 'Location π',
        'choosed': 'Selected',
        'enter memory': 'πΎ Enter memory capacity',
        'enter number': "Please use integers only",
        'error region': 'No region with this name',
        'error': 'Error',
        'next': 'β©',
        'send photo': "πΈ Add photos of your ad \n <i>(Maximum: 6)</i>",
        'continue': 'Continue β‘',
        'next step': "Next step click <b>Continue β‘</b> button \n or you can upload more photos.",
        'select the desired section': "π Choose a menu",
        'active ad': "π Active ads",
        'ad in check': "π Under moderation review",
        'passive ad': "π Ads marked as sold",
        'your active ads': "π Your active ads",
        'your check ads': "π Your ads under moderation review",
        'your passive ads': "π Ads you marked as sold",
        'choose ad status': "π Chose ad status",
        'not ads such as': "π You don't have such an ad",
        'sold out': "π Mark as sold",
        'on inspection': 'π Under moderation',
        'sold': "π Sold out",
        'your ad': "π Your ad",
        'replay your ad': "π  Re-post your ad to the channel",
        'congratulations': "π₯³ Congrats",
        'exception message': "π€ Sorry problem occurred with our bot ",
        'photo except': 'β Please send a photo or click button',
        'imei registered': "IMEI registered",
        'not imei registered': "IMEI not registered",
        'we agree': 'We will deal π€',
        'has exchange': 'open to exchange',
        'not exchange': "no exchange",
        'has document box': 'Yes documents',
        'not document box': "No documents",
        'footer text': "π² Sell a phone π <a href='{channel_link}'>Phone marketplace</a>,\n"
                       "π€ Buy a phone π <a href='{bot_link}'>MyStore Phone Market</a>",
        'sold out formating': '<b>π #Sold_out</b>',
        'ad owner': "Ad owner",
        'footer text instagram': "π² Phone marketplace π sell your phone",
        'not your number': "β This is not your phone number! Please press <b>π² Send Number</b> button",
        'click send number button': "Click <b>π² Send Number</b> button",
        'send me photo only': 'βοΈPlease send me a photo or click button',
        'please click the button': "βοΈPlease click the button",
        'please send me text': "βοΈPlease send me text",
        'please send me text or click button': "βοΈPlease send me text or click button",
        'please send me integer numbers': "βοΈPlease send me integer numbers",
        'change user location': "π Change location",
        'choose category': "β¬ Choose category:",
        'black list': "π You have been blacklisted and cannot post an ad.",
        'max ad count': "π You have reached the limit for free advertising. Please contact admin",
        'text limit': 'β οΈThe text exceeded the limit. Please shorten the text',
        'number limit': 'β οΈThe text exceeded the limit. Please shorten the numbers',
        'current location': "π Current location: ",

    },

    'lang_2': {
        'language flag': 'π¦πͺ',
        'main menu': 'βοΈ Ψ§ΩΩΨ§Ψ¦ΩΨ© Ψ§ΩΨ±Ψ¦ΩΨ³ΩΨ©',
        'advertise': 'π’ ΩΨ―Ω ΩΨ§ΨͺΩ ΩΩΨ¨ΩΨΉ',
        'search ads': 'π Ψ£Ψ¨Ψ­Ψ« ΨΉΩ ΩΨ§ΨͺΩ',
        'back_button': 'β¬οΈ Ψ±Ψ¬ΩΨΉ',
        'cancel': 'β Ψ₯ΩΨΊΨ§Ψ‘',
        'advertisement menu': 'π’ ΩΨ§Ψ¦ΩΨ© Ψ¨ΩΨΉ Ψ§ΩΩΩΨ§ΨͺΩ',
        'select from one of these manufacturer': 'Ψ§ΩΨ±Ψ¬Ψ§Ψ‘ ΨͺΨ­Ψ―ΩΨ― ΩΨ§Ψ±ΩΨ© Ψ§ΩΩΨ§ΨͺΩ',
        'send ad title': 'π Ψ§ΩΨ±Ψ¬Ψ§Ψ‘ Ψ₯Ψ―Ψ?Ψ§Ω Ψ·Ψ±Ψ§Ψ² ΩΨ§ΨͺΩΩ',
        'send product color': 'π¨ Ψ§ΩΨ±Ψ¬Ψ§Ψ‘ Ψ₯Ψ―Ψ?Ψ§Ω ΩΩΩ Ψ§ΩΩΨ§ΨͺΩ',
        'send ad description': 'β Ψ§ΩΨ±Ψ¬Ψ§Ψ‘ Ψ₯Ψ―Ψ?Ψ§Ω ΩΨ΅Ω ΩΩΨ¬Ψ² ΩΨ₯ΨΉΩΨ§ΩΩ Ψ£Ω Ψ§ΨΆΨΊΨ· ΨΉΩΩ Ψ§Ψ³ΨͺΩΨ± β‘',
        'we will deal': 'π€ Ψ£ΩΨ¨Ω Ψ§ΩΨͺΩΨ§ΩΨΆ ΨΉΩΩ Ψ§ΩΨ³ΨΉΨ±',
        'enter your ad price': 'π° Ψ§ΩΨ±Ψ¬Ψ§Ψ‘ Ψ₯Ψ―Ψ?Ψ§Ω Ψ³ΨΉΨ± Ψ§ΩΩΨ§ΨͺΩ (Ψ£Ψ±ΩΨ§Ω Ψ΅Ψ­ΩΨ­Ψ© ΩΩΨ·)',
        'enter your phone number': 'π Ψ§ΩΨ±Ψ¬Ψ§Ψ‘ Ψ₯Ψ―Ψ?Ψ§Ω Ψ±ΩΩ ΩΨ§ΨͺΩΩ Ψ£Ω Ψ§ΩΨΆΨΊΨ· ΨΉΩΩ '
                                   ' π²Ψ₯ Ψ±Ψ³Ψ§Ω Ψ§ΩΨ±ΩΩ ',
        'send number button': " π² Ψ₯Ψ±Ψ³Ψ§Ω Ψ§ΩΨ±ΩΩ ",
        'wow cool phone number': 'Ψ±ΩΩ ΩΨ§ΨͺΩ Ψ¬ΩΩΩ :)',
        'main menu guide': 'ΩΨ°Ω ΩΩ ΩΨ§Ψ¦ΩΨͺΩΨ§ Ψ§ΩΨ±Ψ¦ΩΨ³ΩΨ©Ψ Ψ₯Ψ°Ψ§ ΩΩΨͺ Ψ¨Ψ­Ψ§Ψ¬Ψ© Ψ₯ΩΩ Ψ―ΨΉΩ ΩΩΩΨ ΩΩΨ±Ψ¬Ω Ψ§Ψ³ΨͺΨ?Ψ―Ψ§Ω ΩΨ§Ψ¦ΩΨ© Ψ§ΩΨ―ΨΉΩ Ψ§ΩΩΩΩ',
        'no problem saved your language': 'ΨͺΩ Ψ­ΩΨΈ Ψ§ΩΩΨΊΨ© Ψ¨ΩΨ¬Ψ§Ψ­Ψ Ψ§ΩΨ’Ω Ψ³ΩΨͺΨ­Ψ―Ψ« Ψ¨Ψ§Ψ³ΨͺΨ?Ψ―Ψ§Ω Ψ§ΩΩΨΊΨ© Ψ§ΩΩΨ­ΩΩΨΈΨ©',
        'decline my ad': 'β Ψ₯ΩΨΊΨ§Ψ‘ Ψ§ΩΨ₯ΨΉΩΨ§Ω',
        'confirm my ad': 'β Ψ£ΩΨ§ΩΩ ΨΉΩΩ Ψ§ΩΨ₯ΨΉΩΨ§Ω',
        'check your ad to confirm': "π ΩΨ±Ψ¬Ω Ψ§ΩΨͺΨ­ΩΩ ΩΩ Ψ₯ΨΉΩΨ§ΩΩ ΩΨ§ΩΩΩΨ§ΩΩΨ© ΨΉΩΩΩ",
        'your ad has been received, wait for confirmation': "ΨͺΩ Ψ§Ψ³ΨͺΩΨ§Ω Ψ§ΩΨ₯ΨΉΩΨ§ΩΨ Ψ³ΩΨͺΩ ΨΉΨ±ΨΆΩ Ψ¨ΨΉΨ― Ψ§ΩΩΨ±Ψ§Ψ¬ΨΉΨ© ΩΨ§ΩΩΨ¨ΩΩ",
        'your ad has been declined': "ΩΩΨ― ΩΩΨͺ Ψ¨Ψ₯ΩΨΊΨ§Ψ‘ Ψ§ΩΨ₯ΨΉΩΨ§Ω",
        'your ad has been confirmed by moderator':
            "ΨͺΩΨ§ΩΩΩΨ§Ψ ΨͺΩΨͺ Ψ§ΩΩΩΨ§ΩΩΨ© ΨΉΩΩ Ψ₯ΨΉΩΨ§ΩΩ Ψ¨Ψ§ΩΨΉΩΩΨ§Ω Ψ§ΩΨͺΨ§ΩΩ, {} , ΩΨͺΩΨͺ ΨΉΩΩΩΨ© Ψ§ΩΩΨ΄Ψ± Ψ¨ΩΨ¬Ψ§Ψ­ \n"
            "Ψ¨ΨΉΨ― Ψ¨ΩΨΉ Ψ§ΩΩΨ§ΨͺΩΨ ΩΨ±Ψ¬Ω ΨͺΨ­Ψ―ΩΨ« Ψ§ΩΨ₯ΨΉΩΨ§Ω Ψ₯ΩΩ ΩΨ¨Ψ§ΨΉ",
        'your ad has been declined by moderator':
            'ΩΩΨ£Ψ³ΩΨ ΨͺΩ Ψ±ΩΨΆ Ψ₯ΨΉΩΨ§ΩΩ Ψ§ΩΨ°Ω ΩΨ­ΩΩ Ψ§ΩΨΉΩΩΨ§Ω, {} Ψ ΩΩΨ±Ψ¬Ω ΩΨ±Ψ§Ψ¬ΨΉΨ© Ψ§ΩΨ₯Ψ±Ψ΄Ψ§Ψ―Ψ§Ψͺ ΩΨ§ΩΩΨ­Ψ§ΩΩΨ© ΩΨ±Ψ© Ψ£Ψ?Ψ±Ω ',
        'ad title': 'Ψ§ΩΨΉΩΩΨ§Ω:',
        'ad price': 'Ψ§ΩΨ³ΨΉΨ±:',
        'ad phone': 'Ψ§ΩΩΨ§ΨͺΩ:',
        'ad description': 'Ψ§ΩΩΨ΅Ω:',
        'you must enter digit for price': 'Ψ§ΩΨ±Ψ¬Ψ§Ψ‘ Ψ§Ψ³ΨͺΨ?Ψ―Ψ§Ω Ψ§ΩΨ£ΨΉΨ―Ψ§Ψ― Ψ§ΩΨ΅Ψ­ΩΨ­Ψ© ΩΩΨ³ΨΉΨ± ΩΩΨ·',
        'my account': 'π  Ψ­Ψ³Ψ§Ψ¨Ω',
        'my ads': 'π’ Ψ₯ΨΉΩΨ§ΩΨ§ΨͺΩ',
        'ask your questions from profile below': 'You can ask your questions to the following account:',
        'you dont have any active ads': "ΩΩΨ³ ΩΨ―ΩΩ Ψ£Ω Ψ₯ΨΉΩΨ§ΩΨ§Ψͺ ΩΩΨΉΩΨ©",
        'ask question': 'ΩΩ ΩΨ―ΩΩ Ψ³Ψ€Ψ§ΩΨ ',
        'technical support': 'βΨ§ΩΨ―ΨΉΩ Ψ§ΩΩΩΩ',
        'change user language': 'ΨͺΨΊΩΩΨ± Ψ§ΩΩΨΊΨ©',
        'choose condition': 'β Ψ­Ψ―Ψ― Ψ­Ψ§ΩΨ© Ψ§ΩΩΨ§ΨͺΩ: ',
        'has document': 'π¦π ΩΩ ΩΨ―ΩΩ ΨΉΩΨ¨Ψ© Ψ§ΩΩΨ§ΨͺΩ Ψ§ΩΨ£Ψ΅ΩΩΨ©Ψ ',
        'yes': 'β ΩΨΉΩ',
        'no': 'β ΩΨ§',
        'is imei registered': "β ΩΩ Ψ±ΩΩ IMEI Ψ§ΩΨ?Ψ§Ψ΅ Ψ¨Ψ§ΩΩΨ§ΨͺΩ ΩΨ³Ψ¬ΩΨ",
        'sum': "AED",
        'usd': 'USD π²',
        'change currency': 'π΅ Ψ§Ψ?ΨͺΨ± Ψ§ΩΨΉΩΩΨ©: ',
        'exchange': 'π ΩΩ ΨͺΨ±ΨΊΨ¨ ΩΩ Ψ§ΩΨͺΨ¨Ψ§Ψ―ΩΨ',
        'enter province': "Ψ§ΩΨ±Ψ¬Ψ§Ψ‘ Ψ§Ψ?ΨͺΩΨ§Ψ± Ψ§ΩΨ₯ΩΨ§Ψ±Ψ© Ψ£Ω Ψ§ΨΆΨΊΨ· ΨΉΩΩ Ψ²Ψ± π Ψ§ΩΩΩΩΨΉ ",
        'enter city': "Ψ§ΩΨ±Ψ¬Ψ§Ψ‘ Ψ§Ψ?ΨͺΩΨ§Ψ± Ψ§ΩΩΨ―ΩΩΨ© Ψ£Ω Ψ§ΨΆΨΊΨ· ΨΉΩΩ Ψ²Ψ± π Ψ§ΩΩΩΩΨΉ ",
        'location': 'π Ψ§ΩΩΩΩΨΉ',
        'choosed': 'Ψ§ΩΩΨ­Ψ―Ψ―',
        'enter memory': 'πΎ Ψ§ΩΨ±Ψ¬Ψ§Ψ‘ Ψ₯Ψ―Ψ?Ψ§Ω Ψ³ΨΉΨ© Ψ§ΩΨ°Ψ§ΩΨ±Ψ©',
        'enter number': "Ψ§ΩΨ±Ψ¬Ψ§Ψ‘ Ψ₯Ψ―Ψ?Ψ§Ω Ψ§ΩΨ£ΨΉΨ―Ψ§Ψ― Ψ§ΩΨ΅Ψ­ΩΨ­Ψ© ΩΩΨ·",
        'error region': 'ΩΩ ΩΨ¬Ψ― ΩΩΨ·ΩΨ© Ψ¨ΩΨ°Ψ§ Ψ§ΩΨ§Ψ³Ω',
        'error': 'Ψ?Ψ·Ψ£',
        'next': 'β©',
        'send photo': "πΈ Ψ§ΩΨ±Ψ¬Ψ§Ψ‘ Ψ₯ΨΆΨ§ΩΨ© Ψ§ΩΨ΅ΩΨ± ΩΨ₯ΨΉΩΨ§ΩΩ (Ψ§ΩΨ­Ψ― Ψ§ΩΨ£ΩΨ΅Ω: 6)",
        'continue': 'β‘ ΩΩΨ§Ψ³ΨͺΩΨ±Ψ§Ψ±',
        'next step': "ΩΩΩΩΩ ΨͺΨ­ΩΩΩ Ψ§ΩΩΨ²ΩΨ― ΩΩ Ψ§ΩΨ΅ΩΨ± Ψ£Ω Ψ§ΨΆΨΊΨ· ΨΉΩΩ Ψ§ΩΨ²Ψ± β‘ Ψ§ΩΨͺΨ§ΩΩ ΩΩΨ?Ψ·ΩΨ© Ψ§ΩΨͺΨ§ΩΩΨ©",
        'select the desired section': "π Ψ§Ψ?ΨͺΨ± Ψ§ΩΩΨ§Ψ¦ΩΨ©",
        'active ad': "π Ψ§ΩΨ₯ΨΉΩΨ§ΩΨ§Ψͺ Ψ§ΩΩΩΨΉΩΨ©",
        'ad in check': "π ΩΩΨ― Ψ§ΩΩΨ±Ψ§Ψ¬ΨΉΨ©",
        'passive ad': "π Ψ₯ΨΉΩΨ§ΩΨ§Ψͺ ΩΩΨͺΩΩΨ© Ψ§ΩΨ΅ΩΨ§Ψ­ΩΨ©",
        'your active ads': "π Ψ§ΨΉΩΨ§ΩΨ§Ψͺ ΩΨΉΨ§ΩΨ©",
        'your check ads': "π Ψ§ΩΨ₯ΨΉΩΨ§ΩΨ§Ψͺ ΩΩΨ― Ψ§ΩΩΨ±Ψ§Ψ¬ΨΉΨ©",
        'your passive ads': "π Ψ§ΩΨ₯ΨΉΩΨ§ΩΨ§Ψͺ Ψ§ΩΨͺΩ ΨͺΩ ΨͺΨΊΩΩΨ±ΩΨ§ Ψ₯ΩΩ ΩΨ¨Ψ§ΨΉ ",
        'choose ad status': "π ΩΨͺΨΊΩΩΨ± Ψ­Ψ§ΩΨ© Ψ§ΩΨ₯ΨΉΩΨ§Ω",
        'not ads such as': "π ΩΩΨ³ ΩΨ―ΩΩ Ψ₯ΨΉΩΨ§Ω ΩΨ«Ω ΩΨ°Ψ§",
        'sold out': "π ΨͺΨΊΩΩΨ± Ψ₯ΩΩ ΩΨ¨Ψ§ΨΉ",
        'on inspection': 'π ΩΩΨ― Ψ§ΩΩΨ±Ψ§Ψ¬ΨΉΨ©',
        'sold': "π ΩΨ¨Ψ§ΨΉ",
        'your ad': "π Ψ₯ΨΉΩΨ§ΩΨ§ΨͺΩ",
        'replay your ad': "π  ΩΨ₯ΨΉΨ§Ψ―Ψ© ΩΨ΄Ψ± Ψ§ΩΨ₯ΨΉΩΨ§Ω Ψ¨Ψ§ΩΨΉΩΩΨ§Ω, {} ",
        'congratulations': "ΨͺΩΨ§ΩΩΩΨ§" 'π₯³',
        'exception message': "π€ ΩΨ£Ψ³Ω ΩΨ­Ψ―ΩΨ« Ψ?ΩΩ ΩΩΩ",
        'photo except': 'β Ψ§ΩΨ±Ψ¬Ψ§Ψ‘ Ψ§Ψ±Ψ³Ψ§Ω Ψ§ΩΨ΅ΩΨ±Ψ©',
        'imei registered': "IMEI registered",
        'not imei registered': "IMEI not registered",
        'we agree': 'We will deal π€',
        'has exchange': 'open to exchange',
        'not exchange': "no exchange",
        'has document box': 'Yes documents',
        'not document box': "No documents",
        'footer text': "π² Sell a phone π <a href='{channel_link}'>Phone marketplace</a>,\n"
                       "π€ Buy a phone π <a href='{bot_link}'>MyStore Phone Market</a>",
        'sold out formating': '<b>π #Sold_out</b>',
        'ad owner': "Ad owner",
        'footer text instagram': "π² Phone marketplace π sell your phone",
        'not your number': "β This is not your phone number! Please click <b>π² Send Number</b> button",
        'click send number button': "Click <b>π² Send Number</b> button",
        'send me photo only': 'βοΈPlease send me a photo or click button',
        'please click the button': "βοΈPlease click the button",
        'please send me text': "βοΈPlease send me text",
        'please send me text or click button': "βοΈPlease send me text or click button",
        'please send me integer numbers': "βοΈPlease send me integer numbers",
        'change user location': "π Change location",
        'choose category': "β¬ Choose category:",
        'black list': "π You have been blacklisted and cannot post an ad.",
        'max ad count': "π You have reached the limit for free advertising. Please contact admin",
        'text limit': 'β οΈThe text exceeded the limit. Please shorten the text',
        'number limit': 'β οΈThe text exceeded the limit. Please shorten the numbers',
        'current location': "π Current location: ",

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
        'Chaqirdizmi aka ? π',
        'Xa brad β',
        'Man shottaman π',
        'Mani chaqirdizmi π€¨'
    ]

    answer_admin_mention = [
        'Ho\'jayinni chaqirdizmi π',
        'Ho\'jayinni hozir chaqiraman πβ'
    ]

    answer_mention_admin = [
        'Labbe ho\'jayin π',
        'Chaqirdizmi ho\'jayin π€'
    ]

    call_to_chat = [
        'Aka lichkaga o\'tib  yozvorin, gap bor π\nSpam bo\'lsezam muammo yo\'q',
        'Brad lichkaga o\'tsez telefonizi bepul reklama qivoramiz π\nSpam bo\'lsezam muammo yo\'q'
    ]

    schedule_words = [
        "Assalomu alaykum. Akalar kim e'lon bermoqchi bo'lsa tezda lichkaga o'tamiz π\nE'lon berish bepul β¨",
        "Nima gap akalar π. Kim e'lon bermoqchidi ? Lichkaga yozvorsin",
        "Kimi sotiladigan telefoni boridi o'zi π? Tezda lichkaga o'tib yozvorsin cho'tki qilib reklama qivoramiz.\nπ E'lon berish bepul",
        "Qani kimi sotiladigan telefoni bor ? Lichkaga o'tilar chotki qilib reklama qivoramiz.\nπ E'lon berish bepul"
    ]

    remove_photo = [
        "brad e'lonizi man orqali bersez bo'ladi, lichkaga o'ting o'zim cho'tki reklama qivoraman π",
        "aka e'loniz bo'lsa tez lichkaga o'ting, bez ochered qivoraman π€«",
        "sizi e'loniz bor diyishdi π, lichkaga o'ting sizi kutyapman"
    ]
