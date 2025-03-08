from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    author = models.CharField(max_length = 80)
    title = models.CharField(max_length = 60)
    text = models.TextField()
    data_create = models.DateTimeField(auto_now_add = True)
    data_share = models.DateTimeField(auto_now_add = True)
    ispublisht = models.BooleanField(default = True)
    #def share(self):
        #self.data_share = timezone.now()
        #self.save()
    def __str__(self):
        return self.title