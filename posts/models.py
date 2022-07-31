from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=25)
    body = models.CharField(max_length=500)
    # resp = models.CharField(max_length=500,default = '')

    def __str__(self):
        return f"{self.title}"

# class Resp_Post(models.Model):
#     title = models.CharField(max_length=25)
#     body = models.CharField(max_length=500)
#     resp = models.CharField(max_length=500)