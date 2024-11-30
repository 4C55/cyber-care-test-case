from django.db import models

class Event(models.Model):
    event_type = models.CharField(max_length=255)
    event_payload = models.TextField()

    def __str__(self):
        return f"{self.event_type}: {self.event_payload[:50]}"