from django.db import models

# Create your models here.
LABEL = (
	('hot', 'hot'),
	('hot', 'hot'),
	)
class Product(models.Model):
	title = models.CharField(max_length = 255)
	image = models.CharField(max_length = 255)
	price = models.FloatField()
	label = models.CharField(max_length = 25, choices = LABEL)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.title

class Discount(models.Model):
	code = models.CharField(max_length = 8)
	percent = models.FloatField()
	name = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	expire = models.DateTimeField()

	def __str__(self):
		return self.code

class Cart(models.Model):
	user = models.CharField(max_length = 255)
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	quantity = models.IntegerField()
	price = models.FloatField()
	created_at = models.DateTimeField(auto_now_add = True)
