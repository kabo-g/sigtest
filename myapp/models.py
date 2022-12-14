from django.db import models

# Create your models here.

class Signature(models.Model):

    firstname = models.CharField(max_length = 255, blank=True, null=True)
    lastname = models.CharField(max_length = 255, blank=True, null=True)
    email = models.EmailField(max_length = 255, blank=True, null=True, unique=True)
    signature = models.ImageField(upload_to = 'images_sig/', blank=True, null=True)

    def __str__(self):
        return self.firstname + ' ' + self.lastname
