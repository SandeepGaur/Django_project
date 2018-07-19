from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length = 150)
    technologies = models.CharField(max_length = 150)
    detail = models.TextField(max_length = 500)
    url_project = models.URLField(max_length = 200)
    github_link = models.CharField(max_length = 150)

class blog(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField(max_length=10000)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length = 100)
