from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# Create your models here.


User = get_user_model()


class LostFoundStatus(models.TextChoices):
    LOST = "L", _("LOST")
    CLAIMED = "C", _("CLAIMED")
    FOUND = "F", _("FOUND")
    REGISTERED = "R", _("REGISTERED")


class Location(models.TextChoices):
    GATE_A = "A", _("GATE_A")
    GATE_B = "B", _("GATE_B")
    GATE_C = "C", _("GATE_C")
    GATE_D = "D", _("GATE_D")


class Card(models.Model):
    id_string = models.CharField(max_length=500, null=True,blank=True,)
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="cards",
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=200, null=True,blank=True)
    status = models.CharField(
        max_length=200,
        choices=LostFoundStatus.choices,
        null=True,
        blank=True,
    )
    college_name = models.CharField(max_length=200, null=True,blank=True,)
    reg_number = models.CharField(max_length=200, null=True,blank=True,)
    department = models.CharField(max_length=200, null=True,blank=True,)
    image = models.ImageField(blank=True, null=True, upload_to="images/",)
    location_found = models.CharField(
        max_length=200,
        choices=Location.choices,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.reg_number} - {self.pk}"

    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"




