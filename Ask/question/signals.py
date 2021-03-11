from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Question
from django.utils.text import slugify
from utils.randomString import randomString

@receiver(pre_save, sender=Question)
def add_slug_to_question(sender, instance, *args, **kwargs): 
    if instance and not instance.slug:
        instance.slug = slugify(instance.content) + "-" + randomString()
