from django.core.management.base import BaseCommand
from registar.models import Eparhija


class Command(BaseCommand):
    help = "Попуњава табелу Епархија са примерима епархија"

    def handle(self, *args, **kwargs):
        eparhije = [
            {
                "nivo": "Архиепископија",
                "naziv": "београдско-карловачка",
                "sediste": "Београд",
            },
            {
                "nivo": "Митрополија",
                "naziv": "аустралијско-новозеландска",
                "sediste": "Сиднеј",
            },
            {"nivo": "Митрополија", "naziv": "дабробосанска", "sediste": "Сарајево"},
            {
                "nivo": "Митрополија",
                "naziv": "загребачко-љубљанска",
                "sediste": "Загреб",
            },
            {
                "nivo": "Митрополија",
                "naziv": "црногорско-приморска",
                "sediste": "Цетиње",
            },
            {"nivo": "Епархија", "naziv": "аустријско-швајцарска", "sediste": "Беч"},
            {"nivo": "Епархија", "naziv": "банатска", "sediste": "Вршац"},
            {"nivo": "Епархија", "naziv": "бањалучка", "sediste": "Бања Лука"},
            {"nivo": "Епархија", "naziv": "бачка", "sediste": "Нови Сад"},
            {"nivo": "Епархија", "naziv": "бихаћко-петровачка", "sediste": "Бихаћ"},
            {"nivo": "Епархија", "naziv": "браничевска", "sediste": "Пожаревац"},
            {
                "nivo": "Епархија",
                "naziv": "британско-скандинавска",
                "sediste": "Лондон",
            },
            {"nivo": "Епархија", "naziv": "будимска", "sediste": "Будимпешта"},
            {"nivo": "Епархија", "naziv": "будимљанско-никшићка", "sediste": "Никшић"},
            {"nivo": "Епархија", "naziv": "буенос-ајреска", "sediste": "Буенос Ајрес"},
            {"nivo": "Епархија", "naziv": "ваљевска", "sediste": "Ваљево"},
            {"nivo": "Епархија", "naziv": "врањска", "sediste": "Врање"},
            {"nivo": "Епархија", "naziv": "горњокарловачка", "sediste": "Карловац"},
            {"nivo": "Епархија", "naziv": "далматинска", "sediste": "Шибеник"},
            {
                "nivo": "Епархија",
                "naziv": "диселдорфска и немачка",
                "sediste": "Диселдорф",
            },
            {"nivo": "Епархија", "naziv": "жичка", "sediste": "Краљево"},
            {
                "nivo": "Епархија",
                "naziv": "западноамеричка",
                "sediste": "Сан Франциско",
            },
            {"nivo": "Епархија", "naziv": "западноевропска", "sediste": "Париз"},
            {
                "nivo": "Епархија",
                "naziv": "захумско-херцеговачка",
                "sediste": "Требиње",
            },
            {"nivo": "Епархија", "naziv": "зворничко-тузланска", "sediste": "Бијељина"},
            {"nivo": "Епархија", "naziv": "источноамеричка", "sediste": "Њујорк"},
            {"nivo": "Епархија", "naziv": "канадска", "sediste": "Торонто"},
            {"nivo": "Епархија", "naziv": "крушевачка", "sediste": "Крушевац"},
            {"nivo": "Епархија", "naziv": "милешевска", "sediste": "Пријепоље"},
            {"nivo": "Епархија", "naziv": "нишка", "sediste": "Ниш"},
            {
                "nivo": "Епархија",
                "naziv": "новограчаничко-средњезападноамеричка",
                "sediste": "Чикаго",
            },
            {
                "nivo": "Епархија",
                "naziv": "осечкопољска и барањска",
                "sediste": "Осијек",
            },
            {"nivo": "Епархија", "naziv": "рашко-призренска", "sediste": "Призрен"},
            {"nivo": "Епархија", "naziv": "славонска", "sediste": "Пакрац"},
            {"nivo": "Епархија", "naziv": "сремска", "sediste": "Сремски Карловци"},
            {"nivo": "Епархија", "naziv": "тимочка", "sediste": "Зајечар"},
            {"nivo": "Епархија", "naziv": "темишварска", "sediste": "Темишвар"},
            {"nivo": "Епархија", "naziv": "шабачка", "sediste": "Шабац"},
            {"nivo": "Епархија", "naziv": "шумадијска", "sediste": "Крагујевац"},
            {
                "nivo": "Архиепископија",
                "naziv": "ПРАВОСЛАВНА ОХРИДСКА",
                "sediste": "Охрид",
            },
        ]

        for eparhija in eparhije:
            Eparhija.objects.get_or_create(
                naziv=eparhija["naziv"],
                defaults={"nivo": eparhija["nivo"], "sediste": eparhija["sediste"]},
            )

        self.stdout.write(self.style.SUCCESS("Успешно попуњена табела Епархија"))
