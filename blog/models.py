from django.db import models

class Category(models.Model):
		name=models.CharField(max_length=50)
class Tag(models.Model):
		name=models.CharField(max_length=50)
	
# Create your models here.
class Post(models.Model):
	Title=models.CharField(max_length=100)
	Date=models.DateField()
	Content=models.TextField()
	Category=models.ForeignKey(Category, on_delete=models.CASCADE)
	Author=models.CharField(
				verbose_name="Author Name",
				help_text="Enter Author Name",
				max_length=30,
				blank=True,
				null=True
				)
	
	def __str__(self):
		return self.Title
	
