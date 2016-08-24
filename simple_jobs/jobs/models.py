from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.TextField(max_length=120)
    
    def __str__(self):
        return self.title
    
