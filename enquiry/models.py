from django.db import models

# Create your models here.


class Enquiry(models.Model):
    id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=200)

    class Meta:
        app_label = 'mysite'
        db_table = "enquiry"
