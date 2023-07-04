from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Linkcount
import datetime


@receiver(pre_save, sender=Linkcount)
def create_link_count(sender, instance, ** kwargs):
    instance.updated_at = datetime.datetime.now()
