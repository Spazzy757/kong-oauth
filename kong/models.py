# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from kong.kong import ConsumerResource
from django.dispatch import receiver
from django.db import models


# Create your models here.
class KongConsumer(models.Model):
    user = models.ForeignKey(User, related_name="kong_user", on_delete=models.CASCADE)
    custom_id = models.CharField(max_length=1024)


# Signals
@receiver(post_save, sender=User)
def create_consumer(**kwargs):
    """
    Creates a consumer on kong based on when a user instance is created
    :param kwargs:
    :return:
    """
    if kwargs['created']:
        data = {
            "username": kwargs['instance'].username
        }
        result = ConsumerResource().create(data)
        kong_consumer = KongConsumer.objects.create(user=kwargs['instance'], custom_id=result['id'])
        kong_consumer.save()


@receiver(pre_delete, sender=KongConsumer)
def delete_consumer(**kwargs):
    """
    Deletes a consumer on kong based on when a user instance is deleted
    :param kwargs:
    :return:
    """
    ConsumerResource().delete(kwargs['instance'].custom_id)
