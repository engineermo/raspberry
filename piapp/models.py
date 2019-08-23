from django.db import models

# Create your models here.
class PiFour(models.Model):
    name = models.CharField(max_length=200)
    pi_type = models.CharField(max_length=20)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

