from django.db import models

# Create your models here.
# table contactus
class contactus(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=70,default="")
    phone=models.CharField(max_length=13,default="")
    email=models.CharField(max_length=100,default="")
    desc=models.TextField(max_length=1000,default="")
    timestamp=models.DateTimeField(auto_now_add=True,blank = True)

    # this function displays customer's name on the table rows.
    def __str__(self):
        return self.name