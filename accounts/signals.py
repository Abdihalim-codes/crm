from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Customer
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist

def customer_profile(sender, instance, created, **kwargs):
    if created:
        try:
            group = Group.objects.get(name='customer')
            instance.groups.add(group)

            Customer.objects.create(
                user=instance,
                name=instance.username,
            )
            print('Profile was created and user added to group')
        except ObjectDoesNotExist:
            print('Group "customer" does not exist.')

post_save.connect(customer_profile, sender=User)