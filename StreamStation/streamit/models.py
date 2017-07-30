import uuid
from django.db import models
from streamit.utils import generate_key

class Show(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True)
    key = models.CharField(max_length=2047, unique=True)
    m3u8 = models.CharField(max_length=2047, blank=True, null=True)
    activated = models.BooleanField(default=False)
    last_on = models.DateTimeField(blank=True, null=True)
    last_off = models.DateTimeField(blank=True, null=True)
    on_air = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.uid and not(self.key):
            self.key = generate_key(self.uid.hex)
        super(Show, self).save(*args, **kwargs)

    def suid(self):
        return self.uid.hex[:8]

