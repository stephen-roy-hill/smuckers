from django.db import models

# Create your models here.

class ForkliftDriver(models.Model):

	def __str__(self):
		return self.first_name + ' ' + self.last_name

	first_name = models.CharField(max_length=50, default='', blank=True)
	last_name = models.CharField(max_length=50, default='', blank=True)

class Bol(models.Model):

	def __str__(self):
	   return 'Bol: ' + str(self.bol_number)

	bol_number = models.IntegerField(default=0)

	dock_number = models.CharField(max_length=100, default='', blank=True)
	seal_number = models.CharField(max_length=100, default='', blank=True)

	bill_of_lading = models.CharField(max_length=100, default='', blank=True)
	shipping_order = models.CharField(max_length=100, default='', blank=True)
	shippers_number = models.CharField(max_length=100, default='', blank=True)
	agents_number = models.CharField(max_length=100, default='', blank=True)

	date = models.DateTimeField()
	from_address = models.CharField(max_length=400, default='', blank=True)

	cosigned_to = models.CharField(max_length=100, default='', blank=True)
	destination = models.CharField(max_length=100, default='', blank=True)
	state_of = models.CharField(max_length=20, default='', blank=True)
	county_of = models.CharField(max_length=50, default='', blank=True)
	route = models.CharField(max_length=100, default='', blank=True)
	delivering_carrier = models.CharField(max_length=100, default='', blank=True)
	car_initial = models.CharField(max_length=50, default='', blank=True)
	car_number = models.CharField(max_length=50, default='', blank=True)

	truck_approved = models.BooleanField(default=False)
	approved = models.BooleanField(default=False)

	forklift_driver = models.ForeignKey(ForkliftDriver, default=True, on_delete=models.SET_DEFAULT)

class BolItem(models.Model):

	def __str__(self):
	   return 'Bol Item: ' + self.description

	bol = models.ForeignKey(Bol, on_delete=models.CASCADE)
	packages = models.IntegerField(default=0)
	description = models.CharField(max_length=400, default='')
	weight = models.IntegerField(default=0)
	class_or_rate = models.CharField(max_length=50, default='')
	check_column = models.BooleanField(default=False)