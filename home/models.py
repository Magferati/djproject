from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title
    