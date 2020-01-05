from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.

class Audit(models.Model):
    audit_md = models.DateTimeField(auto_now=True)
    audit_cd = models.DateTimeField(auto_now_add=True)

class Post(Audit):
    title = models.CharField(max_length=200)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)  #auto_now_add=True - cannot be changed
    thumbs_up = models.IntegerField(default=0)
    thumbs_down = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(Audit):
    conttent = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_c = models.ForeignKey(Post,on_delete=models.CASCADE)

class Thumb(Audit):
    DIRECTION = (
        ('UP', 'Thumbs up'),
        ('DOWN', 'Thumbs down'),
    )
    direction = models.CharField(max_length=10,null=True, choices=DIRECTION)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_t = models.ForeignKey(Post,on_delete=models.CASCADE)