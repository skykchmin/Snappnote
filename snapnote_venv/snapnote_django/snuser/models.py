from django.db import models

# Create your models here.
class Snuser(models.Model):
    username = models.CharField(max_length=64, verbose_name='사용자명')
    sdfsffsf