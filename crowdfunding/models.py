from django.conf import settings
from django.db import models


class Reward(models.Model):
	name = models.CharField(max_length=255, verbose_name='Reward Name')
	min_amount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Minimum Amount")
	desc = models.CharField(max_length=255, verbose_name='Reward Description')
	short_desc = models.CharField(max_length=255, verbose_name='Short Reward Description')
	img = models.URLField(verbose_name='Image URL', blank=True)

	def __str__(self):
		return self.name


class Order(models.Model):
	PAY_TYPES = (
		('CC', 'Credit Card'),
		('BT', 'Bank Transfer'),
	)

	created_at = models.DateTimeField(auto_now=True)

	name = models.CharField(max_length=255, verbose_name='Name')
	addr1 = models.CharField(max_length=255, verbose_name='Address 1')
	addr2 = models.CharField(max_length=255, verbose_name='Address 2', blank=True)
	city = models.CharField(max_length=255, verbose_name='City')
	state = models.CharField(max_length=255, verbose_name='State/Province')
	pcode = models.CharField(max_length=255, verbose_name='Postal Code')
	country = models.CharField(max_length=255, verbose_name='Country')
	reward = models.ForeignKey(Reward, related_name='+', verbose_name='Reward Level', blank=True, null=True, on_delete=models.CASCADE)
	amount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Amount')
	ptype = models.CharField(max_length=2, choices=PAY_TYPES, verbose_name='Payment Type')
	pref = models.CharField(max_length=255, verbose_name='Payment Reference', blank=True)
	email = models.EmailField(verbose_name='Email')
	notify = models.BooleanField(verbose_name="Notify me if the project team posts an update?")
	namecredit = models.CharField(max_length=255, verbose_name='Credit Name', blank=True)
	notes = models.CharField(max_length=255, verbose_name='Notes', blank=True)
