from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import uuid


class Device(models.Model):
    device_id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)

    prev_lng = models.FloatField()
    prev_lat = models.FloatField()

    class Meta:
        db_table = 'devices'

    @staticmethod
    def register_device(lng, lat):
        device = Device(prev_lng=lng, prev_lat=lat)

        device.save()
        return device

    @staticmethod
    def find_device(device_id):
        try:
            device = Device.objects.get(device_id=device_id)

            return device

        except ObjectDoesNotExist:
            return None


