from django.db import models


class Vaccine(models.Model):
    vaccine = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f'{self.vaccine}'


class VaccineSchedule(models.Model):
    CYCLE_CHOICES = [
        ('D', 'DAILY'),
        ('W', 'WEEKLY'),
        ('M', 'MONTHLY'),
        ('Y', 'YEARLY')
    ]

    vaccine = models.ForeignKey(Vaccine, related_name='vaccine_schedule', on_delete=models.CASCADE)
    schedule = models.DateTimeField()
    status = models.BooleanField(default=False)
    cycle = models.CharField(max_length=1, choices=CYCLE_CHOICES, default='D')

    def __str__(self):
        return f'{self.vaccine} - {self.schedule}'
