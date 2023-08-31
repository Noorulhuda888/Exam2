from django.db import models

class BlogPost(models.Model):
  title = models.CharField(max_length=255)
  content = models.CharField(max_length=255)
  pub_data = models.CharField(max_length=255)
  author = models.CharField(max_length=255, null=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    discription = models.CharField(max_length=255)