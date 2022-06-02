import json
import os

from django.core.management import BaseCommand

# from bot.models.property import Region
# from django.conf import settings
#

class Command(BaseCommand):
    pass
    # help = 'seed region and districts'

    # def handle(self, *args, **options):
    #     regions = json.load(open(os.path.join(settings.BASE_DIR, 'fixtures/regions.json'), encoding="utf8"))
    #     for region in regions:
    #         reg, _ = Region.objects.get_or_create(pk=region.get('id'))
    #         reg.name_uz = region.get('name_uz')
    #         reg.name_ru = region.get('name_ru')
    #         reg.save()
    #     districts = json.load(open(os.path.join(settings.BASE_DIR, 'fixtures/districts.json'), encoding="utf8"))
    #     for district in districts:
    #         dis, _ = Region.objects.get_or_create(pk=district.get('id'))
    #         dis.parent_id = district.get('region_id')
    #         dis.name_uz = district.get('name_uz')
    #         dis.name_ru = district.get('name_ru')
    #         dis.save()
        # channels = json.load(open(os.path.join(settings.BASE_DIR, 'fixtures/channels.json'), encoding="utf8"))
        # for channel in channels:
        #     dis, _ = Region.objects.get_or_create(pk=channel.get('id'))
        #     dis.parent_id = channel.get('region_id')
        #     dis.name_uz = channel.get('name_uz')
        #     dis.name_ru = channel.get('name_ru')
        #     dis.save()

        #
        #
        #
        # self.stdout.write(self.style.SUCCESS('Alhamdulillah'))
