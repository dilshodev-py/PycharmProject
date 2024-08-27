from django.db import models

# Create your models here.
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext_lazy as _

class MyModel(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_("Title"), max_length=200)
    )

