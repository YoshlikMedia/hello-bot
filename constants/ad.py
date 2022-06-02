from django.db import models

class ConditionChoices(models.IntegerChoices):
    NEW = 1
    IDEAL = 2
    AVERAGE = 3
    OLD = 4

class HasDocumentChoices(models.IntegerChoices):
    YES = 1
    NO = 2

class AdTypeChoices(models.IntegerChoices):
    SELL = 1
    EXCHANGE = 2

class CurrencyChoices(models.IntegerChoices):
    UZBEK_SUM = 1
    US_DOLLAR = 2


class AdStatusChoices(models.IntegerChoices):
    NEW = 1
    WAITING_FOR_CONFIRMATION = 2
    ACTIVE = 3
    PASSIVE = 4
    DECLINED = 5

class DetailTypes(models.IntegerChoices):
    SELECT = 1
    MULTI_SELECT = 2
    INTEGER = 3
    STRING = 4
