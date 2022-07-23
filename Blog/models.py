from django.db import models


class Blog(models.Model):
    BlogId = models.CharField(max_length=30)
    Title = models.CharField(max_length=200)
    Author_Name = models.CharField(max_length=300)
    Start_Date = models.DateField()
    End_Date = models.DateField()

    class Meta:
        db_table = 'Blog'
