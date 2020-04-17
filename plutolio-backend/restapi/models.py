from django.db import models

# Create your models here.
class Position(models.Model):

    TYPE_BOND = 'BND'
    TYPE_EQUITY = 'EQY'
    TYPE_ETF = 'ETF'
    TYPE_OTHER = 'OTH'

    TYPE_CHOICES = (
        (TYPE_BOND, 'Bond'),
        (TYPE_EQUITY, 'Equity'),
        (TYPE_ETF, 'ETF'),
        (TYPE_OTHER, 'Other'),
    )

    ASSETCLASS_EQUITIES = 'EQS'
    ASSETCLASS_FIXED_INCOME = 'FXI'
    ASSETCLASS_CASH = 'CSH'
    ASSETCLASS_ALTERNATIVES = 'ALT'

    ASSETCLASS_CHOICES = (
        (ASSETCLASS_EQUITIES, 'Equities'),
        (ASSETCLASS_FIXED_INCOME, 'Fixed Income'),
        (ASSETCLASS_CASH, 'Cash'),
        (ASSETCLASS_ALTERNATIVES, 'Alternatives'),
    )

    id = models.AutoField(primary_key=True)
    place = models.CharField(max_length=32)
    type = models.CharField(max_length=3, choices=TYPE_CHOICES, default=TYPE_OTHER)
    assetclass = models.CharField(max_length=3, choices=ASSETCLASS_CHOICES, default=ASSETCLASS_ALTERNATIVES)
    info = models.CharField(max_length=256)
    quantity = models.IntegerField()
    price = models.FloatField()
