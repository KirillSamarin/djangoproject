from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'create group of managers'

    def handle(self, *args, **options):
        managers_group = Group.objects.create(name="Managers")
        managers_group.permissions.clear()

        unpublish_permission = Permission.objects.get(codename='can_unpublish_product')
        delete_permission = Permission.objects.get(codename='delete_product')

        managers_group.permissions.add(unpublish_permission, delete_permission)
        managers_group.save()