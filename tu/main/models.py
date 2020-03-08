from django.db import models

# Create your models here.

class Region(models.Model):
    """
    Справочник регионов
    """
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Contractor(models.Model):
    """
    Справочник арендодателей
    """
    name = models.CharField(max_length=255, unique=True)


class Appl(models.Model):
    REOLUTIONS = (('В работе', 'В работе'),
                  ('ТУ получено', 'ТУ получено'),
                  ('Отказ', 'Отказ'))

    applnum = models.CharField(max_length=50)
    sitenum = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    contractor = models.ForeignKey(Contractor, on_delete=models.PROTECT)
    appl_date = models.DateField()
    resp_date = models.DateField(null=True, blank=True)
    resolution = models.CharField(max_length=50, default='В работе')


