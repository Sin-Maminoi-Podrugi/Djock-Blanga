from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    title = models.CharField(max_length = 60)
    text = models.TextField()
    data_create = models.DateTimeField(default = timezone.now)
    data_share = models.DateTimeField(blank = True,null = True)
    def share(self):
        self.data_share = timezone.now()
        self.save()
    def __str__(self):
        return self.title