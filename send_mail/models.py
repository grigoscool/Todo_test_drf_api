from django.db import models


class Reminder(models.Model):
    text = models.CharField(max_length=255)
    email = models.EmailField()
    delay_minutes = models.IntegerField()

    def __str__(self):
        return f'Remind after {self.delay_minutes}'
