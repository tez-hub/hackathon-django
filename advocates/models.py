from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Advocates(models.Model):
    profile_pic = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200)
    bio = models.TextField()
    twitter = models.CharField(max_length=200)

    def __str__(self):
        return self.username

