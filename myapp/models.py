from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date_published')
    body = models.TextField()
    #index = models.IntegerField()

    def __str__(self):
        return self.title
    
    def  sum(self):
        return self.body[:10]    


class Blog2(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date_published')
    body = models.TextField()
    #index = models.IntegerField()

    def __str__(self):
        return self.title

    def sum(self):
        return self.body[:10]
