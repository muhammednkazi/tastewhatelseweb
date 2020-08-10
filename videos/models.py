from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# here we create databse tables with their columns and column datatype.

# Create your models here.
# table product
class video(models.Model):
    video_id=models.AutoField(primary_key=True)
    author=models.CharField(max_length=50,default="")
    title=models.CharField(max_length=150,default="")
    link=models.CharField(max_length=500,default="")
    category=models.CharField(max_length=50,default="")
    content=models.TextField(max_length=3000,default="")
    slug=models.CharField(max_length=150,default="")
    timestamp=models.DateTimeField(auto_now_add=True,blank = True)
    thumbnail=models.ImageField(upload_to="videos/images",default="")
    
    # this function displays product names on the table rows.
    def __str__(self):
        return self.title

class videoComment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    video_id=models.ForeignKey(video, on_delete=models.CASCADE)
    parent= models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:15] + " by " + self.user.first_name
    
