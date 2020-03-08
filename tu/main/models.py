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
    RESOLUTIONS = (('В работе', 'В работе'),
                  ('ТУ получено', 'ТУ получено'),
                  ('Отказ', 'Отказ'))

    applnum = models.CharField(max_length=50)  # номер заявки на получение ТУ
    sitenum = models.CharField(max_length=50)  # номер площадки
    region = models.ForeignKey(Region, on_delete=models.PROTECT)  # регион
    contractor = models.ForeignKey(Contractor, on_delete=models.PROTECT)  # арендодатель
    appl_date = models.DateField()  # дата подачи заявки на получение ТУ
    resp_date = models.DateField(null=True, blank=True)  # дата получения ответа на заявку
    resolution = models.CharField(max_length=50, default='В работе', choices=RESOLUTIONS)


