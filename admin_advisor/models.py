from django.db import models

# Create your models here.

class advisor_name(models.Model):
    name = models.CharField(max_length=100, default="", editable=True)
    url = models.CharField(max_length=100, default="", editable=True)
    advisor_id = models.IntegerField(default = 0)
    def __str__(self):
        return self.name