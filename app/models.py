from django.db import models

# Create your models here.

class Code(models.Model):
	code_type = models.CharField(max_length=3)
	code_desc = models.CharField(max_length=20)
	
	def __str__(self):
		return self.code_desc
		
class Prop(models.Model):
	short_name = models.CharField(max_length=5)
	address = models.CharField(max_length=30, blank=True)
	city = models.CharField(max_length=15, blank=True)
	state = models.CharField(max_length=2, blank=True)
	zip = models.CharField(max_length=10, blank=True)
	comment = models.TextField(blank=True)
	enis_no = models.IntegerField(blank=True, null=True)
	mgmt_co = models.CharField(max_length=5, blank=True)
	mgmt_pct = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

	def __str__(self):
		return "{} - {}".format(self.short_name, self.address)
	
class Tran(models.Model):
	prop = models.ForeignKey('Prop')
	date = models.DateField()
	code = models.ForeignKey('Code')
	comment = models.TextField()
	amt = models.DecimalField(max_digits=9, decimal_places=2)
	date_modified = models.DateField(auto_now=True)
	
	def __str__(self):
		return "{} - {} - {} - {}".format(self.prop, self.date, self.code, self.amt)