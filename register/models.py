# import random
# import string
from django.db import models

# Create your models here.
# def genexid(size=5,nums=string.digits):
# 	exid='EXLID'
# 	for _ in range(size):
# 	 exid +=random.choice(nums)
# 	return exid

# def uniqueid():
# 	code=genexid()
# 	qs=userinfo.objects.filter(excelid=code).exists()
#     	if qs:
#         	uniqueid()
#         return code



class userinfo(models.Model):

    class Meta:
        verbose_name = "userinfo"
        verbose_name_plural = "userinfos"

    excelid=models.CharField(max_length=10,primary_key=True,default='excel',null=False)
    name=models.CharField(max_length=100,null=True)
    college=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=50,null=True)
    phone=models.CharField(max_length=10,null=True)
    present=models.BooleanField(default=False)
    stay=models.BooleanField(default=False)
    printed=models.BooleanField(default=False)
    participated_events=models.CharField(max_length=100,blank=True)

    
    def __str__(self):
        k=self.excelid+":  "+self.name
    	return str(k)
  
    # def save(self,*args,**kwargs):
    # 	code=uniqueid()
    # 	self.excelid=code
    # 	super(userinfo,self).save(*args,**kwargs)

class winners(models.Model):
    excelid = models.CharField(blank=True, max_length=30)
    event = models.CharField(blank=True, max_length=50)
    name = models.CharField(max_length=100,null=True)
    college = models.CharField(blank=True, max_length=50)
    position= models.IntegerField(blank=False, default =0)
    printed=models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.excelid

class paid_userinfo(models.Model):

    class Meta:
        verbose_name = "paid_userinfo"
        verbose_name_plural = "paid_userinfos"

    excelid=models.CharField(max_length=10,primary_key=True,default='excel',null=False)
    name=models.CharField(max_length=100,null=True)
    college=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=50,null=True)
    phone=models.CharField(max_length=10,null=True)
    present=models.BooleanField(default=False)
    stay=models.BooleanField(default=False)
    printed=models.BooleanField(default=False)
    event=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return str(self.name)

class paid_winners(models.Model):
    excelid = models.CharField(blank=True, max_length=30)
    event = models.CharField(blank=True, max_length=50)
    name = models.CharField(max_length=100,null=True)
    college = models.CharField(blank=True, max_length=50)
    position= models.IntegerField(blank=False, default =0)
    printed=models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.excelid