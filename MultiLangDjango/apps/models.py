from django.db import models
from parler.models import TranslatedFields, TranslatableModel


# Create your models here.

class Post(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=100),
        description=models.TextField()
    )

    image = models.ImageField(upload_to='posts/')



