from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Post(models.Model):
        sno=models.AutoField(primary_key=True)
        tittle=models.CharField(max_length=120)
        author=models.CharField(max_length=120)
        content=models.TextField()
        views=models.IntegerField(default=0)
        timestamp=models.DateTimeField(blank=True)
        slug = models.CharField(max_length = 250, null = True, blank = True)
        #post_image=models.ImageField(upload_to='static/')
        def __str__(self):
          return self.tittle
       
class Comments(models.Model):
        sno=models.AutoField(primary_key=True)
        user=models.ForeignKey(User,on_delete=models.CASCADE)
        content=models.TextField()
        timestamp=models.DateTimeField(default=now)
        post = models.ForeignKey(Post,on_delete=models.CASCADE)
        parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
        def __str__(self):
          return self.content[0:15]+"... by "+self.user.username
 
 
 
 
 
 
     