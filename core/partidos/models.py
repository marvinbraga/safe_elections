from django.db import models
from django.utils.translation import gettext_lazy as _

from core.commons.models import IdTimeStampedModel


class EspectroPolitico(models.IntegerChoices):
    NENHUM = 0
    LIBERAL = 1
    CONSERVADOR = 3
    SOCIAL_DEMOCRATA = 5
    SOCIALISTA = 6


class Partido(IdTimeStampedModel):
    name = models.CharField(
        verbose_name=_("Nome"),
        max_length=250,
        unique=True,
        help_text="",
    )
    short_name = models.CharField(verbose_name=_("Sigla"), max_length=15, unique=True)
    number = models.IntegerField(verbose_name=_("Número"), unique=True)
    type = models.IntegerField(
        verbose_name=_("Espectro"),
        choices=EspectroPolitico.choices,
        default=EspectroPolitico.NENHUM,
    )
    description = models.CharField(
        verbose_name=_("Descrição"),
        max_length=250,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.short_name} ({self.number})"

    class Meta:
        verbose_name_plural = _("Partidos")
