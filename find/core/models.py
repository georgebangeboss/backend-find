from django.db import models
from django.utils.translation import gettext_lazy as _
import django_filters

# Create your models here.


class LostFoundStatus(models.TextChoices):
    LOST = "LOST", _("Lost")
    FOUND = "FOUND", _("Found")


class Card(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    second_name = models.CharField(max_length=200, null=True)
    third_name = models.CharField(max_length=200, null=True)
    reg_number = models.CharField(max_length=200, null=True)
    status = models.CharField(
        max_length=200,
        choices=LostFoundStatus.choices,
        default=LostFoundStatus.FOUND,
    )
    id_number = models.CharField(max_length=200, null=True)
    school_name = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=200, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="images/")
    location_found = models.CharField(max_length=200, null=True)

    @property
    def extraField(self):
        pass


    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"


