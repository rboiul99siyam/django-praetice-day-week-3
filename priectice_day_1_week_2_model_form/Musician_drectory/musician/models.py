from django.db import models

# Create your models here.
class Musicians(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    Instrument_type = models.TextField()

    def __str__(self) -> str:
        return self.first_name
